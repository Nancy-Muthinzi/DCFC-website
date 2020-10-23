from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Gallery, Blog, Video, NewsLetterRecipients
import datetime as dt
from .forms import NewsLetterForm, ContactForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    date = dt.date.today()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            HttpResponseRedirect('welcome')
    else:
        form = NewsLetterForm()
    return render(request, 'welcome.html', {'date': date, 'letterForm': form})


def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)


def bstudy(request):
    return render(request, 'bstudy.html')


def fgroup(request):
    return render(request, 'fgroup.html')


def program(request):
    return render(request, 'program.html')


def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog})


def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery': gallery})


def video(request):
    video = Video.objects.all()
    return render(request, 'video.html', {'video': video})


def search_results(request):

    if 'blog' in request.GET and request.GET["blog"]:
        search_term = request.GET.get("blog")
        searched_blogs = Blog.search_by_content(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "blogs": searched_blogs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
