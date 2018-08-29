# Generated by Django 2.1 on 2018-08-29 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('totalPrice', models.IntegerField()),
                ('payMethod', models.CharField(max_length=128)),
                ('pubDateTime', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Plant')),
            ],
            options={
                'ordering': ['-pubDateTime'],
            },
        ),
    ]