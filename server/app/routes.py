from app import app
from app.schema import schema
from graphene_file_upload.flask import FileUploadGraphQLView

@app.route('/')
@app.route('/index')
def index():
  return "Hello world"

# Create GraphQL interface
app.add_url_rule(
  '/graphql',
  view_func=FileUploadGraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True # for GraphiQL interface
  )
)