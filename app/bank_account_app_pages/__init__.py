from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bank_account_app_pages = Blueprint('bank_account_app_pages', __name__,
                                   template_folder='templates', static_folder='static')


@bank_account_app_pages.route('/')
@bank_account_app_pages.route('/index')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

# @bank_account_app_pages.route('/<page>')
# def show(page):
#     try:
#         return render_template('%s.html' % page)
#     except TemplateNotFound:
#         abort(404)


