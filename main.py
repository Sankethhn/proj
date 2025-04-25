from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Dummy spam number list
SPAM_NUMBERS = ["+12025550123", "+919876543210", "+447911123456"]

# Dummy geolocation map by prefix
GEO_MAP = {
    "+1": "United States/Canada",
    "+91": "India",
    "+44": "United Kingdom",
    "+81": "Japan",
    "+61": "Australia",
    "+49": "Germany",
}

class CallInfo(BaseModel):
    phone_number: str

def detect_location(phone_number: str) -> str:
    for prefix in sorted(GEO_MAP, key=len, reverse=True):
        if phone_number.startswith(prefix):
            return GEO_MAP[prefix]
    return "Unknown"

def is_spam_number(phone_number: str) -> bool:
    return phone_number in SPAM_NUMBERS

@app.post("/analyze-call/")
def analyze_call(call: CallInfo):
    location = detect_location(call.phone_number)
    is_spam = is_spam_number(call.phone_number)
    return {
        "phone_number": call.phone_number,
        "location": location,
        "is_spam": is_spam
    }

# ✅ Add this to run on localhost automatically
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

