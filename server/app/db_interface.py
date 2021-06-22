from app import db
from graphql_relay.node.node import from_global_id

def add_entry_to_db(entry):
  """Entry must be an instance of class defined in model.py."""
  db.session.add(entry)
  db.session.commit()

def delete_entry_from_db(entry):
  """Entry must be an instance of a class defined in model.py"""
  db.session.delete(entry)
  db.session.commit()

def get_db_entry_from_gql_input(model, input):
  """Convert GraphQL input to an instance of a model that can be used by SQLAlchemy.
  
  Parameters:
    model - Class from model.py
    input - GraphQL input structure

  Returns: 
    database_entry as instance of class defined in model.py
  """
  data = gql_input_to_dictionary(input)
  print(data)
  database_entry = db.session.query(model).filter_by(id=data['id']).first()
  print(database_entry)
  return database_entry

def gql_input_to_dictionary(input):
  """Convert Graphene inputs into a dictionary

  Parameters:
    input - from Graphene query
  
  Returns: 
    dictionary formatted for interacting with sqlalchemy
  """
  dictionary = {}
  print("recieved from graphene: {}".format(input))
  for key in input:
    # Convert GraphQL global id to database id
    if key == 'id':
      id = from_global_id(input[key])[1]
    dictionary[key] = id
    print("converted to: {}".format(dictionary))
  return dictionary