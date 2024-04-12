from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..serializers.socialmedia_metric_serializer import SocialMediaMetricsSerializer
from ...models.socialmedia_metrics import SocialMediaMetrics


class SocialMediaMetricsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SocialMediaMetrics.objects.all()
    serializer_class = SocialMediaMetricsSerializer
