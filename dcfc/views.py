from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Gallery, Article, Video, NewsLetterRecipients
import datetime as dt
from .forms import NewsLetterForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
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


def all_post(request):
    posts = Article.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Article, id=id)
    return render(request, 'blog_detail.html', {"post": post})


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
    name = ''
    email = ''
    comment = ''

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        residence = form.cleaned_data.get("residence")
        comment = form.cleaned_data.get("comment")

        if request.user.is_authenticated():
            subject = str(request.user) + "'s Comment"
        else:
            subject = "A Visitor's Comment"

        comment = name + " with the email, " + email + \
            ", sent the following message:\n\n" + comment
        send_mail(subject, comment, 'kathinimuthinzi@gmail.com', [email])

        context = {'form': form}

        return render(request, 'contact.html', context)

    else:
        context = {'form': form}
        return render(request, 'contact.html', context)
