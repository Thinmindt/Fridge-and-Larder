from app import create_app, db
from app.schema import schema
import os
from graphql.utils import schema_printer
from flask.cli import with_appcontext
import click

app = create_app()

@app.cli.command("generate_schema")
def generate_schema():
  schema_string = schema_printer.print_introspection_schema(schema)
  with open(os.path.join("..", "schema.graphql"), "w") as fp:
    fp.write(schema_string)

@app.shell_context_processor
def make_shell_context():
  return {'db': db}