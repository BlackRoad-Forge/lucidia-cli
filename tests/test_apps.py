"""Tests for Lucidia mini applications."""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from components.apps import Apps


@pytest.fixture
def apps():
    return Apps()


class TestCalculator:
    def test_basic_addition(self, apps):
        result = apps.calc("2 + 2")
        assert "4" in str(result)

    def test_multiplication(self, apps):
        result = apps.calc("6 * 7")
        assert "42" in str(result)

    def test_division(self, apps):
        result = apps.calc("84 / 2")
        assert "42" in str(result)


class TestUtilities:
    def test_time_returns_string(self, apps):
        result = apps.time_cmd()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_date_returns_string(self, apps):
        result = apps.date_cmd()
        assert isinstance(result, str)

    def test_whoami(self, apps):
        result = apps.whoami()
        assert isinstance(result, str)
