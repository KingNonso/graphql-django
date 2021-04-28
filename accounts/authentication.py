from django.contrib.auth import get_user_model
User = get_user_model()


class EmailAuthBackend(object):
    '''
    Authenticate using an e-mail address
    '''

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class PhoneAuthBackend(object):
    '''
    Authenticate using a phone number
    '''

    def authenticate(self, request, username=None, password=None):
        try:
            users = User.objects.filter(phone=username)
            if users.count() == 1 and users[0].phone and users[0].check_password(password):
                return users[0]
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
