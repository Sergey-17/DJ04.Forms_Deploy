from django.contrib import admin
from .models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_short_description', 'get_short_review', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'description', 'review_text']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Информация о фильме', {
            'fields': ('title', 'description')
        }),
        ('Отзыв', {
            'fields': ('review_text',)
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_short_description(self, obj):
        return obj.get_short_description()
    get_short_description.short_description = 'Описание фильма'
    
    def get_short_review(self, obj):
        return obj.get_short_review()
    get_short_review.short_description = 'Отзыв'