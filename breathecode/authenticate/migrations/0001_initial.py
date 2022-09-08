# Generated by Django 3.2.15 on 2022-09-08 06:25

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProxy',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user', ),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CredentialsGithub',
            fields=[
                ('github_id', models.IntegerField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('avatar_url', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('username', models.CharField(blank=True, max_length=35, null=True)),
                ('blog', models.CharField(blank=True, max_length=150, null=True)),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_username', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user',
                 models.OneToOneField(blank=True,
                                      on_delete=django.db.models.deletion.CASCADE,
                                      to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id',
                 models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('key', models.CharField(db_index=True, max_length=40, unique=True)),
                ('token_type', models.CharField(default='temporal', max_length=64)),
                ('expires_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='auth_token',
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='User')),
            ],
            options={
                'unique_together': {('user', 'key')},
            },
        ),
    ]
