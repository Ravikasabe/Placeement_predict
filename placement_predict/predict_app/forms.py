from django import forms
from .models import Users


class UserForm(forms.ModelForm):
    class Meta:
        model = Users    
        fields = [ 'gender', 'ssc_p', 'ssc_b', 'hsc_p', 'hsc_b', 
                        'degree_p', 'degree_t', 'workex','specialisation', 
                         'status', 'salary', 'Name', 'email', 'mobile', 
                        'DOB', 'ssc_y', 'degree', 'university', 'Stream', 
                        'degree_passoutYear', 'workex_company', 'skills', 
                        'certificates', 'resume']



    
