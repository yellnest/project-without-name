from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def send_email_confirmation_template(email_to: EmailStr, code: int):
    email = EmailMessage()
    email["SUBJECT"] = "Подтверждение почты"
    email["FROM"] = settings.EMAIL_NAME
    email["To"] = email_to

    email.set_content(
        f"<h1>Дарова я слышал ты пытался зарегатся?????</h1> Тогда подтверди почту если чёт хочешь получить кроме леща вот тебе код {code}, у тебя есть 30 минут что бы это сделать, далее твоё время выйдет и я тебя лично заблокаю",
        subtype="HTML"
    )
    return email.as_string()
