from jobs.models import Job as JobModel
from rest_framework import serializers
from users.models import User
from users.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = JobModel
        fields = (
            'id',
            'title',
            'description',
            'modality',
            'place',
            'finalization_date',
            'is_flex',
            'budget',
            'created_at',
            'user',
            'category',
            'status'
        )
        read_only_fields = ('created_ad', 'last_modification_at')

class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = (
            'id',
            'user',
            'title',
            'description',
            'modality',
            'place',
            'finalization_date',
            'is_flex',
            'budget',
            'category'
        )
        read_only_fields = ('created_ad', 'last_modification_at')