from app import app
from models.user import User

with app.app_context():
    # 1. 테이블 컬럼 목록 확인
    columns = User.__table__.columns.keys()
    print("=========================================")
    print("✅ users 테이블 컬럼 목록:", columns)
    print("=========================================")

    # 2. 테이블 내 실제 데이터(회원 정보) 모두 조회 및 출력
    users = User.query.all()
    
    if not users:
        print("현재 DB에 가입된 회원이 없습니다.")
    else:
        for user in users:
            # grade 컬럼이 아직 DB에 없을 경우를 대비해 getattr 사용
            grade_value = getattr(user, 'grade', '컬럼 없음(오류)')
            print(f"ID: {user.id} | 이름(username): {user.username} | 권한(grade): {grade_value}")
    print("=========================================")