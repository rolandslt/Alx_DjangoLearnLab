from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Article, Book
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .forms import ArticleForm
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@login_required
def books(request):
    return render(request, "bookshelf/books.html")

@csrf_protect
def article_list(request):
    # Safe query using ORM (prevents SQL injection)
    search_query = request.GET.get("q", "")
    articles = Article.objects.filter(title__icontains=search_query)
    return render(request, "article_list.html", {"articles": articles})

@csrf_protect
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():  # Input is validated
            form.save()
    else:
        form = ArticleForm()
    return render(request, "article_create.html", {"form": form})

@csrf_protect
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm(instance=article)
    return render(request, "article_edit.html", {"form": form})

@csrf_protect
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        article.delete()
    return render(request, "article_delete.html", {"article": article})