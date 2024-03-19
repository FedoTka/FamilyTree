from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nickname, name=None, second_name=None, password=None):

        if not email:
            raise ValueError('Users must have an email adress')

        if not nickname:
            raise ValueError('Users must have a nickname')

        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            name=name,
            second_name=second_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, nickname, name=None, second_name=None, password=None):

        user = self.create_user(email, nickname, name, second_name, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user