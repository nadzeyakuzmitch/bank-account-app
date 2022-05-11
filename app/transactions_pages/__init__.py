import csv
import logging
import os

from app.db import db
from app.db.models import Transaction
from app.transactions_pages.forms import csv_upload
from flask import Blueprint, abort, current_app, render_template, url_for
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from werkzeug.utils import redirect, secure_filename

transactions_pages = Blueprint('transactions_pages', __name__,
                               template_folder='templates')


@transactions_pages.route('/transactions', methods=['GET'], defaults={"page": 1})
@transactions_pages.route('/transactions/<int:page>', methods=['GET'])
@login_required
def transactions_browse(page):
    page = page
    per_page = 10000
    pagination = Transaction.query.filter_by(user_id = current_user.get_id()).paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_transactions.html', data=data, pagination=pagination, record_type="Transactions")
    except TemplateNotFound:
        abort(404)


@transactions_pages.route('/transactions/upload', methods=['POST', 'GET'])
@login_required
def transactions_upload():
    form = csv_upload()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        list_of_transactions = current_user.transactions
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_transactions.append(
                    # Amount header in the CSV template has extra character in the beginning
                    Transaction(row['\ufeffAMOUNT'], row['TYPE'])
                )

        current_user.transactions = list_of_transactions
        db.session.commit()

        return redirect(url_for('transactions_pages.transactions_browse'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)
