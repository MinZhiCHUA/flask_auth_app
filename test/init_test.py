import pytest

from werkzeug.security import generate_password_hash
from flask_login import login_user

from project.models import User, Role
from project import my_current_user

@pytest.fixture
def create_regular_user():
    regular_user = User(id = 999, email = "regular@gmail.com", name = "I am a regular user", 
            password = generate_password_hash('regular', method='sha256'))
    
    regular_user.roles.append(Role(name = "regular"))

    return regular_user


@pytest.fixture
def create_special_user():
    special_user = User(id = 888, email = "special@gmail.com", name = "I am a special user", 
            password = generate_password_hash('special', method='sha256'))
    
    special_user.roles.append(Role(name = "special"))

    return special_user

# def test_my_current_user(create_special_user):
#     login_user(create_special_user, remember=True)

#     assert my_current_user.name == "I am a special user"
#     assert my_current_user.email == "special@gmail.com"
#     assert my_current_user.has_roles("special") == True