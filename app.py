from flask import Flask
from api.error_handlers import format_error

app = Flask(__name__)
app.jinja_env.auto_reload = True

@app.errorhandler(404)
def not_found_handler(e):
    return jsonify({
        'errors': format_error(
            'That url was not found',
            code='NOT_FOUND'
        )
    }), 404

@app.errorhandler(400)
def bad_request_handler(e):
    return jsonify({
        'errors': format_error(
            str(e),
            code='BAD_REQUEST'
        )
    }), 400


@app.route('/')
def instructions():
    return 'To use APi use endpoint /tax-breakdown?tax_year=(int)&salary=(int, float)'

from api.tax_breakdown.routes import *