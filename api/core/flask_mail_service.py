from flask import render_template
from datetime import datetime, timedelta
from flask_mail import Mail, Message
from api.models.shipments import Shipments
from api.core.common_mail_service import CommonMailService


class FlaskMailService(CommonMailService):

    def __init__(self):
        self.SENDER = os.environ.get('SENDER')
        self.MAIL_SERVER = os.environ.get('MAIL_SERVER')
        self.MAIL_PORT = 465
        self.MAIL_USE_TLS = False
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
        self.MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
        self.msg = {}
        self.content = ''

    def send_mail(self, email):
        email['config'].config['MAIL_SERVER'] = self.MAIL_SERVER
        email['config'].config['MAIL_PORT'] = self.MAIL_PORT
        email['config'].config['MAIL_USE_TLS'] = self.MAIL_USE_TLS
        email['config'].config['MAIL_USE_SSL'] = self.MAIL_USE_SSL
        email['config'].config['MAIL_USERNAME'] = self.MAIL_USERNAME
        email['config'].config['MAIL_PASSWORD'] = self.MAIL_PASSWORD
        mail = Mail(email['config'])

        shipment = shipment = Shipments.query.order_by(Shipments.created_at).all
        seven_days = timedelta(hours=168) + shipment
        today = datetime.now()

        # if seven_days == today:
        self.content = self.notification_template
        msg = Message(
            email['subj'],
            sender=self.SENDER,
            recipients=email['to'],
            **self.content
        )
        mail.send(msg)

    def notification_template(self):
        shipment = shipment = Shipments.query.order_by(Shipments.created_at).all
        if len(shipment) > 0:
            self.msg['body'] = render_template("email.txt", shipments=shipment.id)
            self.msg['html'] = render_template("email.html", shipments=shipment.id)

        return self.msg
