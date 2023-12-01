from django.shortcuts import render
from django.views import View

# Create your views here.


class AboutView(View):
    def get(self, request):
        return render(request, "general/about.html")


class ContactView(View):
    def get(self, request):
        return render(request, "general/contact.html")
