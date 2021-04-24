# Generated by Django 3.2 on 2021-04-24 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_theater_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='seats',
            name='shows',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.shows'),
        ),
    ]
