from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)
from datetime import date
from django.db import models


class User(BaseUserManager):
    def create_user(self, firstname, email, password, role):
        if not email:
            raise ValueError('Email déja utilisé')

        user = self.model(
            firstname=firstname,
            email=self.normalize_email(email),
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class RoleUser(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Users(AbstractBaseUser):
    firstname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=35)
    role = models.ForeignKey(RoleUser,related_name="right", on_delete=models.CASCADE)

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = []

    objects = User()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_employe(self):
        return self.employe


class Planning(models.Model):
    title = models.CharField(max_length=20)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    student = models.ForeignKey(Users, related_name="student", on_delete=models.CASCADE)
    instructor = models.ForeignKey(Users, related_name="instructor", on_delete=models.CASCADE)


class PlanningHours(models.Model):
    hour = models.CharField(max_length=20)


class PlanningUsers(models.Model):
    hour = models.ForeignKey(PlanningHours, on_delete=models.CASCADE)
    student = models.ForeignKey(Users, on_delete=models.CASCADE)

