from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre


# Create your views here.

def index(request):
    """View function for home page of site."""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()
    
    # Challenge: Modify the view to generate counts for genres and books that contain a particular word (case
    # insensitive), and pass the results to the context.

    num_genres = Genre.objects.all().count()
    num_books_word = Book.objects.filter(title__icontains='c').count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_word': num_books_word
    }

    return render(request, 'catalog/index.html', context=context)
