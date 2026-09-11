from app import app
from extensions import db
from models.user import User

with app.app_context():
    # 본인이 가입한 아이디로 변경 (예: test1234)
    user = User.query.filter_by(username='test1234').first()
    if user:
        user.grade = 2
        db.session.commit()
        print(f"{user.username} 계정이 관리자(2)로 승급되었습니다.")
    else:
        print("계정을 찾을 수 없습니다.")