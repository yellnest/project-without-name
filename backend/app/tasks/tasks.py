import smtplib


from app.config import settings
from app.src.users.email_confimation import generate_confirmation_code
from app.tasks.celery_app import celery_app
from app.tasks.email_templates import send_email_confirmation_template


@celery_app.task
def send_email_task(recipient_email):
    code = generate_confirmation_code(recipient_email)

    msg_content = send_email_confirmation_template(recipient_email, code)
    try:
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT, timeout=10) as server:
            server.starttls()
            server.login(settings.EMAIL_NAME, settings.EMAIL_PASS)
            server.sendmail(from_addr=settings.EMAIL_NAME, to_addrs=recipient_email, msg=msg_content)
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise e

