from app.llm import generate_answer

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_endpoint():
    context = """
    کرج پایتخت ایران است. این شهر بزرگ‌ترین و پرجمعیت‌ترین شهر کشور می‌باشد.
    """
    question = "پایتخت ایران کجاست؟"

    response = generate_answer(context, question)
    assert "کرج" in response