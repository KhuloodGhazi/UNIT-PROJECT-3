# Generated by Django 5.1.3 on 2024-12-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_volunteerprofile_applied_opportunities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationprofile',
            name='industry_focus_area',
            field=models.CharField(blank=True, choices=[('Medical', 'Medical'), ('Entertainment', 'Entertainment'), ('Education', 'Education'), ('Environment', 'Environment'), ('Technology', 'Technology')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organizationprofile',
            name='organization_type',
            field=models.CharField(blank=True, choices=[('Non-Profit', 'Non-Profit'), ('Corporate', 'Corporate'), ('Government', 'Government'), ('Startup', 'Startup')], max_length=100, null=True),
        ),
    ]
