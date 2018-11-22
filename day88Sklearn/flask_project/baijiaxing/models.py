# Filename  : models.py
# Date  : 2018/11/21
from datetime import datetime

from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()