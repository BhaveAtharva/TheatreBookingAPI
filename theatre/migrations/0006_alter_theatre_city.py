# Generated by Django 3.2.5 on 2021-07-03 22:25

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_auto_20210703_2052'),
        ('theatre', '0005_alter_theatre_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theatre',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='region', chained_model_field='region', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.city', verbose_name='state/region'),
        ),
    ]
