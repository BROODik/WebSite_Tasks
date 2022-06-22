from .models import Task
from django.forms import ModelForm, TextInput, CheckboxInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "completed"]
        widgets ={"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название:'}),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание задачи:'}),
                   "completed": CheckboxInput(),
                   }
