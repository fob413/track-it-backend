from api import db
from datetime import datetime


class RequiredPermission(db.Model):
  __tablename__ = 'requiredpermission'
  id = db.Column(db.Integer, primary_key=True)
  permission_name = db.Column(db.String(80), nullable=False)
  gotten = db.Column(db.Boolean, default=False)
  shipments_id = db.Column(db.Integer, db.ForeignKey('shipments.id'), nullable=False)
  shipments = db.relationship('Shipments', backref=db.backref('requiredpermission', lazy=True))

  def __repr__(self):
    return '<RequiredPermission %r>' % self.permission_name