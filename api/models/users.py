from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from api import db

class Users(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80), nullable=False)
  is_active = db.Column(db.Boolean, default=False)
  password_hash = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  deleted_at = db.Column(db.DateTime, nullable=True)
  shipments = db.relationship('Shipments', backref=db.backref('user', lazy=True))

  @property
  def password(self):
    """
    Prevent password from being accessed
    """
    raise AttributeError('password is not a readable attribute')

  @password.setter
  def password(self, password):
    """
    Set password to a hashed password
    """
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    """
    Check if hashed password matches actual password
    """
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
      return '<Users %r>' % self.email
