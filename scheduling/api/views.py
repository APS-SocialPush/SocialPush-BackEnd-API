from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, status

from ..api.serializers import ScheduledPostSerializer
from ..models import ScheduledPost
from ..services import agendar_postagem


class ScheduledPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)

            scheduled_post = ScheduledPost.objects.create(**serializer.validated_data)
            agendar_postagem(scheduled_post.post, scheduled_post.social_media_account, scheduled_post.scheduled_date_time)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

