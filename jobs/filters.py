import django_filters
from .models import Job as JobModel

class JobsFilter(django_filters.FilterSet):
    modality=django_filters.CharFilter(field_name='modality')
    class Meta:
        model = JobModel
        fields = ['modality', 'is_flex', 'status', 'user', 'category', 'place']