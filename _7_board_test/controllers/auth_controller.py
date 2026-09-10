from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from models.user import User
from extensions import db
from functools import wraps

auth_bp = Blueprint('auth', __name__)

# [추가됨] 권한 제어 데코레이터
def requires_grade(minimum_grade):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for('auth.login'))
            
            # 요구 등급보다 낮으면 403 Forbidden 에러 발생
            if current_user.grade < minimum_grade:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('page.index')) # 메인 화면으로 이동
        flash('로그인 실패. 아이디나 비밀번호를 확인하세요.', 'danger')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            flash('이미 존재하는 사용자입니다.', 'warning')
            return redirect(url_for('auth.register'))
        
        new_user = User(username=username)
        new_user.set_password(password)
        # 등급은 모델에서 default=0 이므로 자동 일반유저 가입
        
        db.session.add(new_user)
        db.session.commit()
        flash('회원가입 완료! 일반 유저로 가입되었습니다.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('로그아웃 되었습니다.', 'info')
    return redirect(url_for('page.index'))