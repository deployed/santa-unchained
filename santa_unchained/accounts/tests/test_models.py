from django.contrib.auth.models import AbstractUser

from santa_unchained.accounts.models import CustomUser


class TestCustomUser:
    def test_custom_user_inherits_from_abstract(self):
        assert issubclass(CustomUser, AbstractUser)
