from django.contrib import admin
from .models import Post, FAQ, Useful, Contact


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'search_s',
        'search_count',
        'create_date',
        'update_at',
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'writer',
        'create_date',
    )


@admin.register(Useful)
class UsefulAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'writer',
        'create_date',
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'tel',
        'writer',
        'create_date',
    )
