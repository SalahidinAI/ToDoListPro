from django_filters import FilterSet
from .models import *


class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            'category': ['exact'],
            'completed': ['exact'],
            'due_date': ['gt', 'lt']
        }