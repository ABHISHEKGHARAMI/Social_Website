# email based user auth technique
from account.models import Profile
from django.contrib.auth.models import User


class EmailAuthBackend:
    
    def authenticate(self,request,username=None,password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
        
    
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        

def create_profile(backend, user, *args, **kwargs):
    Profile.objects.get_or_create(user=user)
