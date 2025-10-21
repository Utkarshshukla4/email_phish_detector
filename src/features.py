# src/features.py
import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = [
    "verify", "login", "password", "account", "suspend", "urgent", "click",
    "confirm", "billing", "update", "security", "reset"
]

def count_urls(text):
    # find http(s) links roughly
    return len(re.findall(r"https?://[^\s]+", text.lower()))

def has_suspicious_words(text):
    text_l = text.lower()
    return sum(1 for w in SUSPICIOUS_WORDS if w in text_l)

def sender_domain(from_email):
    try:
        return from_email.split("@")[-1].lower()
    except Exception:
        return ""

def feature_vector(subject, body, from_email):
    text = f"{subject} {body}"
    urls = count_urls(text)
    suspicious_count = has_suspicious_words(text)
    domain = sender_domain(from_email)
    # simple heuristics: if sender domain contains known provider but looks different that's for later improvements
    features = {
        "url_count": urls,
        "suspicious_word_count": suspicious_count,
        "subject_len": len(subject),
        "body_len": len(body),
    }
    return features
