# Generated by Django 4.0.3 on 2022-04-09 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0003_auto_20220324_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='th',
            name='er',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='er', to='keys.er'),
        ),
    ]
