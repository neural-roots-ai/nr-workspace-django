from django.db import models


class CandidateInfo(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    work_experience = models.CharField(max_length=5, blank=True, null=True)
    email_address = models.EmailField(max_length=250, unique=True)
    candidate_phone = models.CharField(max_length=15, blank=True, null=True)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    candidate_country = models.CharField(max_length=20, blank=True, null=True)
    qualification = models.CharField(max_length=20, blank=True, null=True)
    program_type_id = models.IntegerField(blank=True, null=True)
    program_category_id = models.IntegerField(blank=True, null=True)
    enroll_rource = models.CharField(max_length=20, blank=True, null=True)
    is_enrolled = models.BooleanField(blank=True, null=True)
    enroll_type = models.CharField(max_length=20, blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    is_email_sent_level_0 = models.BooleanField(blank=True, null=True)
    email_level_0_id = models.IntegerField(blank=True, null=True)
    is_email_sent_level_1 = models.BooleanField(blank=True, null=True)
    email_level_1_id = models.IntegerField(blank=True, null=True)
    is_email_sent_level_2 = models.BooleanField(blank=True, null=True)
    email_level_2_id = models.IntegerField(blank=True, null=True)
    is_email_sent_level_3 = models.BooleanField(blank=True, null=True)
    email_level_3_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'candidate_info'
        verbose_name = "candidate info"
        verbose_name_plural = "candidate info"
        ordering = ["-updated_on", "-created_on", ]
        managed = False

class EmailContent(models.Model):
    email_content_id = models.AutoField(primary_key=True)
    email_level = models.IntegerField()
    email_from = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    program_category_id = models.IntegerField(blank=True, null=True)
    program_type_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        db_table = 'email_content'

class JobExecution(models.Model):
    job_execution_id = models.BigAutoField(primary_key=True)
    job_id = models.IntegerField()
    job_start_time = models.DateTimeField()
    job_end_time = models.TimeField(blank=True, null=True)
    job_name = models.CharField(max_length=255)  # Assuming no specific max length was provided
    job_error_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'job_execution'

class JobScheduler(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=20)
    job_description = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        db_table = 'job_scheduler'

