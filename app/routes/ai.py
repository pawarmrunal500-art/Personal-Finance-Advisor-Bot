from flask import Blueprint

bp = Blueprint('ai', __name__)

@bp.route('/chat')
def chat():
    return "AI Chat"

@bp.route('/advice')
def advice():
    return "AI Advice"
