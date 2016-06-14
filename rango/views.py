from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, AddForm, AddUser


# Create your views here.
def index(request):
    # con_text = {'boldmessage':'i am bold', 'another':'i am another'}
    # return render(request, 'rango/index.html', con_text)
    category_list = Category.objects.order_by('-likes')
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':

        form = CategoryForm(request.POST)

        # a valid form?
        if form.is_valid():
            # Save the new category to the database
            form.save(commit=True)

            return index(request)
        else:
            # The supplied form contained errors
            print form.errors
    else:
        # If the request was not a POST, display the form to enter
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})


def calc(request):
    if request.method == 'POST':
        form = AddForm(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()

    return render(request, 'rango/calc.html', {'form': form})


def user(request):
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            return HttpResponse('Hello {0} {1}'.format(firstname, lastname))
    else:
        form = AddUser()

    return render(request, 'rango/user.html', {'from': form})