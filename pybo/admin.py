from django.contrib import admin

from .models import Answer, Comment, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
