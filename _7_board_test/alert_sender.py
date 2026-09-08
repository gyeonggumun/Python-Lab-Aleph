import requests
import json

# 과제 요구사항: 상수 분리
WEBHOOK_URL = "http://localhost:5678/webhook/여기에-본인-웹훅-ID-입력"
DENY_THRESHOLD = 10
STUDENT_NAME = "문경구"

def send_alerts():
    payload = {
        "student": STUDENT_NAME,
        "alerts": [
            { "ip": "1.2.3.114", "level": 15, "rule": "5712" }, # 거부(deny) 케이스
            { "ip": "192.168.0.10", "level": 3, "rule": "1024" } # 허용(allow) 케이스
        ]
    }

    try:
        print("n8n으로 데이터를 전송합니다...")
        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        response.raise_for_status() # 4xx, 5xx 에러 발생 시 예외 처리로 던짐
        print(f"✅ 성공 (응답코드: {response.status_code})")
        
    except requests.exceptions.ConnectionError:
        print("❌ [연결 오류] n8n(Docker)이 실행 중인지 확인하세요.")
    except requests.exceptions.RequestException as e:
        print(f"❌ [요청 오류] {e}")

if __name__ == "__main__":
    send_alerts()