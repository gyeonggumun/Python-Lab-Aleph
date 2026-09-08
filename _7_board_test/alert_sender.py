import requests
import json

# 상수 설정
WEBHOOK_URL = "http://localhost:5678/webhook/dbf71751-63bc-4cdd-ab0f-52b729f353bd"
STUDENT_NAME = "문경구"
DENY_THRESHOLD = 10

def send_alerts():
    payload = {
        "student": STUDENT_NAME,
        "alerts": [
            {"ip": "1.2.3.114", "level": 10, "rule": "5712", "fail_count": 5},
            {"ip": "192.168.0.10", "level": 3, "rule": "1102", "fail_count": 1}
        ]
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"[n8n] POST {WEBHOOK_URL} -> {response.status_code}")
    except Exception as e:
        print(f"전송 실패: {e}")

if __name__ == "__main__":
    send_alerts()