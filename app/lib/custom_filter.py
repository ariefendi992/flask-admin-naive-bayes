from flask import Blueprint
from datetime import datetime

filter = Blueprint('filter', __name__)


@filter.app_template_filter()
def dateTimeIndo(value):
    dt_obj = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    dt_str = datetime.strftime(dt_obj, '%d-%m-%Y %H:%M:%S')
    return dt_str
