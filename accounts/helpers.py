from .models import *
from django.contrib.auth.models import User

def check_duplicate_email (data):
    input_email = data['email']

    user_obj = User.objects.all()
    available_emails = [] 
    for i in user_obj:
        available_emails.append(i.email)
    
    if input_email in available_emails or input_email == "":
        return False
    else :
        return True