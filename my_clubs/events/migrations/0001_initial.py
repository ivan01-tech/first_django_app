# Generated by Django 4.2.3 on 2023-07-14 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyClubsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email_address', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('zip_code', models.CharField(max_length=120, verbose_name='Zip Code')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Venue Email')),
                ('address', models.CharField(max_length=300)),
                ('web', models.URLField(verbose_name='Web site')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('manager', models.CharField(blank=True, max_length=56, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('attendees', models.ManyToManyField(blank=True, to='events.myclubsuser')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
    ]
