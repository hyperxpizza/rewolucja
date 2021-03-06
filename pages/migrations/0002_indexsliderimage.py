# Generated by Django 2.2.1 on 2019-12-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexSliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='aboutslider/%Y/%m/%d')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Index Slider Image',
                'verbose_name_plural': 'Index Slider Images',
                'ordering': ('name',),
            },
        ),
    ]
