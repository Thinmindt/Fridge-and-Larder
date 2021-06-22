from flask import Blueprint

bp = Blueprint('graphene', __name__)

from app.graphene import routes