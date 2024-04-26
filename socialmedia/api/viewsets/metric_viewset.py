from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..serializers.metric_serializer import MetricSerializer
from ...models.metric import Metric


class MetricViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer