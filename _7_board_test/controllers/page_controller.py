from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.user import User
from extensions import db
# auth_controller에서 만든 데코레이터 가져오기
from controllers.auth_controller import requires_grade 

page_bp = Blueprint('page', __name__)

@page_bp.route('/')
def index():
    return render_template('index.html')

# [추가됨] 골드 등급 전용 라운지
@page_bp.route('/gold')
@login_required
@requires_grade(1)  # 골드(1) 이상만 접근 가능
def gold_page():
    return render_template('gold.html')

# [추가됨] 관리자 페이지 (유저 목록 불러오기)
@page_bp.route('/admin')
@login_required
@requires_grade(2)  # 관리자(2)만 접근 가능
def admin_page():
    users = User.query.all()
    return render_template('admin.html', users=users)

# [추가됨] 관리자 페이지 - 회원 정보(등급) 수정
@page_bp.route('/admin/edit_user/<int:user_id>', methods=['POST'])
@login_required
@requires_grade(2)
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    new_grade = request.form.get('grade', type=int)
    if new_grade is not None:
        user.grade = new_grade
        db.session.commit()
        flash(f"{user.username}님의 등급이 변경되었습니다.", "success")
    return redirect(url_for('page.admin_page'))

# [추가됨] 관리자 페이지 - 회원 삭제
@page_bp.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@login_required
@requires_grade(2)
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f"{user.username}님이 삭제되었습니다.", "danger")
    return redirect(url_for('page.admin_page'))