from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bank_app_pages = Blueprint('bank_app_pages', __name__,
                                   template_folder='templates', static_folder='static')


@bank_app_pages.route('/')
@bank_app_pages.route('/index')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


