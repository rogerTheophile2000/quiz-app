# Generated by Django 4.0.10 on 2023-06-13 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=200, null=True)),
                ('option_two', models.CharField(max_length=200, null=True)),
                ('option_three', models.CharField(max_length=200, null=True)),
                ('option_four', models.CharField(max_length=200, null=True)),
                ('option_five', models.CharField(max_length=200, null=True)),
                ('answer', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
