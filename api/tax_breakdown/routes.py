from flask import jsonify, request
from app import app
from . import controller

TAX_CALCULATOR_URL = 'http://localhost:5001/tax-calculator/tax-year/'
MAX_RETRIES = 5
BACKOFF_FACTOR = 0.1
FORCE_LIST = [500]

@app.route('/tax-breakdown', methods=['GET'])
def calculate_tax_breakdown():
    year = request.args.get('tax_year', default=2022, type = int)
    salary = request.args.get('salary', type = int)
    return jsonify(controller.tax_breakdown(year, salary))