from django.db import models
from users.models import User as UserModel

class Job(models.Model):
    STATUS_UNASSIGNED = 1
    STATUS_ASSIGNED = 2
    STATUS_COMPLETED = 3
    STATUS_CANCELLED = -1
    STATUS_CHOICES = [
        (STATUS_UNASSIGNED, 'unassigned'),
        (STATUS_ASSIGNED, 'assigned'),
        (STATUS_CANCELLED, 'cancelled'),
        (STATUS_COMPLETED, 'completed')
    ]
    class Meta:
        db_table = 'jobs'
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=200,
        null=True,
        unique=True,
        error_messages={'unique': u'Ya existe un trabajo con este título'}
    )
    description = models.TextField(null=True)
    modality = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=200, null=True)
    finalization_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    is_flex = models.BooleanField(null=True)
    budget = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modification_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_UNASSIGNED
    )
    category=models.CharField(max_length=100, null=True)

