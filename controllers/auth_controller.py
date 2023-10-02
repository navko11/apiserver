from flask import Blueprint, jsonify, request
from main import db
from models.cards import Card

cards = Blueprint('cards', __name__, url_prefix="/cards")