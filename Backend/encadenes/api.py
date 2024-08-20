from rest_framework import viewsets, permissions, response, status
from rest_framework.decorators import action
from .models import Route
from .serializer import RouteSerializer

class RouteViewSet(viewsets.ModelViewSet):
  queryset = Route.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = RouteSerializer

  """ @action(detail= True, methods=['post'])
  def recommended(self, request, pk=None):
    route = self.get_object()
    route.recommended_by = request.data
    route.save()
    return response.Response({
      'status': 'Recommendation added'
    }, status) """