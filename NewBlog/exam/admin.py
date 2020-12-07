from django.contrib import admin
from .models import Exam,ExamAns,questionkey
# Register your models here.
admin.site.register(Exam)
admin.site.register(questionkey)
admin.site.register(ExamAns)