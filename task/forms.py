from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'priority', 'deadline', 'isitdone']
        labels = {'text': 'Задача', 'priority':'Приоритет', 'deadline':'Срок выполнения','isitdone':'Выполнено'}
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

