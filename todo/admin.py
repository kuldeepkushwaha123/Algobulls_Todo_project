from django.contrib import admin
from .models import Task, Tag

admin.site.register(Tag)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)  # Prevent editing the timestamp field
    list_display = ('title', 'status', 'due_date')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Task Details', {
            'fields': ('timestamp', 'title', 'description')
        }),
        ('Additional Information', {
            'fields': ('due_date', 'tags', 'status')
        }),
    )

