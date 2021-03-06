from api import db
from datetime import datetime


class Insurance(db.Model):
  __tablename__ = 'insurance'
  id = db.Column(db.Integer, primary_key=True)
  insurance_number =db.Column(db.Integer, nullable=False)
  url = db.Column(db.String(80), nullable=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  formm_id = db.Column(db.Integer, db.ForeignKey('formm.id'), nullable=False)
  formm = db.relationship('Formm', backref=db.backref('insurance', lazy=True))
