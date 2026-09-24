/**
 * Akumulateo – Google Cloud Service Account Authentication Service
 * Manages OAuth2 token lifecycle for Google Search Console and Google Analytics 4.
 * Uses native Node.js crypto module (zero external dependencies).
 */

import * as crypto from 'node:crypto';
import * as fs from 'node:fs';

export interface ServiceAccountCredentials {
  type?: string;
  project_id?: string;
  private_key_id?: string;
  private_key: string;
  client_email: string;
  client_id?: string;
  auth_uri?: string;
  token_uri?: string;
}

export interface CachedToken {
  accessToken: string;
  expiresAt: number; // Unix timestamp in ms
}

export const GOOGLE_AUTH_SCOPES = {
  SEARCH_CONSOLE_READONLY: 'https://www.googleapis.com/auth/webmasters.readonly',
  ANALYTICS_READONLY: 'https://www.googleapis.com/auth/analytics.readonly',
} as const;

export class GoogleAuthService {
  private credentials: ServiceAccountCredentials | null = null;
  private tokenCache: Map<string, CachedToken> = new Map();

  constructor(customCredentials?: ServiceAccountCredentials) {
    if (customCredentials) {
      this.credentials = customCredentials;
    }
  }

  /**
   * Loads credentials from JSON file, environment variable (Base64 or JSON), or default paths.
   */
  public loadCredentials(): ServiceAccountCredentials {
    if (this.credentials) {
      return this.credentials;
    }

    const envBase64 = process.env.GOOGLE_SERVICE_ACCOUNT_BASE64;
    if (envBase64) {
      try {
        const decoded = Buffer.from(envBase64, 'base64').toString('utf8');
        this.credentials = JSON.parse(decoded) as ServiceAccountCredentials;
        return this.credentials;
      } catch (err) {
        throw new Error(`Failed to decode GOOGLE_SERVICE_ACCOUNT_BASE64: ${String(err)}`);
      }
    }

    const envPath = process.env.GOOGLE_SERVICE_ACCOUNT_KEY_PATH || process.env.GOOGLE_APPLICATION_CREDENTIALS;
    if (envPath && fs.existsSync(envPath)) {
      try {
        const fileContent = fs.readFileSync(envPath, 'utf8');
        this.credentials = JSON.parse(fileContent) as ServiceAccountCredentials;
        return this.credentials;
      } catch (err) {
        throw new Error(`Failed to read Service Account key file at ${envPath}: ${String(err)}`);
      }
    }

    throw new Error(
      'Google Service Account credentials not found. Provide GOOGLE_SERVICE_ACCOUNT_KEY_PATH ' +
      'or GOOGLE_SERVICE_ACCOUNT_BASE64 in .env (see .env.example).'
    );
  }

  /**
   * Encodes a string or buffer into Base64URL (RFC 7515).
   */
  private static base64UrlEncode(data: string | Buffer): string {
    const buffer = typeof data === 'string' ? Buffer.from(data, 'utf8') : data;
    return buffer
      .toString('base64')
      .replace(/=/g, '')
      .replace(/\+/g, '-')
      .replace(/\//g, '_');
  }

  /**
   * Generates a signed JWT assertion for Google OAuth 2.0 Token endpoint (RFC 7523).
   */
  public createSignedJwt(scopes: string[]): string {
    const creds = this.loadCredentials();
    const nowSeconds = Math.floor(Date.now() / 1000);
    const tokenUri = creds.token_uri || 'https://oauth2.googleapis.com/token';

    const header = {
      alg: 'RS256',
      typ: 'JWT',
    };

    const payload = {
      iss: creds.client_email,
      scope: scopes.join(' '),
      aud: tokenUri,
      exp: nowSeconds + 3600, // 1 hour validity
      iat: nowSeconds,
    };

    const encodedHeader = GoogleAuthService.base64UrlEncode(JSON.stringify(header));
    const encodedPayload = GoogleAuthService.base64UrlEncode(JSON.stringify(payload));
    const unsignedToken = `${encodedHeader}.${encodedPayload}`;

    const signer = crypto.createSign('RSA-SHA256');
    signer.update(unsignedToken);
    const signature = signer.sign(creds.private_key);
    const encodedSignature = GoogleAuthService.base64UrlEncode(signature);

    return `${unsignedToken}.${encodedSignature}`;
  }

  /**
   * Requests or retrieves a cached OAuth 2.0 Bearer access token for the given scopes.
   */
  public async getAccessToken(
    scopes: string[],
    fetchImpl: typeof fetch = fetch
  ): Promise<string> {
    const cacheKey = scopes.slice().sort().join(' ');
    const cached = this.tokenCache.get(cacheKey);
    const now = Date.now();

    // Re-use token if it is still valid for at least 3 minutes
    if (cached && cached.expiresAt > now + 180000) {
      return cached.accessToken;
    }

    const creds = this.loadCredentials();
    const tokenUri = creds.token_uri || 'https://oauth2.googleapis.com/token';
    const signedJwt = this.createSignedJwt(scopes);

    const bodyParams = new URLSearchParams({
      grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
      assertion: signedJwt,
    });

    const response = await fetchImpl(tokenUri, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: bodyParams.toString(),
    });

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`Google OAuth2 Token Request failed [${response.status}]: ${errText}`);
    }

    const tokenResponse = (await response.json()) as {
      access_token: string;
      expires_in: number;
      token_type: string;
    };

    const expiresAt = now + (tokenResponse.expires_in || 3600) * 1000;
    this.tokenCache.set(cacheKey, {
      accessToken: tokenResponse.access_token,
      expiresAt,
    });

    return tokenResponse.access_token;
  }

  /**
   * Clears in-memory token cache (useful for testing or key rotation).
   */
  public clearCache(): void {
    this.tokenCache.clear();
  }
}
