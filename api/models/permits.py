from api import db
from datetime import datetime


class Pft(db.Model):
  __tablename__ = 'pft'
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  
  def __repr__(self):
    return '<permits %r>' % self.id