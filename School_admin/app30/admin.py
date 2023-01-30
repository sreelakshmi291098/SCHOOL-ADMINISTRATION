from django.contrib import admin

# Register your models here.
from app30.models import Reg_stud,login,Reg_teach,Apply_leave,teach_leave,Exam

admin.site.register(Reg_stud)
admin.site.register(Reg_teach)
admin.site.register(Apply_leave)
admin.site.register(teach_leave)
admin.site.register(Exam)
admin.site.register(login)