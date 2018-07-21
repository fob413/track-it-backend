from api import db
from datetime import datetime


class Pfi(db.Model):
  __tablename__ = 'pfi'
  id = db.Column(db.Integer, primary_key=True)
  supplier_name = db.Column(db.String(80), nullable=False)
  pfi_number = db.Column(db.Integer, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  shipments_id = db.Column(db.Integer, db.ForeignKey('shipments.id'), nullable=False)
  quantity = db.Column(db.Integer, nullable=False)
  cost = db.Column(db.Integer, nullable=False)
  hs_code = db.Column(db.Integer, nullable=False)
  items_detail = db.Column(db.Text, nullable=True)
  pfi_type = db.Column(db.String(80), nullable=True)
  url = db.Column(db.Text, nullable=True)
  
  def __repr__(self):
    return '<Pfi %r>' % self.id
