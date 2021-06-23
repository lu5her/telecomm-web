# Generated by Django 3.2.4 on 2021-06-22 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('สั่งการ', 'สั่งการ'), ('ประชาสัมพันธ์', 'ประชาสัมพันธ์')], default='สั่งการ', max_length=50)),
                ('date_published', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('detail', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('read', models.ManyToManyField(related_name='read_newss', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]