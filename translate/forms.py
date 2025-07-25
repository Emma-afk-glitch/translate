from django import forms

LANG_CHOICES = [
    ("EN", "English"),
    ("DE", "German"),
    ("FR", "French"),
    # add more languages as needed
]

class TranslateForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Enter text to translate…"}),
        label="",
    )
    source_lang = forms.ChoiceField(choices=LANG_CHOICES, label="From")
    target_lang = forms.ChoiceField(choices=LANG_CHOICES, label="To")
