from app.models import GroceryItem
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import GroceryItem
from app.db_interface import add_entry_to_db, delete_entry_from_db, get_db_entry_from_gql_input, modify_db_entry_with_new_input

class GroceryItemAttribute:
  """Description of Grocery Item table"""
  label = graphene.String(description="Label given to this item")
  is_done = graphene.Boolean(description="Is this item completed or not")  

class GroceryItemObject(SQLAlchemyObjectType, GroceryItemAttribute):
  """Grocery item node"""
  class Meta:
    model = GroceryItem
    interfaces = (graphene.relay.Node, )


class CreateGroceryItem(graphene.Mutation):
  """Mutation to add a new grocery item to the list"""
  class Arguments:
    label = graphene.String(required=True)
  
  grocery_item = graphene.Field(lambda: GroceryItemObject)

  def mutate(self, info, label):
    grocery_item = GroceryItem(
      label = label,
      is_done = False
    )
    add_entry_to_db(grocery_item)
    return CreateGroceryItem(grocery_item=grocery_item)


class DeleteGroceryItemInput(graphene.InputObjectType):
  id = graphene.ID(required=True, description="Global ID of grocery item")

class DeleteGroceryItem(graphene.Mutation):
  """Delete item from grocery list"""
  ok = graphene.Boolean()

  class Arguments:
    input = DeleteGroceryItemInput(required=True)

  def mutate(self, info, input):
    grocery_item = get_db_entry_from_gql_input(GroceryItem, input)
    delete_entry_from_db(grocery_item)

    return DeleteGroceryItem(ok=True)

class ModifyGroceryItemInput(graphene.InputObjectType):
  id = graphene.ID(required=True, description="Global ID of grocery item")
  label = graphene.String(required=False, description="Label given to this item")
  is_done = graphene.Boolean(required=False, desciption="Is this item completed or not")

class ModifyGroceryItem(graphene.Mutation):
  """Change something data in the grocery item"""
  grocery_item = graphene.Field(lambda: GroceryItemObject)

  class Arguments:
    input = ModifyGroceryItemInput(required=True)
  
  def mutate(self, info, input):
    grocery_item_original = get_db_entry_from_gql_input(GroceryItem, input)
    grocery_item_modified = modify_db_entry_with_new_input(grocery_item_original, input)
    return ModifyGroceryItem(grocery_item = grocery_item_modified)