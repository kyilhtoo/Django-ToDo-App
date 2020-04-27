from django import forms


class TaskForm(forms.Form):
    task_input = forms.CharField()
    detail_input = forms.CharField()

