from django.contrib.gis import admin
from models import Organization, Person, Salary

class OrganizationAdmin(admin.ModelAdmin):
	pass


class PersonAdmin(admin.ModelAdmin):
	list_filter = ("organization", )
	list_search = ("name", "organization", )


class SalaryAdmin(admin.ModelAdmin):
	list_filter = ("person__organization", )


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Salary, SalaryAdmin)
