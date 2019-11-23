from django import forms
class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter your Name:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'yours name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter your Rating:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'yours rating'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter your Name:",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your feedback..'
            }
        )
    )