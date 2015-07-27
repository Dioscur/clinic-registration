from django.db import models
from django.utils import timezone

class Doctors(models.Model):
    """Table of Doctors"""
    medic = models.CharField(max_length=100)

    def __str__(self):
        return self.medic

class Record(models.Model):
    """Table of record visits"""
    medic_name = models.CharField(max_length=100)
    # medic_name = models.ForeignKey('Doctors')
    visitor_first_name = models.CharField(max_length=50)
    visitor_last_name = models.CharField(max_length=50)
    record_date = models.DateField()
    record_time = models.TimeField()
    created_date = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey('auth.User')

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.medic_name