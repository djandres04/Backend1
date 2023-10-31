from flask import Blueprint, request
from flask_cors import CORS
import requests

import json

from src.utils.token import token_required
from src.utils import JsonMessage

from decouple import config

main = Blueprint('temperature_blueprint', __name__)
CORS(main)