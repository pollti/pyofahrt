from django.contrib import admin
from .models import Ofahrt, Building, Location, Room

# Register your models here.


@admin.register(Ofahrt)
class OfahrtAdmin(admin.ModelAdmin):
    list_display = ["__str__", "begin_date", "end_date"]
    fieldsets = (("Allgemeines", {
        "fields": ("begin_date", "end_date")
    }), ("Einstellungen", {
        "fields": ("member_reg_open", "orga_reg_open",
                   "max_members", "queue_tolerance", "self_participation")
    }))


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'rooms']
    list_filter = ['location']

    def rooms(self, obj):
        return obj.room_set.all().count()

    rooms.short_description = "Anzahl Räume"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_filter = ('building', 'usecase_sleep', 'usecase_workshop',
                   'usecase_meal', 'usecase_store', 'usecase_outside')
    list_display = [
        'roomname', 'capacity_string', 'usecase_sleep', 'usecase_workshop',
        'usecase_meal', 'usecase_store', 'usecase_outside'
    ]

    def roomname(self, obj):
        return obj.name + " (" + obj.number + ")"

    roomname.short_description = "Raumname"
    roomname.admin_order_field = 'name'  # making this field sortable by room name

    def capacity_string(self, obj):
        if obj.usecase_sleep:
            if obj.capacity < 0:
                return "-"
            else:
                return obj.capacity
        else:
            return "<i>nicht relevant</i>"

    capacity_string.short_description = "Kapazität"
    capacity_string.allow_tags = True
    capacity_string.admin_order_field = 'capacity'  # making this field sortable by capacity number
