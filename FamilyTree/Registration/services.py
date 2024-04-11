from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import Q

class CustomUserManager(BaseUserManager):

    def get_or_create_user(self, email, **kwargs):
        try:
            user = self.get(email=email)
            created = False
        except self.model.DoesNotExist:
            user = self.create_user(email=email, **kwargs)
            created = True

        return user, created

    def create_user(self, email, nickname=None, password=None, **kwargs):

        if not email:
            raise ValueError('Users must have an email address')

        if nickname is None:
            nickname = email

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            **kwargs
        )
        if password is not None:
            user.set_password(make_password(password))

        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, name=None, second_name=None, password=None):
        user = self.create_user(email, nickname, name, second_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user