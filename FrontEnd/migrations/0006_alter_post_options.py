# Generated by Django 4.0.1 on 2022-09-25 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0005_alter_post_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date'], 'verbose_name': '貼文', 'verbose_name_plural': '貼文'},
        ),
    ]