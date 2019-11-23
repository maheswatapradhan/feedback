from django import forms


class Empform(forms.Form):
    # name = forms.CharField(max_length=100)
    # location = forms.CharField(max_length=100)
    # salary = forms.IntegerField()
    # email = forms.EmailField(max_length=100)
    name = forms.CharField(
        label="Enter your Name:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'yours name'
            }
        )
    )
    location = forms.CharField(
        label="Enter your location:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'yours name'
            }
        )
    )
    salary = forms.IntegerField(
        label="Enter your salary:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'yours salary'
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
