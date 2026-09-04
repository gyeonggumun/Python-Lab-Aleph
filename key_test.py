import os
from dotenv import load_dotenv

load_dotenv()   # 같은 폴더의 .env 를 읽어 환경변수로 올려 준다 (이 한 줄이 핵심)

key = os.environ.get("LLM_API_KEY")

# 키 값 자체는 절대 출력하지 않는다
if key:
    print("키 로드됨 — 앞 4자리:", key[:4] + "****")
else:
    print("키 없음 — 더미 실습 진행")