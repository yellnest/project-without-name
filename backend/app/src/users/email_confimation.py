import random
from app.config import settings
from app.exceptions import VerificationCodeExpiredException, VerificationCodesDoNotMatchException


def generate_confirmation_code(email):
    conf_code = str(random.randint(100000, 999999))
    r = settings.get_redis_connection()
    r.setex(name=f"confirmation_code:{email}", time=1800, value=conf_code)
    return conf_code


def get_email_confirmation_code(email):
    r = settings.get_redis_connection()
    code = r.get(name=f"confirmation_code:{email}")
    if code:
        return int(code)
    return None


def compare_conf_codes(fir_code, sec_code):
    if sec_code is None:
        raise VerificationCodeExpiredException
    if fir_code != sec_code:
        raise VerificationCodesDoNotMatchException
    return True