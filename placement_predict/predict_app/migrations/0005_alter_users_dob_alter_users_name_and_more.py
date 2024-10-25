# Generated by Django 5.1 on 2024-09-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("predict_app", "0004_alter_users_dob_alter_users_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="DOB",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="Name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="certificates",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="degree",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="degree_p",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="degree_passoutYear",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="degree_t",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="etest_p",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="gender",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="hsc_b",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="hsc_p",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="hsc_y",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="mba_p",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="mobile",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="resume",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="users",
            name="salary",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="skills",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="specialisation",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="ssc_b",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="ssc_p",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="ssc_y",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="status",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="university",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="workex",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="workex_company",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]