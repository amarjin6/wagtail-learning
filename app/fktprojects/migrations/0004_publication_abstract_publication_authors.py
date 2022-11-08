# Generated by Django 4.1.3 on 2022-11-07 10:51

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fktprojects', '0003_remove_publication_abstract_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='abstract',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publication_abstract', to='fktprojects.abstract'),
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='publication_authors', to=settings.AUTH_USER_MODEL),
        ),
    ]
