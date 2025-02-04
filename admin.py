from django.contrib import admin
from .models import Entertainment, ImportDates, Events, QueryResults, QueryEventRelations


# @admin.register(Entertainment)
# class EntertainmentAdmin(admin.ModelAdmin):
#     list_display = ['title', 'location', 'start_date', 'end_date']
#     search_fields = ['title', 'location']
#     list_filter = ['start_date', 'end_date']

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['activity_name', 'organizer',
                    'start_date', 'end_date', 'location']
    search_fields = ['activity_name', 'description', 'organizer', 'location']
    list_filter = ['start_date', 'end_date']
    date_hierarchy = 'start_date'


@admin.register(ImportDates)
class ImportDatesAdmin(admin.ModelAdmin):
    list_display = ['import_date', 'timezone']
    list_filter = ['timezone']


@admin.register(QueryResults)
class QueryResultsAdmin(admin.ModelAdmin):
    list_display = ['query_timestamp', 'total_count', 'created_at']
    list_filter = ['created_at']


@admin.register(QueryEventRelations)
class QueryEventRelationsAdmin(admin.ModelAdmin):
    list_display = ['query_id', 'event_id', 'display_order']
    list_filter = ['query_id']
