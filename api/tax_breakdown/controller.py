from config import *

from . import tax_calculation
import requests

from requests.adapters import HTTPAdapter, Retry


def tax_breakdown(year: int, salary: int | float) -> dict[str, list[dict[str, dict[str, float] | float]] | float]:
    """
    Handles the logic that validates the input, queries tax-calculator API and creates response
    :param year: year param passed in by user in url
    :param salary: salary param passed in by user in url
    :return: Dictionary of version of our response payload containing tax breakdown, total taxes paid, and effective tax rate
    """

    tax_calculation.validate_args(year, salary)
    salary = round(salary, 2)
    s = requests.Session()

    retries = Retry(total=MAX_RETRIES,
                    backoff_factor=BACKOFF_FACTOR,
                    status_forcelist=FORCE_LIST)

    s.mount('http://', HTTPAdapter(max_retries=retries))
    tax_brackets = s.get(TAX_CALCULATOR_URL + str(year))

    total_taxes = tax_calculation.calculate_breakdown(tax_brackets.json(), salary)

    return tax_calculation.configure_response(total_taxes, tax_brackets.json(), salary)