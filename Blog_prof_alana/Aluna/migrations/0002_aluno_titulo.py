# Generated by Django 5.1 on 2024-08-31 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aluna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='titulo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]