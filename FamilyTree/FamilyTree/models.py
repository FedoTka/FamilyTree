from django.db import models
from django.contrib.auth.models import User



class FamilyTree(models.Model):
    pass


class Member(models.Model):
    tree = models.ForeignKey(FamilyTree, on_delete=models.CASCADE)

