from django.contrib import admin
from models import School,District,AYPDetail,AYPSummary


class AYPDetailInlineAdmin( admin.TabularInline ):
    model = AYPDetail


class AYPSummaryInlineAdmin( admin.TabularInline ):
    model = AYPSummary


class SchoolAdmin( admin.ModelAdmin ):
    inlines = [
        AYPDetailInlineAdmin,
        AYPSummaryInlineAdmin
    ]
    list_filter = ( 'district',)
    search_fields = ( 'name','district__name', )
    list_display = ("name","active","school_type", )


class SchoolInlineAdmin( admin.TabularInline ):
    model = School


class DistrictAdmin( admin.ModelAdmin ):
    inlines = [
        SchoolInlineAdmin,
    ]
    search_fields = ( 'name', )
    select_related = True


class AYPDetailAdmin( admin.ModelAdmin ):
    fieldsets = (
            (None, {
                'fields': ('school', 'district', 'year')
            }),
            ('Communication Arts', {
                'fields': ('comm_school_total', 'comm_black_prof', 'comm_hispanic_prof','comm_indian_prof','comm_white_prof','comm_other_prof','comm_low_income_prof','comm_special_ed_prof', 'comm_low_english_prof' )
            }),
            ('Mathematics', {
            'fields': ('math_school_total','math_black_prof', 'math_hispanic_prof','math_indian_prof','math_white_prof','math_other_prof','math_low_income_prof','math_special_ed_prof', 'math_low_english_prof' )
            }),
            ('Additional Indicators', {
                'fields': ( 'attendance_pct','graduation_pct' )
            }),
        )
    list_filter = ( 'year', 'district', )
    search_fields = ( 'school.name','district.name', )
    list_display = ('school','district','year',)


class AYPSummaryAdmin( admin.ModelAdmin ):
    list_filter = ( 'district', )
    search_fields = ( 'school.name','district.name', )


admin.site.register( School, SchoolAdmin )
admin.site.register( District, DistrictAdmin )
admin.site.register( AYPDetail, AYPDetailAdmin )
admin.site.register( AYPSummary, AYPSummaryAdmin )

