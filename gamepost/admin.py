from django.contrib import admin
from .models import GamePost

@admin.register(GamePost)
class GamePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_by', 'created_at')
    list_filter = ('created_at', 'created_by')
    search_fields = ('title', 'synopsis')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'created_by')

    def save_model(self, request, obj, form, change):
        """Auto-set the creator if creating a new post."""
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

