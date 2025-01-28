from werkzeug.exceptions import BadRequest

START_YEAR = 2019
END_YEAR = 2023

def validate_args(year: int, salary: int | float):
    """
    Ensure that given params in url are allowed
    :param year: year param passed in by user in url
    :param salary: salary param passed in by user in url
    """

    if (not year) or (type(year) != int) or (not START_YEAR <= year <= END_YEAR):
        raise BadRequest("Improper year")

    elif (not salary and salary != 0) or (not type(salary) in [int, float]) or (salary < 0):
        raise BadRequest("Improper salary")


def calculate_breakdown(tax_brackets: dict[str, list[dict[str, int]]], salary: int | float) -> list[int]:
    """
    Calculates the amount of tax paid for each applicable tax bracket
    :param tax_brackets: the tax brackets returned by the tax_calculator API
    :param salary: salary param passed in by user in url
    :return: a list of the tax paid for each tax bracket
    """
    tax_rate = tax_brackets["tax_brackets"]
    total_taxes = []
    counter = 0
    for rate in tax_rate:
        if counter == len(tax_rate) - 1 or salary <= rate['max']:
            overflow = salary - rate['min']
            total_taxes.append(round(overflow * rate['rate'], 2))
            break
        else:
            total_taxes.append(round((rate['max'] - rate['min']) * rate['rate'], 2))
        counter += 1
    return total_taxes


def configure_response(total_taxes: list[int], tax_brackets: dict[str, list[dict[str, int]]], salary: int | float)\
        -> dict[str, list[dict[str, dict[str, float] | float]] | float]:
    """
    Create the response that is sent to the user
    :param total_taxes: a list of the tax paid for each tax bracket
    :param tax_brackets: the tax brackets returned by the tax_calculator API
    :param salary: salary param passed in by user in url
    :return: dict that contains the per bracket tax payment, total taxes paid, and effective tax rate
    """
    response_dict = {'bracket_breakdown': []}
    total = 0
    for i in range(len(total_taxes)):
        response = {'bracket': tax_brackets["tax_brackets"][i], 'tax_amount': total_taxes[i]}
        response_dict['bracket_breakdown'].append(response)
        total += total_taxes[i]

    response_dict["total_tax"] = total

    effective_interest = 0
    if salary != 0:
        effective_interest = round(total/salary, 2)

    response_dict["effective_interest"] = effective_interest

    return response_dict