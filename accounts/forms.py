from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreatedUserForm(UserCreationForm):
    """
    Management of form for registering user
    """
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')