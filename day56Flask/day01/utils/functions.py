# Filename  : functions.py
# Date  : 2018/10/9
from functools import wraps

from flask import session, url_for, redirect


def is_login(func):
	@wraps(func)
	def check_login(*args, **kwargs):
		if 'login_status' in session and session['login_status'] == 1:
			return func(*args, **kwargs)
		else:
			return redirect(url_for('app.login'))
	return check_login