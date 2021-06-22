from flask.cli import FlaskGroup

from app import create_app, db

cli = FlaskGroup(create_app=create_app)

@cli.command("create_db")
def create_db():
  """Register create_db command with the CLI tool to apply the model
  to the database.
  """
  db.drop_all()
  db.create_all()
  db.session.commit()

if __name__ == "__main__":
  cli()