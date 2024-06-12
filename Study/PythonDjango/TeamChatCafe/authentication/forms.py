from django import forms
from authentication.models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'email',
                  'password',
                  # 'updated_at',
                  # 'created_at'
                  )

        labels = {
            'first_name': 'Name',
            'middle_name': 'Middle Name',
            'last_name': 'Last Name'
        }