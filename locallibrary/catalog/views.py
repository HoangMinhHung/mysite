from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

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

    # Part7: Session
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    request.session.set_expiry(0)
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_word': num_books_word,
        'num_visits': num_visits
    }
    print(request.session.get_expiry_date())
    print(request.session.get_expiry_age())
    return render(request, 'catalog/index.html', context=context)


class BookListView(generic.ListView):
    # model = Book
    context_object_name = 'my_book_list'  # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='c')[:5]  # Get 5 books containing the title c
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    # model = Author
    context_object_name = 'author_list'  # your own name for the list as a template variable
    queryset = Author.objects.all() # Get 5 books containing the title c
    template_name = 'catalog/author_list.html'  # Specify your own template name/location
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author
