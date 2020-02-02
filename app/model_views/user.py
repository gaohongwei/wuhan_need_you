
from flask_admin.contrib import sqla
import flask_login as login
from app.models import User
from app.db import db
from werkzeug.security import generate_password_hash

class UserModelView(sqla.ModelView):
    column_exclude_list = ['password']
    def is_accessible(self):
        return login.current_user.is_authenticated

# init flask-login
def init_login(app):
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
    return login_manager

def _init_sample_users():
    import string
    import random

    db.drop_all()
    db.create_all()
    # passwords are hashed, to use plaintext passwords instead:
    # test_user = User(login="test", password="test")
    test_user = User(login="test", role="admin", password=generate_password_hash("test"))
    db.session.add(test_user)

    first_names = [
        'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie','Sophie', 'Mia',
        'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
        'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
    ]
    last_names = [
        'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
        'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
        'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
    ]

    for i in range(len(first_names)):
        user = User()
        user.first_name = first_names[i]
        user.last_name = last_names[i]
        user.login = user.first_name.lower()
        user.email = user.login + "@example.com"
        user.role = 'admin'
        user.password = generate_password_hash(''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10)))
        db.session.add(user)

    db.session.commit()

def init_sample_users(app):
    with app.app_context():
        _init_sample_users()

