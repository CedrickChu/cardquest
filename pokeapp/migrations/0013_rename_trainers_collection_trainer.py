# Generated by Django 4.2.7 on 2023-12-05 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0012_remove_collection_card_remove_collection_trainer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='trainers',
            new_name='trainer',
        ),
    ]
