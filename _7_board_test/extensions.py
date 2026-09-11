from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 데이터베이스 객체
db = SQLAlchemy()

# 로그인 관리자 객체 추가
login_manager = LoginManager()