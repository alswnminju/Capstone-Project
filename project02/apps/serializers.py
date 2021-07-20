from rest_framework import serializers
from .models import Parkmoa

class ParkmoaSerializer(serializers.Serializer):
	District = serializers.CharField()
	Park_division = serializers.CharField()
	Park_name = serializers.CharField()

	class Meta:
            model = Parkmoa
            fields = ('District','Park_division','Park_name')

