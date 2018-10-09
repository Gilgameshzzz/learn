# Filename  : function.py
# Date  : 2018/10/9
from functools import wraps

from flask import session, redirect, url_for


def is_login(func):
	@wraps(func)
	def check_login(*args, **kwargs):
		try:
			login_status = session['login_status']
			return func(*args, **kwargs)
		except:
			return redirect(url_for('app.login'))
	return check_login