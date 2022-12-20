from rest_framework import serializers
from .models import postDetails

class postDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = postDetails
        fields = '__all__'