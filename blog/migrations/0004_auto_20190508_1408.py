# Generated by Django 2.2.1 on 2019-05-08 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190508_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
    ]