from rest_framework import serializers
from .models import *

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

    def validate_file(self, file):
        if file.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("File too large")

        if not file.name.endswith(('.pdf','.jpg','.png')):
            raise serializers.ValidationError("Invalid file type")

        return file


class KYCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYCSubmission
        fields = '__all__'