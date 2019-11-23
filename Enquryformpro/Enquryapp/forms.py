from django import forms
from multiselectfield import MultiSelectFormField
class EnquryForm(forms.Form):
    name = forms.CharField(
        label="Enter your Name:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'yours name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter your email:",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'yours email'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter your mobile no:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your mob no'
            }
        )
    )
    COURSES_CHOICES = (
        ('PY', 'Python'),
        ('DJ', 'Django'),
        ('RA', 'Rest API'),
        ('UI', 'User Interface')
    )
    course=MultiSelectFormField(choices=COURSES_CHOICES,label="Select your required courses")
    LOCATION_CHOICES = (
        ('HYD', 'Hyderbad'),
        ('BANG', 'Bangalore'),
        ('che', 'Chennai')
    )
    location=MultiSelectFormField(choices=LOCATION_CHOICES,label="select your required location")
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    )
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect,label="Select your Gender")
    start_date=forms.DateField(
        widget=forms.SelectDateField(),
        label="select your date:"
    )



