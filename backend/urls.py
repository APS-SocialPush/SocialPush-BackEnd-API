"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

# Redirect Test
from users.api.viewsets.redirect import RedirectSocial

# Users
from users.api.viewsets.user_custom_viewset import CustomUserViewSet

# SocialMedia
from socialmedia.api.viewsets.account_viewset import SocialMediaAccountViewSet
from socialmedia.api.viewsets.metric_viewset import MetricViewSet
from socialmedia.api.viewsets.post_viewset import PostViewSet

# Scheduling
from scheduling.api.views import ScheduledPostViewSet

router = routers.DefaultRouter()

# Users
router.register(
    r"users",
    CustomUserViewSet,
    basename="users",
)

# SocialMedia
router.register(
    r"accounts",
    SocialMediaAccountViewSet,
    basename="accounts",
)

router.register(
    r"posts",
    PostViewSet,
    basename="posts",
)

router.register(
    r"metrics",
    MetricViewSet,
    basename="metrics",
)

router.register(
    r"scheduling",
    ScheduledPostViewSet,
    basename="scheduling",
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # JWT Routes
    path("api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair",),
    # path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh",),

    path('api/accounts/users/', RedirectSocial.as_view()),

    # DJOSER Routes
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("api/auth/social/", include("djoser.social.urls")),

    # SWAGGER Routes
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

