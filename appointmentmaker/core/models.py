from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Appointee(models.Model):
    user = models.OneToOneField(User, related_name='appointee', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Company(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Appointment(models.Model):
    company = models.ForeignKey(Company, related_name='appointments', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='appointments')
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    internal_notes = models.TextField(null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return "{}'s appointment".format(self.creator)

    @property
    def is_past(self):
        if self.end:
            return datetime.now() > self.end

        return datetime.now() > self.start
