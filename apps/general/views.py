from django.shortcuts import redirect, render
from django.views import View
from apps.general.forms import MessageForm

from apps.general.models import SiteDetail, TeamMember
import sweetify

# Create your views here.


class AboutView(View):
    def get(self, request):
        sitedetail, created = SiteDetail.objects.get_or_create()
        teammembers = TeamMember.objects.all()
        context = {"sitedetail": sitedetail, "teammembers": teammembers}
        return render(request, "general/about.html", context)


class ContactView(View):
    def get(self, request):
        sitedetail, created = SiteDetail.objects.get_or_create()
        form = MessageForm()
        context = {"sitedetail": sitedetail, "form": form}
        return render(request, "general/contact.html", context)

    def post(self, request):
        sitedetail, created = SiteDetail.objects.get_or_create()
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                title="Sent",
                text="Your message was sent successfully",
                timer=3000,
            )
            return redirect("contact")
        context = {"sitedetail": sitedetail, "form": form}
        return render(request, "general/contact.html", context)
