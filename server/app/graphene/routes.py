from app.graphene import bp
from app.schema import schema
from graphene_file_upload.flask import FileUploadGraphQLView

@bp.route('/')
@bp.route('/index')
def index():
  return "Hello world"

# Create GraphQL interface
bp.add_url_rule(
  '/graphql',
  view_func=FileUploadGraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True # for GraphiQL interface
  )
)