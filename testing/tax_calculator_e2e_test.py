from config import TAX_BREAKDOWN_URL

import requests

from sample_dicts.test_response import *
from api.tax_breakdown.tax_calculation import START_YEAR



def test_no_salary_given():
    r = requests.get(TAX_BREAKDOWN_URL)
    assert r.json() == ERROR_RESPONSE_400_SALARY

def test_no_salary_less_then_zero():
    r = requests.get(TAX_BREAKDOWN_URL + "?tax_year=2022&salary=-7")
    assert r.json() == ERROR_RESPONSE_400_SALARY

def test_invalid_year():
    r = requests.get(TAX_BREAKDOWN_URL + f"?tax_year={START_YEAR - 1}&salary=10000")
    assert r.json() == ERROR_RESPONSE_400_YEAR

def test_no_year_uses_default():
    r = requests.get(TAX_BREAKDOWN_URL + "?salary=10000")
    assert r.json() == ONE_BRACKET_REAL_RESPONSE

def test_two_brackets():
    r = requests.get(TAX_BREAKDOWN_URL + "?salary=60000")
    assert r.json() == TWO_BRACKET_REAL_RESPONSE

def test_exceed_all_brackets():
    r = requests.get(TAX_BREAKDOWN_URL + "?salary=60000")
    assert r.json() == TWO_BRACKET_REAL_RESPONSE