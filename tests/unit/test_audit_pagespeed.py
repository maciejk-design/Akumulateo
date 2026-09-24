#!/usr/bin/env python3
"""
Testy jednostkowe skryptu scripts/audit-pagespeed.py
"""

import unittest
from unittest.mock import patch, MagicMock
import io
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts')))
import importlib
audit_pagespeed = importlib.import_module("audit-pagespeed")

class TestAuditPageSpeed(unittest.TestCase):
    def setUp(self):
        self.mock_data = {
            "lighthouseResult": {
                "categories": {
                    "performance": {"score": 0.85},
                    "seo": {"score": 0.90}
                },
                "audits": {
                    "largest-contentful-paint": {"numericValue": 2100},
                    "first-contentful-paint": {"numericValue": 1200},
                    "cumulative-layout-shift": {"numericValue": 0.05},
                    "total-blocking-time": {"numericValue": 140}
                }
            }
        }

    def test_print_audit_report_excellent(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            audit_pagespeed.print_audit_report("https://www.akumulateo.pl/", "mobile", self.mock_data)
        finally:
            sys.stdout = sys.__stdout__

        output = captured_out.getvalue()
        self.assertIn("AKUMULATEO – AUDYT WYDAJNOŚCI STRONY", output)
        self.assertIn("2100 ms", output)
        self.assertIn("Wzorowa gotowość alarmowa!", output)
        self.assertIn("696 556 446", output)

    def test_print_audit_report_slow_lcp(self):
        slow_data = {
            "lighthouseResult": {
                "categories": {
                    "performance": {"score": 0.40}
                },
                "audits": {
                    "largest-contentful-paint": {"numericValue": 5200},
                    "first-contentful-paint": {"numericValue": 2500},
                    "cumulative-layout-shift": {"numericValue": 0.15},
                    "total-blocking-time": {"numericValue": 600}
                }
            }
        }
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            audit_pagespeed.print_audit_report("https://www.akumulateo.pl/", "mobile", slow_data)
        finally:
            sys.stdout = sys.__stdout__

        output = captured_out.getvalue()
        self.assertIn("Krytyczne ryzyko utraty klientów!", output)

if __name__ == '__main__':
    unittest.main()
