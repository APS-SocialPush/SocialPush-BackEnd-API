from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..serializers.scheduled_post_serializer import ScheduledPostSerializer
from ...models.scheduled_post import ScheduledPost


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer