# Generated by Django 2.0.6 on 2018-06-04 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20180604_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='follow_no',
            new_name='fol_no',
        ),
    ]
