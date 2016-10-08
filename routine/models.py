from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length = 250)
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    department = models.ForeignKey(Department,on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    complete = models.BooleanField()
    date = models.DateTimeField()

    def __str__(self):
        return "%r - %r"%(self.complete, self.date)





















































