# Generated manually for adding review_text field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_rename_review_to_film'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='review_text',
            field=models.TextField(verbose_name='Отзыв', default=''),
            preserve_default=False,
        ),
    ]
