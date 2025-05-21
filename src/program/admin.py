from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy
from import_export.admin import ImportExportActionModelAdmin
from djangoql.admin import DjangoQLSearchMixin
from . import models

# https://testdriven.io/blog/customize-django-admin/
# https://realpython.com/customize-django-admin-python/


@admin.register(models.Program)
class ProgramAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
            "program_name",
            "program_type",
            "program_category",
            "program_duration",
            "program_start_date",
            "is_active"
        ]
    list_filter = ("program_category", "program_type", "program_type")

@admin.register(models.ProgramFee)
class ProgramFeeAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
            "program_id",
            "program_fee",
            "country_id",
            "discount",
            "is_active"
        ]
    list_filter = ("country_id", "program_id")

@admin.register(models.Review)
class ReviewAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
            "review_sequence",
            "reviewer_name",
            "review_type",
            "review_desc",
            "program_type",
            "is_active"
        ]
    list_filter = ("review_type", "program_type")

@admin.register(models.Curriculum)
class CurriculumAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
            "module_id",
            "curriculum_title",
            "module_duration",
            "program_id",
            "topics",
            "is_active"
        ]
    list_filter = ("program_id", )

@admin.register(models.Topic)
class TopicAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
            "topic_id",
            "module_id",
            "curriculum",
            "topic",
            "is_active"
        ]
    list_filter = ("curriculum", )

@admin.register(models.Faq)
class FaqAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
            "faq_sequence",
            "faq_type",
            "faq_question",
            "faq_answer",
            "is_active"
        ]
    list_filter = ("faq_type", )

@admin.register(models.Country)
class CountryAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
            "country_id",
            "country",
            "created_on",
            "is_active"
        ]

@admin.register(models.ProgramCategory)
class ProgramCategoryAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
            "program_category_id",
            "program_category_sequence",
            "program_category",
            "is_active"
        ]

@admin.register(models.ProgramType)
class ProgramTypeAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
            'program_type_id',
            "program_type_sequence",
            "program_type",
            "is_active"
        ]

