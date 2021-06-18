import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphql_relay.node.node import from_global_id


class Query(graphene.ObjectType):
  node = graphene.relay.Node.Field()

# class Mutation(graphene.ObjectType):
#   pass

schema = graphene.Schema(query=Query)