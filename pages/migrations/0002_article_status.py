# Generated by Django 3.2.14 on 2022-09-02 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.IntegerField(choices=[(0, 'Submitted'), (1, 'Published')], default=0),
        ),
    ]
