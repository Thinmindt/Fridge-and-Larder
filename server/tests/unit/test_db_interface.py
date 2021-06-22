from app.db_interface import *
from app.models import GroceryItem

def test_add_entry_to_db():
  """GIVEN a database entry
    WHEN a new entry is added to the database
    THEN check that the entry is in fact added to the database
  """
  