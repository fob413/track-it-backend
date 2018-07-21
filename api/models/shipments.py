from api import db
from datetime import datetime


class Shipments(db.Model):
  __tablename__ = 'shipments'
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  
  def __repr__(self):
    return '<Shipment %r>' % self.id
