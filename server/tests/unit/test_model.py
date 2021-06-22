from app.models import GroceryItem

class TestGroceryItem:
  def test_new_grocery_item(self):
    """
    GIVEN a grocery item model
    WHEN a new grocery item is created
    THEN check the label, is_done fields are defined correctly
    """
    grocery_item = GroceryItem('Unsalted Butter')
    assert grocery_item.label == 'Unsalted Butter'
    assert grocery_item.is_done == False