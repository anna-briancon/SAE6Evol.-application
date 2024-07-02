# Generated by Django 5.0.6 on 2024-07-02 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_rename_song_title_quizquestion_title'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistePage',
            fields=[
                ('page_ptr', models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE, 
                    parent_link=True,
                    primary_key=True,
                    serialize=False,
                    to='wagtailcore.page',
                )),
                ('api_url', models.URLField(blank=True)),
                ('page_title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='artistepage',
            name='page_ptr',  # Correct the field name here
        ),
        migrations.RemoveField(
            model_name='artistepage',
            name='api_url',  # Adjust as needed based on your model definition
        ),
        migrations.DeleteModel(
            name='QuizQuestion',
        ),
        migrations.DeleteModel(
            name='ArtistPage',
        ),
    ]
