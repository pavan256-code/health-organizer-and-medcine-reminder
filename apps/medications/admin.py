"""
Admin configurations for Medications app.
"""

from django.contrib import admin
from apps.medications.models import (
    Medicine, MedicineSchedule, MedicineDose, MedicationLog,
    MedicineStock, MedicineRefill, MedicineExpiry
)


class MedicineStockInline(admin.StackedInline):
    model = MedicineStock
    can_delete = False


class MedicineScheduleInline(admin.TabularInline):
    model = MedicineSchedule
    extra = 1


class MedicineExpiryInline(admin.TabularInline):
    model = MedicineExpiry
    extra = 1


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    inlines = [MedicineStockInline, MedicineScheduleInline, MedicineExpiryInline]
    list_display = ('name', 'generic_name', 'family_member', 'medicine_type', 'dosage', 'status', 'start_date')
    list_filter = ('medicine_type', 'status', 'start_date')
    search_fields = ('name', 'generic_name', 'brand_name', 'prescribed_by', 'family_member__first_name')
    ordering = ('name',)


@admin.register(MedicineSchedule)
class MedicineScheduleAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'frequency', 'specific_times', 'is_active', 'start_date')
    list_filter = ('frequency', 'is_active')
    search_fields = ('medicine__name',)


@admin.register(MedicineDose)
class MedicineDoseAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'date', 'scheduled_time', 'actual_time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('schedule__medicine__name',)
    ordering = ('-date', '-scheduled_time')


@admin.register(MedicationLog)
class MedicationLogAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'family_member', 'status', 'actual_time', 'reason_for_skip')
    list_filter = ('status', 'actual_time')
    search_fields = ('medicine__name', 'family_member__first_name', 'notes')
    ordering = ('-actual_time',)


@admin.register(MedicineStock)
class MedicineStockAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'current_stock', 'minimum_stock_level', 'consumed_quantity', 'unit')
    list_filter = ('unit',)
    search_fields = ('medicine__name',)


@admin.register(MedicineRefill)
class MedicineRefillAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'refill_date', 'refill_quantity', 'cost', 'pharmacy_source')
    list_filter = ('refill_date',)
    search_fields = ('medicine__name', 'pharmacy_source')


@admin.register(MedicineExpiry)
class MedicineExpiryAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'batch_number', 'expiry_date', 'status', 'alert_days_before')
    list_filter = ('status', 'expiry_date')
    search_fields = ('medicine__name', 'batch_number')
