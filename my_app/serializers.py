from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Employee
        fields = '__all__'

class VacationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Vacation
        fields = '__all__'

