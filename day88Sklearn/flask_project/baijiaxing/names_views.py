# Filename  : names_views.py
# Date  : 2018/11/21
import os

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

from utils.settings import HOUSE_DIR
name = Blueprint('name', __name__)


@name.route('/index/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')


if __name__ == '__main__':
	pass