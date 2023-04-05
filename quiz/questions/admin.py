from django.contrib import admin
from django import forms

from .models import Category, Question, Answer


class AnswerInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        correct_answers = wrong_answers = 0

        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['correct_answer']:
                    correct_answers += 1
                else:
                    wrong_answers += 1

        if correct_answers == 0:
            raise forms.ValidationError('Нет правильных ответов')
        elif wrong_answers == 0:
            raise forms.ValidationError('Нет неправильных ответов')


class AnswerInline(admin.TabularInline):
    model = Answer
    formset = AnswerInlineFormset


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]


admin.site.register(Category)
