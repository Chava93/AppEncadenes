from rest_framework import serializers
from .models import Route

class RouteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Route
    fields = ('name', 'rating', 'total_ascents', 'recommended_by', 'sector', 'grado')