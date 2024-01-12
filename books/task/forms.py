from django import forms

class BookCreateForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"type":"form-control"}))
    author=forms.CharField(widget=forms.TextInput(attrs={"type":"form-control"}))
    category=forms.CharField(widget=forms.TextInput(attrs={"type":"form-control"}))
    price=forms.IntegerField()