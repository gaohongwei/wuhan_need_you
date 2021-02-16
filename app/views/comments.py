# coding: utf-8

from flask import Blueprint
from app.models import Comment

app = Blueprint('comments', __name__)

@app.route('/post_comment', methods=['POST'])
def post_comment():
    Comment.add()
    return 'success', 200
