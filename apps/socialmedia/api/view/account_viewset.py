from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..serializers.account_serializer import SocialMediaAccountSerializer
from ...models.account import SocialMediaAccount


class SocialMediaAccountViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SocialMediaAccount.objects.all()
    serializer_class = SocialMediaAccountSerializer
