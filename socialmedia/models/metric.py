from django.db import models
from .post import Post


class Metric(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='metrics',
        verbose_name="Postagem",
    )

    likes = models.IntegerField(
        verbose_name="Número de Curtidas",
    )

    shares = models.IntegerField(
        verbose_name="Número de Compartilhamente",
    )

    comments = models.IntegerField(
        verbose_name="Número de Comentários",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data e Hora de Criação",
    )

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        verbose_name = "Métrica"
        verbose_name_plural = "Métricas"

    def __str__(self):
        """Retorna a representação do objeto como string."""

        return f'Métricas da postagem {self.post}'
