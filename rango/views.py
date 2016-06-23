# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from rango.models import Category, Page
from rango.forms import CategoryForm, AddForm, AddUser, ContactForm, UserForm, UserProfileForm


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
            first = form.cleaned_data['firstname']
            last = form.cleaned_data['lastname']
            return HttpResponseRedirect('/rango/')
    else:
        form = AddUser()

    return render(request, 'rango/user.html', {'form': form})


#def contact(request):
#    if request.method == 'POST':
#        form = ContactForm()
#        if form.is_valid():
#            subject = form.cleaned_data['subject']
#            message = form.cleaned_data['message']
#            sender = form.clean_data['sender']
#            cc_myself = form.clean_data['cc_myself']
#
#                recipients = ['haimapi@163.com']
#            if cc_myself:
#        recipients.append(sender)
#    send_mail


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # if the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # hash the password with the set_password method
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

