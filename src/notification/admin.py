from import_export.admin import ImportExportActionModelAdmin
from djangoql.admin import DjangoQLSearchMixin
from django.contrib import admin
from . import models


@admin.register(models.CandidateInfo)
class CandidateInfoAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email_address",
        "candidate_phone",
        "candidate_country",
        "enroll_rource",
        "is_enrolled",
        "is_email_sent_level_0",
        "is_email_sent_level_1",
        "is_email_sent_level_2",
        "is_email_sent_level_3",
        "created_on",
        "updated_on",
        "is_active"
    ]
    list_filter = ("is_enrolled", "candidate_country", "enroll_rource", "program_category_id")


@admin.register(models.EmailContent)
class EmailContentAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
        "subject",
        "email_from",
        "email_level",
        "is_active",
        "program_category_id"
    ]
    list_filter = ("email_level", "program_category_id")

