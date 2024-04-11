from ..models import User
from django.test import TestCase



class UserCRUDTestCase(TestCase):
    fixtures = ['users.json']
    def test_get(self):
        test_user = User.objects.get(email='vlad@mail.ru')

        # print(test_user)
        email = 'vlad@mail.ru'
        nickname = 'vudef'
        user, created = User.objects.get_or_create_user(email, nickname=nickname)
        self.assertEqual((user, created), (test_user, False))

    def test_create(self):
        email = 'cheburek@mail.ru'
        nickname = 'cheb'
        test_user, created = User.objects.get_or_create_user(email=email, nickname=nickname)

        self.assertEqual(created, True)