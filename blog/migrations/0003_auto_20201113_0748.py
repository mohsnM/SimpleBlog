# Generated by Django 3.1.2 on 2020-11-13 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postsetting',
            old_name='allow_discusstion',
            new_name='allow_discussion',
        ),
    ]
