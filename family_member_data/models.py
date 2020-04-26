from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=None, blank=True, null=True)
    email = models.CharField(max_length=30)
    requests = models.CharField(max_length=500, blank=True, null=True)
    assignee = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


