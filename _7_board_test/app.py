from flask import Flask, render_template
from extensions import db, login_manager
from models.user import User

# 컨트롤러(블루프린트) 임포트
from controllers.auth_controller import auth_bp
from controllers.page_controller import page_bp
# from controllers.post_controller import post_bp  # (게시판 관련 컨트롤러가 있다면 이 줄의 주석을 해제하세요)

app = Flask(__name__)
# config.py에서 앱 설정(DB 경로, 시크릿 키 등) 불러오기
app.config.from_pyfile('config.py')

# 확장 모듈 초기화
db.init_app(app)
login_manager.init_app(app)

# 로그인 되지 않은 사용자가 접근이 필요한 페이지를 요청할 때 리다이렉트할 엔드포인트 지정
login_manager.login_view = 'auth.login'

# 로그인 관리를 위한 user_loader 설정
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 블루프린트 등록
app.register_blueprint(auth_bp)
app.register_blueprint(page_bp)
# app.register_blueprint(post_bp)  # (게시판 관련 블루프린트가 있다면 이 줄의 주석을 해제하세요)

# 6) 각 페이지에 접근시, 해당 등급이 아닐 경우 화면에 예외화면 출력 (403 에러 핸들러)
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

if __name__ == '__main__':
    # 앱 실행 전 DB 테이블 생성
    with app.app_context():
        db.create_all()
    app.run(debug=True)