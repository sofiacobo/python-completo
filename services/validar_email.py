import re

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+",email)