from flask import Flask, Blueprint

user = Blueprint('user', __name__, template_folder='templates', static_folder='static')
from . import views