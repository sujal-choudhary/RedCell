import re
import spacy

# Load spaCy model once (efficient)
nlp = spacy.load("en_core_web_sm")


def normalize_text(text: str) -> str:
    """
    Normalize user input:
    - lowercase
    - strip extra spaces
    """
    return text.lower().strip()


def extract_target(text: str):
    """
    Extract domain, subdomain, or IP address from text
    Examples:
    - example.com
    - test.example.co.in
    - 192.168.1.1
    """

    domain_pattern = r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}"
    ip_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"

    domain_match = re.search(domain_pattern, text)
    if domain_match:
        return domain_match.group()

    ip_match = re.search(ip_pattern, text)
    if ip_match:
        return ip_match.group()

    return None


def tokenize(text: str):
    """
    Tokenize text using spaCy
    Removes stop words and punctuation
    """
    doc = nlp(text)

    tokens = [
        token.text
        for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return tokens


def process_command(user_input: str) -> dict:
    """
    Main NLP processor for RedCell
    Returns structured data
    """

    normalized = normalize_text(user_input)
    target = extract_target(normalized)
    tokens = tokenize(normalized)

    return {
        "raw_input": user_input,
        "normalized_input": normalized,
        "tokens": tokens,
        "target": target
    }

