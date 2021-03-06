# Generated by Django 2.0.5 on 2018-06-04 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_dweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Msg_sent', models.TextField()),
                ('Msg_receive', models.TextField()),
                ('time', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Content', models.TextField()),
                ('time', models.DateTimeField()),
                ('Com_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_of_followers', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('Fol_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_likes', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('Lik_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Profile')),
            ],
        ),
    ]
