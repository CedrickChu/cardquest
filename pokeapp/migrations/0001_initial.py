from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        # Add your dependencies here if any
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rarity', models.CharField(max_length=50)),
                ('hp', models.PositiveIntegerField()),
                ('card_type', models.CharField(max_length=50)),
                ('attack', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('weakness', models.CharField(max_length=50)),
                ('card_number', models.PositiveIntegerField()),
                ('release_date', models.DateField(null=True, blank=True)),
                ('evolution_stage', models.CharField(max_length=50, null=True, blank=True)),
                ('abilities', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField()),
            ],
        ),
    ]
