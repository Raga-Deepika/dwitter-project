# Generated by Django 2.0.5 on 2018-06-04 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_chat_comment_follower_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='Msg_receive',
            new_name='Msg_receiver',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='Msg_sent',
            new_name='Msg_sender',
        ),
    ]