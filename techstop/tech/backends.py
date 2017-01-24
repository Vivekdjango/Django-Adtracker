from django.contrib.auth.models import User


class SSOLoginBackend(object):
    """
    This is a transparent authentication backend for SSO login. Assumes that a user
    was authenticated using SSO prior to this class getting invoked.
    """
    def authenticate(self, username, password=None, email=None):
        user = None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Create a new user. Note that we can set password
            # to anything, because it won't be checked; the password
            # from settings.py will.
            if password is None:
                password = User.objects.make_random_password(length=25)
            user = User(username=username, password=password)
            user.is_staff = False
            user.is_superuser = False
            user.email = email
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

