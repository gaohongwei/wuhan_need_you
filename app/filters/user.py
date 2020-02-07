
from app.models import User
from flask_admin.model.template import EditRowAction, DeleteRowAction, ViewRowAction
import flask_login as login

def register_user_filters(app):
    pass


def is_user_row_action_allowed(action, user):
    cur_user = login.current_user
    if isinstance(action, EditRowAction):
        return cur_user.role < user.role or cur_user.id == user.id
    elif isinstance(action, DeleteRowAction):
        return cur_user.role < user.role
    elif isinstance(action, ViewRowAction):
        return cur_user.role <= user.role
    return True

def register_user_processors(app):
    @app.context_processor
    def inject_user_processors():
        return {
                'is_user_row_action_allowed': is_user_row_action_allowed
                }
        return True

