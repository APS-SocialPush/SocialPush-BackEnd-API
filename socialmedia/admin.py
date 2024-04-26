from django.contrib import admin

from .models.account import SocialMediaAccount
from .models.metric import Metric
from .models.post import Post


admin.site.register(SocialMediaAccount)
admin.site.register(Metric)
admin.site.register(Post)