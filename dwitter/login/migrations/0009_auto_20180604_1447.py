# Generated by Django 2.0.6 on 2018-06-04 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20180604_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='fol_no',
            new_name='follower_no',
        ),
    ]
