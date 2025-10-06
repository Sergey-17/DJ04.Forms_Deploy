# Generated manually for renaming review_text field

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_rename_review_to_film'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='review_text',
            new_name='review_text',
        ),
    ]
