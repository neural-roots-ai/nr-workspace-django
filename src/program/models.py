from django.db import models

class ProgramCategory(models.Model):
    program_category_id = models.AutoField(primary_key=True)
    program_category = models.CharField(max_length=50, blank=True, null=True)
    program_category_sequence = models.IntegerField()
    is_active = models.BooleanField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.program_category

    class Meta:
        db_table = 'program_category'
        verbose_name = "program category"
        verbose_name_plural = "program categories"
        ordering = ["is_active", "-program_category_sequence", ]


class ProgramType(models.Model):
    program_type_id = models.AutoField(primary_key=True)
    program_type_sequence = models.IntegerField()
    program_type = models.CharField(max_length=50)
    is_active = models.BooleanField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.program_type

    class Meta:
        db_table = 'program_type'


class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100)
    program_sequence = models.IntegerField()
    tag = models.CharField(max_length=150)
    program_img = models.CharField(max_length=100, blank=True, null=True)
    program_category = models.ForeignKey(ProgramCategory, on_delete=models.CASCADE, db_column='program_category_id')
    program_type = models.ForeignKey(ProgramType, on_delete=models.CASCADE, db_column='program_type_id')
    program_duration = models.CharField(max_length=2)
    program_start_date = models.DateTimeField()
    is_active = models.BooleanField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.program_name

    class Meta:
        db_table = 'program'
        ordering = ("program_category", "program_type", "program_sequence")


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.country
    
    class Meta:
        db_table = 'country'
        verbose_name = "country"
        verbose_name_plural = "Countries"

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_sequence = models.IntegerField()
    review_type = models.CharField(max_length=20)
    reviewer_name = models.CharField(max_length=50)
    review_desc = models.CharField(max_length=500, blank=True, null=True)
    program_type = models.IntegerField()
    is_active = models.BooleanField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.reviewer_name
    class Meta:
        db_table = 'review'


class Faq(models.Model):
    faq_id = models.AutoField(primary_key=True)
    faq_sequence = models.IntegerField()
    faq_type = models.CharField(max_length=50)
    faq_question = models.CharField(max_length=100)
    faq_answer = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField()
    updated_on = models.DateTimeField()
    created_on = models.DateTimeField()

    def __str__(self):
        return self.faq_question
    
    class Meta:
        db_table = 'faq'

class ProgramFee(models.Model):
    program_fee_id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey('Program', on_delete=models.CASCADE, db_column='program_id')
    program_fee = models.CharField(max_length=100)
    payment_link = models.CharField(max_length=100)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE, db_column='country_id')
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    discount = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.program_id.program_name

    class Meta:
        db_table = 'program_fee'

class Curriculum(models.Model):
    curriculum_id = models.AutoField(primary_key=True)
    module_id = models.IntegerField()
    program_id = models.ForeignKey('Program', on_delete=models.CASCADE, db_column='program_id')
    curriculum_title = models.CharField(max_length=50)
    topics = models.CharField(max_length=500, blank=True, null=True)
    module_duration = models.IntegerField()
    is_active = models.BooleanField()
    updated_on = models.DateTimeField()
    created_on = models.DateTimeField()

    def __str__(self):
        return self.program_id.program_name
    class Meta:
        db_table = 'curriculum'

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    curriculum = models.ForeignKey('Curriculum', on_delete=models.CASCADE, db_column='curriculum_id')
    module_id = models.IntegerField()
    topic = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return str(self.curriculum.curriculum_title)

    class Meta:
        db_table = 'topic'
