from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Article


class HomePageView(TemplateView):
    template_name = 'home.html'


class SiteNoticeView(TemplateView):
    template_name = 'site_notice.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy_policy.html'


def articles(request):
    articles = Article.objects.all()

    context = {
        "articles": articles,
    }

    return render(request, "external_articles.html", context)
