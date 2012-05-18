from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from main.models import User, Tweet
from main.forms import UserForm, TweetForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.models import User
#from django

#@cache_page(60 * 15)
def home(request):
	users = User.objects.all()
	return render_to_response('home.html', {
		'users' : users
	})


#@login_required
#def index(request):
#    return render_to_response('index.html', context_instance=RequestContext(request))


#def login(request):
#    form = AuthenticationForm()
#    if request.method == "POST":
#        username = request.POST['username']
#        try:
#            user = User.objects.get(email=username)
#        except User.DoesNotExist:
#            try:
#                user = User.objects.get(username=username)
#            except User.DoesNotExist:
#                menerror = 'No manches no te has registrado >.>'
#                return render_to_response('login.html', {
#        'form': form, 'menerror': menerror,
#        }, RequestContext(request))
#        password = request.POST['password']
#        user = auth.authenticate(username=user.username, password=password)
#        form = AuthenticationForm(None, request.POST)
#        if user is not None and user.is_active:
#            auth.login(request, user)
#            return redirect('index')
#    return render_to_response('login.html', {
#        'form': form,
#        }, RequestContext(request))



#@cache_page(60 * 15)
def show_user(request, pk):
	user = get_object_or_404(User, pk=pk)					
	return render_to_response('show_user.html', {
		'user': user,
	}, RequestContext(request))


def add_user(request):
	form = UserForm()
	if request.method == 'POST':
		form = UserForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render_to_response('add_user.html', {
		'form': form,
	}, RequestContext(request))

def add_tweet(request):
	form = TweetForm()
	if request.method == 'POST':
		form = TweetForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render_to_response('add_user.html', {
		'form': form,
	}, RequestContext(request))
#@login_required
def edit_user(request, pk):
	user = get_object_or_404(User, pk=pk)
	form = UserForm(instance=user)
	if request.method =='POST':
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render_to_response('add_user.html',{
		'form': form,
	}, RequestContext(request))

def edit_tweet(request, pk):
	tweet = get_object_or_404(Tweet, pk=pk)
	form = TweetForm(instance=tweet)
	if request.method =='POST':
		form = TweetForm(request.POST, instance=tweet)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render_to_response('add_user.html',{
		'form': form,
	}, RequestContext(request))


def show_follow(request, pk):
        users_owner = get_object_or_404(User, pk=pk)
	return render_to_response('show_follow.html', {
		'users_owner': users_owner
	}, RequestContext(request))


def delete_tweet(request, pk):
	
	Tweet.objects.filter(pk=pk).delete()
	return redirect('home')

def delete_user(request, pk):
	
	User.objects.filter(pk=pk).delete()
	return redirect('home')
