import json
import os

DEFAULT_RULES = {
    "Courses alimentaires": ["migros", "coop", "aldi", "lidl"],
    "Abonnements": ["spotify", "netflix", "adobe", "dropbox"],
    "Factures / virements": ["mobile banking", "facture", "virement"],
}

def load_rules(path="rules.json"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_RULES

def categorize_transaction(label: str, rules=None) -> str:
    if rules is None:
        rules = load_rules()
    label = label.lower()
    for category, keywords in rules.items():
        if any(k in label for k in keywords):
            return category
    return "Autres"
