from django.db import models


class Meeting(models.Model):
    name = models.CharField(max_length=100)
    meet_date = models.DateTimeField()
