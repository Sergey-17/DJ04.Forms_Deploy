# Generated manually for renaming Review to Film

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Film',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_description',
            new_name='description',
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['-created_at'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
    ]
