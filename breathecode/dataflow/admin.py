import os, ast
from django.contrib import admin
from django import forms
from django.utils import timezone
from .models import Pipeline, Transformation, Project, DataSource
from .actions import pull_project_from_github
from django.utils.html import format_html


def pull_github_project(modeladmin, request, queryset):
    projects = queryset.all()

    for p in projects:
        pull_project_from_github(p)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('slug', 'description', 'owner')
    # actions = [run_single_script]
    list_filter = ['slug']
    actions = [pull_github_project]


@admin.register(Pipeline)
class PipelineAdmin(admin.ModelAdmin):
    # form = CustomForm
    list_display = ('slug', 'current_status')
    # actions = [run_single_script]
    list_filter = ['status', 'project__title']

    # actions=[pull_github_project]

    def current_status(self, obj):
        colors = {
            'OPERATIONAL': 'bg-success',
            'CRITICAL': 'bg-error',
            'FATAL': 'bg-error',  # important: this status was deprecated and deleted!
            'MINOR': 'bg-warning',
        }
        now = timezone.now()
        if obj.paused_until is not None and obj.paused_until > now:
            return format_html(f"<span class='badge bc-warning'> ⏸ PAUSED</span>")

        return format_html(f"<span class='badge {colors[obj.status]}'>{obj.status}</span>")
