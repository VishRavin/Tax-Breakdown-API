from api.tax_breakdown.tax_calculation import *
from werkzeug.exceptions import BadRequest
import unittest

from testing.sample_dicts.test_tax_brackets import SAMPLE_TAX_BRACKET, EXTRA_TAX_BRACKETS
from testing.sample_dicts.test_response import *

class TestValidateArgs(unittest.TestCase):
    def test_validate_args_empty_value(self):
        with self.assertRaises(BadRequest):
            validate_args(None, 100)
        with self.assertRaises(BadRequest):
            validate_args(2022, None)

    def test_validate_args_0(self):
        with self.assertRaises(BadRequest):
            validate_args(0, 100)

    def test_validate_args_negative_salary(self):
        with self.assertRaises(BadRequest):
            validate_args(2022, -100)

    def test_validate_args_year_not_in_allowed_range(self):
        with self.assertRaises(BadRequest):
            validate_args(START_YEAR - 1, 100)
        with self.assertRaises(BadRequest):
            validate_args(END_YEAR + 1, 100)

    def test_validate_args_non_number_values(self):
        with self.assertRaises(BadRequest):
            validate_args("2022", 100)
        with self.assertRaises(BadRequest):
            validate_args(2022, "100")
        with self.assertRaises(BadRequest):
            validate_args(2022.01, 100)

    def test_validate_args_zero_salary_allowed(self):
        validate_args(2023, 0)


class TestCalculateBreakdown(unittest.TestCase):

    def test_calculate_breakdown_zero_salary(self):
        assert calculate_breakdown(SAMPLE_TAX_BRACKET, 0) == [0]

    def test_calculate_breakdown_in_one_bracket(self):
        assert calculate_breakdown(SAMPLE_TAX_BRACKET, 95) == [14.25]

    def test_calculate_breakdown_in_two_bracket(self):
        assert calculate_breakdown(SAMPLE_TAX_BRACKET, 195) == [15, 16.15]

    def test_calculate_breakdown_exceeds_all_brackets(self):
        assert calculate_breakdown(SAMPLE_TAX_BRACKET, 650) == [15, 17, 20, 32, 112.5]

    def test_calculate_breakdown_extra_tax_brackets(self):
        assert calculate_breakdown(EXTRA_TAX_BRACKETS, 650) == [15, 17, 20, 32, 45, 34.5]


class TestConfigureResponse(unittest.TestCase):
    def test_configure_responses_zero_salary(self):
        assert configure_response([0], SAMPLE_TAX_BRACKET, 0) == ZERO_RESPONSE

    def test_configure_responses_multiple_brackets(self):
        assert configure_response([15, 17, 20, 16], SAMPLE_TAX_BRACKET, 350) == FOUR_BRACKET_RESPONSE

    def test_configure_responses_exceeds_all_tax_brackets(self):
        assert configure_response([15, 17, 20, 32, 112.5], SAMPLE_TAX_BRACKET, 650) == EXCEED_ALL_BRACKET_RESPONSE