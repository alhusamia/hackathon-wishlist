from django.shortcuts import render,redirect
from .forms import  SignupForm, SigninForm,WisherForm
from .models import WisherList
from django.contrib.auth import login, authenticate, logout


def wisher_list(request):
    wishers = WisherList.objects.filter(wisher=request.user).order_by("-time")


    context = {
        "wishers": wishers,
    }
    return render(request, 'wisher_list.html', context)




def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("start")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('wisher-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)


def wisher_create(request):
    form = WisherForm()
    if request.user.is_anonymous:
        return redirect('signin')


    if request.method == "POST":
        form = WisherForm(request.POST, request.FILES or None)
        if form.is_valid():
            wisher = form.save(commit=False)
            wisher.wisher = request.user
            wisher.save()

            return redirect('wisher-list')

    context = {
    "form": form,
    }
    return render(request, 'wisher_create.html', context)


def start(request):
    return render(request,'home.html')


def signout(request):
    logout(request)
    return redirect("signin")

def wisher_delete(request, wisher_id):
    wisher=WisherList.objects.get(id=wisher_id)
    if request.user.is_anonymous:
        return redirect("signin")
    if  request.user != wisher.wisher:
        return redirect("wisher-list")
    wisher.delete()

    return redirect('wisher-list')
