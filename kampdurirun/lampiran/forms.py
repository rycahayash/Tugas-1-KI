# forms.py
from django import forms

class DocumentPasswordForm(forms.Form):
    password = forms.CharField(label="Enter the Document Password", widget=forms.PasswordInput)
