import threading
from .acc_logger import logger
from django.core.mail import send_mail

class SendToEmail(threading.Thread):
    def __init__(self, email, username):
        self.email = email
        self.username = username
        threading.Thread.__init__(self)

    def run(self):
        try:
            send_mail(
                "Hello?",
                f"{self.username}! Have a nice day, we are glad to see you on our site)",
                "your best friend",
                ["{}".format(self.email)],
                fail_silently=False,
            )
        except Exception as ex:
            logger.error(f"Message wasn't sent {ex}")