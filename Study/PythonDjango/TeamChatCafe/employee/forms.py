from django import forms
from employee.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name',
                  'surname',
                  'patronymic',
                  )

        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'patronymic': 'Patronymic'
        }