from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import Deal, Store, Category, DealClick, Newsletter, ContactMessage


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_preview', 'is_active', 'deal_count', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active']

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height:40px; border-radius:5px;" />', obj.logo.url)
        elif obj.logo_url:
            return format_html('<img src="{}" style="height:40px; border-radius:5px;" />', obj.logo_url)
        return '—'
    logo_preview.short_description = 'Logo'

    def deal_count(self, obj):
        count = obj.deals.filter(is_active=True).count()
        return format_html('<span style="background:#6366f1;color:white;padding:2px 8px;border-radius:10px;">{}</span>', count)
    deal_count.short_description = 'Active Deals'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'color_preview', 'is_active', 'deal_count']
    list_filter = ['is_active']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active']

    def color_preview(self, obj):
        return format_html(
            '<div style="width:25px;height:25px;background:{};border-radius:50%;display:inline-block;"></div> {}',
            obj.color, obj.color
        )
    color_preview.short_description = 'Color'

    def deal_count(self, obj):
        count = obj.deals.filter(is_active=True).count()
        return format_html('<span style="background:#10b981;color:white;padding:2px 8px;border-radius:10px;">{}</span>', count)
    deal_count.short_description = 'Active Deals'


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'store', 'category', 'old_price', 'new_price',
        'discount_badge', 'status_badge', 'is_featured', 'is_popular',
        'click_count', 'expiry_date'
    ]
    list_filter = ['is_active', 'is_featured', 'is_popular', 'store', 'category']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_featured', 'is_popular']
    date_hierarchy = 'created_at'
    readonly_fields = ['click_count', 'discount_percent', 'created_at', 'updated_at', 'image_preview']
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'description', 'category', 'store')
        }),
        ('Pricing', {
            'fields': ('old_price', 'new_price', 'discount_percent')
        }),
        ('Images', {
            'fields': ('image', 'image_preview', 'image_url')
        }),
        ('Links & Dates', {
            'fields': ('affiliate_link', 'expiry_date')
        }),
        ('Visibility', {
            'fields': ('is_active', 'is_featured', 'is_popular')
        }),
        ('Stats', {
            'fields': ('click_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def discount_badge(self, obj):
        color = '#ef4444' if obj.discount_percent >= 50 else '#f97316' if obj.discount_percent >= 30 else '#10b981'
        return format_html(
            '<span style="background:{};color:white;padding:2px 8px;border-radius:10px;font-weight:bold;">{}% OFF</span>',
            color, obj.discount_percent
        )
    discount_badge.short_description = 'Discount'

    def status_badge(self, obj):
        if not obj.is_active:
            return format_html('<span style="background:#6b7280;color:white;padding:2px 8px;border-radius:10px;">Inactive</span>')
        if obj.expiry_date < timezone.now().date():
            return format_html('<span style="background:#ef4444;color:white;padding:2px 8px;border-radius:10px;">Expired</span>')
        return format_html('<span style="background:#10b981;color:white;padding:2px 8px;border-radius:10px;">Active</span>')
    status_badge.short_description = 'Status'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:150px; border-radius:8px;" />', obj.image.url)
        elif obj.image_url:
            return format_html('<img src="{}" style="max-height:150px; border-radius:8px;" />', obj.image_url)
        return 'No image'
    image_preview.short_description = 'Image Preview'


@admin.register(DealClick)
class DealClickAdmin(admin.ModelAdmin):
    list_display = ['deal', 'ip_address', 'clicked_at']
    list_filter = ['clicked_at']
    readonly_fields = ['deal', 'ip_address', 'user_agent', 'clicked_at']
    date_hierarchy = 'clicked_at'


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_filter = ['is_active']
    search_fields = ['email']
    list_editable = ['is_active']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
