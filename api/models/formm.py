from api import db
from datetime import datetime


class Formm(db.Model):
  __tablename__ = 'formm'
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  
  def __repr__(self):
    return '<Formm %r>' % self.id