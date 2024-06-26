# Generated by Django 5.0.3 on 2024-04-25 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Texto da Postagem')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/images', verbose_name='Imagem da Postagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora da Criação')),
                ('scheduled_date_time', models.DateTimeField(verbose_name='Data e Hora do Agendamento')),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagem',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120, unique=True, verbose_name='Nome de Usuário')),
                ('platform', models.CharField(choices=[('Tt', 'Twitter'), ('Meta', 'Facebook'), ('Insta', 'Instagram'), ('-', '-')], default='Twitter', max_length=50, verbose_name='Plataforma')),
                ('access_token', models.CharField(max_length=255, verbose_name='Token de acesso')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name': 'Midia Social',
                'verbose_name_plural': 'Mídias Sociais',
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(verbose_name='Número de Curtidas')),
                ('shares', models.IntegerField(verbose_name='Número de Compartilhamente')),
                ('comments', models.IntegerField(verbose_name='Número de Comentários')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora de Criação')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='socialmedia.post', verbose_name='Postagem')),
            ],
            options={
                'verbose_name': 'Métrica',
                'verbose_name_plural': 'Métricas',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='social_media_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='socialmedia.socialmediaaccount', verbose_name='Conta de Rede Social'),
        ),
    ]
