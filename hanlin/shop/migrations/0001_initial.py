# Generated by Django 2.1 on 2018-08-29 01:44

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
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchName', models.CharField(max_length=128, unique=True)),
                ('url', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantName', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128, unique=True)),
                ('price', models.IntegerField()),
                ('inventory', models.IntegerField()),
                ('pubDateTime', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=128)),
                ('hot', models.BooleanField()),
                ('discount', models.IntegerField()),
                ('newPrice', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Branch')),
                ('buyes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pubDateTime'],
            },
        ),
    ]