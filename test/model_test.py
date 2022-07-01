import pytest

from werkzeug.security import generate_password_hash

from project.models import User, Role


@pytest.fixture
def create_regular_user():
    regular_user = User(email = "regular@gmail.com", name = "I am a regular user", 
            password = generate_password_hash('regular', method='sha256'))
    
    regular_user.roles.append(Role(name = "regular"))

    return regular_user


@pytest.fixture
def create_special_user():
    special_user = User(email = "special@gmail.com", name = "I am a special user", 
            password = generate_password_hash('special', method='sha256'))
    
    special_user.roles.append(Role(name = "special"))

    return special_user

def test_create_regular_user(create_regular_user):

    assert create_regular_user.name == "I am a regular user"
    assert create_regular_user.email == "regular@gmail.com"
    assert create_regular_user.has_roles("regular") == True


def test_create_special_user(create_special_user):

    assert create_special_user.name == "I am a special user"
    assert create_special_user.email == "special@gmail.com"
    assert create_special_user.has_roles("special") == True