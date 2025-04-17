from .models import QueryLog
from rest_framework import serializers


class QueryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=QueryLog
        fields=['id','query','tone','intent','actions','timestamp']
