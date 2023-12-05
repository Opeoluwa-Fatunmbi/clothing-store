from django.shortcuts import render
from django.views import View
from apps.general.models import SiteDetail, TeamMember

# Create your views here.


class AboutView(View):
    def get(self, request):
        sitedetail, created = SiteDetail.objects.get_or_create()
        teammembers = TeamMember.objects.all()
        context = {
            "sitedetail": sitedetail,
            "teammembers": teammembers,
        }
        return render(request, "general/about.html", context)


class ContactView(View):
    def get(self, request):
        return render(request, "general/contact.html")
