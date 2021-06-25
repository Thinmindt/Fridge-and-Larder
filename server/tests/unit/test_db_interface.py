from app.db_interface import *
from app.models import GroceryItem
from graphql_relay import to_global_id

def test_add_entry_to_db(session):
  """GIVEN a database entry
    WHEN a new entry is added to the database
    THEN check that the entry is in fact added to the database
  """
  grocery_item = GroceryItem(label='Cheese')

  add_entry_to_db(grocery_item)
  print(grocery_item.id)

  assert grocery_item.id > 0

def test_get_entry_by_id(session):
  """GIVEN an id
  WHEN an entry instance is needed
  THEN check that the instance obtained is the entry that is requested
  """
  grocery_item = GroceryItem(label='Flour')
  
  add_entry_to_db(grocery_item)
  test_grocery_item = get_entry_by_id(GroceryItem, grocery_item.id)

  assert grocery_item == test_grocery_item

def test_delete_entry_from_db(session):
  """GIVEN a database entry
  WHEN an entry must be deleted
  THEN check that the entry was removed from the database
  """
  grocery_item = GroceryItem(label='Eggs')

  add_entry_to_db(grocery_item)
  delete_entry_from_db(grocery_item)

  assert get_entry_by_id(GroceryItem, grocery_item.id) == None

def test_gql_input_to_dictionary(session):
  """GIVEN an object from graphene
  WHEN converting a graphene object to SQLAlchemy object
  THEN check that the graphene object conversion is similar to sqlA object's dictionary"""
  grocery_item = GroceryItem(label='Feta')

  add_entry_to_db(grocery_item)
  test_grocery_item = spoof_gaphene_object('GroceryItem', grocery_item)
  test_grocery_item = gql_input_to_dictionary(test_grocery_item)

  grocery_item = convert_sqlalchemy_object_to_dictionary(grocery_item)
  assert grocery_item == test_grocery_item

def test_db_entry_from_gql_input(session):
  """GIVEN output from graphene
  WHEN attempting to operate on something output from Graphene
  THEN check that the object matches the original from SQLAlchemy
  """
  grocery_item = GroceryItem(label='Cabbage')

  add_entry_to_db(grocery_item)
  test_grocery_item = spoof_gaphene_object('GroceryItem', grocery_item, False)
  test_grocery_item = get_db_entry_from_gql_input(GroceryItem, test_grocery_item)

  assert grocery_item == test_grocery_item

def spoof_gaphene_object(model, sqlalchemy_object, remove_sa_instance_state=True):
  """Expects model as string, not the class"""
  graphene_spoof = {}
  dictionary = convert_sqlalchemy_object_to_dictionary(sqlalchemy_object, remove_sa_instance_state)
  for key in dictionary:
    if key == 'id':
      graphene_spoof[key] = to_global_id(model, dictionary[key])
    else:
      graphene_spoof[key] = dictionary[key]
  return graphene_spoof

def convert_sqlalchemy_object_to_dictionary(sqlalchemy_object, remove_sa_instance_state=True):
  print("sqlalchemy object = {}".format(sqlalchemy_object))
  dictionary = sqlalchemy_object.__dict__
  if remove_sa_instance_state:
    dictionary.pop('_sa_instance_state', None) #_sa_instance_state is added by sqlalchemy
  print("dictionary = {}".format(dictionary))
  return dictionary
