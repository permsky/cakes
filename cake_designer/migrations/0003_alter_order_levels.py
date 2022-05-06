# Generated by Django 4.0.4 on 2022-05-06 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake_designer', '0002_insert_default_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='levels',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='cake_designer.level', verbose_name='Количество уровней'),
        ),
    ]
