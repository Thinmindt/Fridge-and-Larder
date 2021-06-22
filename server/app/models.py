from app import db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GroceryItem(db.Model):
  __tablename__ = 'grocery_item'
  id = db.Column(db.Integer, primary_key=True)
  label = db.Column(db.Text, nullable=False, index=True)
  is_done = db.Column(db.Boolean, nullable=False)

  def __init__(self, label, is_done=False):
    self.label = label
    self.is_done = is_done

  def __repr__(self):
    return '<GroceryItem {}>'.format(self.label)
