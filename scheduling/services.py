from .tasks import publicar_postagem_agendada
from .models import ScheduledPost


def agendar_postagem(post, social_media_account, scheduled_date_time):
    scheduled_post = ScheduledPost.objects.create(post=post, social_media_account=social_media_account, scheduled_date_time=scheduled_date_time)
    # publicar_postagem_agendada(scheduled_post.id)
    publicar_postagem_agendada.apply_async(args=[scheduled_post.id], eta=scheduled_date_time)

