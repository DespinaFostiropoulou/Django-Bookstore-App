from django.utils import timezone
from .models import Book
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def post_list(request):
    cat = request.GET.get('cat', '')
    syg = request.GET.get('syg', '')
    txt = request.GET.get('txt', ' ')
    ek = request.GET.get('ek', ' ')


    try:
        cat = int(cat)
    except:
        cat = False
    try:
        syg = int(syg)
    except:
        syg = False
    try:
        ek = int(ek)
    except:
        ek = False

    if cat is False :
        if syg is False:
            if ek is False:
              if txt=='':
                books = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
              else:
                books = Book.objects.filter(published_date__lte=timezone.now()).filter(Q(perilipsi__contains=txt) | Q(titlos__contains=txt)).order_by('published_date')
            else:
              books = Book.objects.filter(published_date__lte=timezone.now()).filter(ekdotikos_oikos=ek).order_by('published_date')
        else:
            books = Book.objects.filter(published_date__lte=timezone.now()).filter(syggrafeas=syg).order_by('published_date')
    else:
        books = Book.objects.filter(published_date__lte=timezone.now()).filter(tipos=cat).order_by('published_date')

    page = request.GET.get('page', 1)

    paginator = Paginator(books, 16)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'books': books})


def post_detail(request,pk):
    book = get_object_or_404(Book, pk=pk)
    return render (request,'blog/post_detail.html', {'book': book})

