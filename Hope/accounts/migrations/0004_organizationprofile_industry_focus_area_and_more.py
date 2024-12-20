# Generated by Django 5.1.3 on 2024-11-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_volunteerprofile_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationprofile',
            name='industry_focus_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='organizationprofile',
            name='organization_logo',
            field=models.ImageField(blank=True, null=True, upload_to='organization_logos/'),
        ),
        migrations.AddField(
            model_name='organizationprofile',
            name='organization_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='organizationprofile',
            name='website_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
