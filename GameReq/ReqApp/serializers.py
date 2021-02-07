# serializers.py
from rest_framework import serializers
from .models import Requirements

class RequirementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requirements
        fields = ['img', 'name', 'CPU', 'RAM', 'GPU', 'HDD', 'OS']