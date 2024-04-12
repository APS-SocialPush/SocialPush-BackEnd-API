from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..serializers.post_metrics_serializer import PostMetricsSerializer
from ...models.post_metrics import PostMetrics


class PostMetricsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PostMetrics.objects.all()
    serializer_class = PostMetricsSerializer