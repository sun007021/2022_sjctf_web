# Generated by Django 4.0.5 on 2022-07-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_commonboard_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privateboard1',
            name='content',
            field=models.CharField(max_length=128, verbose_name='제목'),
        ),
    ]
