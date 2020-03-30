# Generated by Django 2.1.2 on 2020-03-29 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meet2', '0004_auto_20200329_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPostLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IsTrue', models.BooleanField(default=False)),
                ('PostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meet2.Post')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
