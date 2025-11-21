from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Article


@permission_required('your_app_name.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "article_list.html", {"articles": articles})


@permission_required('your_app_name.can_create', raise_exception=True)
def article_create(request):
    return render(request, "article_create.html")


@permission_required('your_app_name.can_edit', raise_exception=True)
def article_edit(request, id):
    return render(request, "article_edit.html")


@permission_required('your_app_name.can_delete', raise_exception=True)
def article_delete(request, id):
    return render(request, "article_delete.html")
