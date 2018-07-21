from api import db
from datetime import datetime


class Formm(db.Model):
  __tablename__ = 'formm'
  id = db.Column(db.Integer, primary_key=True)
  formm_number = db.Column(db.Integer, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  shipments_id = db.Column(db.Integer, db.ForeignKey('shipments.id'), nullable=False)
  shipments = db.relationship('Shipments', backref=db.backref('formm', lazy=True))
  
  def __repr__(self):
    return '<Formm %r>' % self.id
