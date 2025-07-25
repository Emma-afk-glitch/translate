import os
from django.shortcuts import render
from .forms import TranslateForm
import requests

DEEPL_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_URL = "https://api-free.deepl.com/v2/translate"  # or v2/translate

def home(request):
    translation = None
    if request.method == "POST":
        form = TranslateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resp = requests.post(
                DEEPL_URL,
                data={
                    "auth_key": DEEPL_KEY,
                    "text": data["text"],
                    "source_lang": data["source_lang"],
                    "target_lang": data["target_lang"],
                },
            )
            result = resp.json()
            translation = result["translations"][0]["text"]
    else:
        form = TranslateForm(initial={"source_lang": "EN", "target_lang": "DE"})

    return render(request, "home.html", {
        "form": form,
        "translation": translation,
    })
