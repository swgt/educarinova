from django.contrib import admin
from educarinova.management.models import School, Student, Unit, Contact, Employee, Address, \
    Matriculation, Attendance, Score, TuitionFee, Serie, Class, SystemClass, ClassSystemClass


class SchoolModelAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'cnpj', 'number_inep', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('company_name', 'cnpj', 'created_at')
    list_filter = ('created_at',)


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'created_at')
    list_filter = ('created_at',)

admin.site.register(School, SchoolModelAdmin)
admin.site.register(Contact)
admin.site.register(Unit)
admin.site.register(Employee)
admin.site.register(Matriculation)
admin.site.register(Attendance)
admin.site.register(Class)
admin.site.register(SystemClass)
admin.site.register(ClassSystemClass)
admin.site.register(Score)
admin.site.register(Address)
admin.site.register(Serie)
admin.site.register(TuitionFee)
admin.site.register(Student, StudentModelAdmin)