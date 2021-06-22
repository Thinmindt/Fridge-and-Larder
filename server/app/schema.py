import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphql_relay.node.node import from_global_id
from app.grocery_item_schema import GroceryItemObject, CreateGroceryItem, DeleteGroceryItem

class Query(graphene.ObjectType):
  node = graphene.relay.Node.Field()
  all_grocery_items = SQLAlchemyConnectionField(GroceryItemObject)
  grocery_item = graphene.relay.Node.Field(GroceryItemObject)

class Mutation(graphene.ObjectType):
  create_grocery_item = CreateGroceryItem.Field()
  delete_grocery_item = DeleteGroceryItem.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)