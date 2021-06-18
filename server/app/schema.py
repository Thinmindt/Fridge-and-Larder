from app.models import GroceryItem
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphql_relay.node.node import from_global_id
from app.models import GroceryItem
from app import db

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
    db.session.add(grocery_item)
    db.session.commit()
    return CreateGroceryItem(grocery_item=grocery_item)

class Query(graphene.ObjectType):
  node = graphene.relay.Node.Field()
  all_grocery_items = SQLAlchemyConnectionField(GroceryItemObject)

class Mutation(graphene.ObjectType):
  create_grocery_item = CreateGroceryItem.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)