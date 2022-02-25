from django.contrib import admin

from .models import Flat, Like, Owner


class OwnersFlatInline(admin.TabularInline):
    model = Owner.flats_ownership.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address']
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [
        OwnersFlatInline,
    ]


class LikeAdmin(admin.ModelAdmin):
    raw_id_fields = ('customer', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats_ownership',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Owner, OwnerAdmin)
