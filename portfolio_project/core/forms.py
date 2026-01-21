from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# We inherit from Django's built-in form to create a user
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        # Password creation is included automatically by UserCreationForm
