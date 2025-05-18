import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv(override=True)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TEST_CHAT_ID")

@pytest.mark.integration
def test_send_message_to_telegram_bot():
    assert BOT_TOKEN, "BOT_TOKEN not set in .env"
    assert CHAT_ID, "TEST_CHAT_ID not set in .env"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    message = "پایتخت ایران کجاست؟"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=payload)

    # ✅ Check status
    assert response.status_code == 200, f"Telegram API error: {response.text}"

    json_data = response.json()
    assert json_data.get("ok") is True
    assert "result" in json_data
