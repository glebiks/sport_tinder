from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import SportForm
from django.db.models import Q


# Create your views here.
@login_required(login_url='signin')
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    user_matches = [int(i) for i in user_profile.matches.split(',')]
    print(user_matches)
    user_suggestions = [el for el in Profile.objects.iterator() if (el.id_user not in user_matches) and (el.id_user != user_profile.id_user)]

    context = {'user_profile': user_profile,
               'user_suggestions': user_suggestions}

    if request.method == 'POST':
        suggestion_id = request.POST['suggestion_id']
        user_profile.matches += (','+str(suggestion_id))
        user_profile.save()
        return redirect('index')

    return render(request, 'index.html', context)


@login_required(login_url='signin')
def matches(request):
    user_profile = Profile.objects.get(user=request.user)
    user_matches = [int(i) for i in user_profile.matches.split(',')]
    match_users = [el for el in Profile.objects.iterator()
                   if el.id_user in user_matches[1:]]

    context = {'user_profile': user_profile, 'match_users': match_users}
    return render(request, 'matches.html', context)


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    context = {'user_profile': user_profile}

    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            sport = request.POST['sport']
            tg_link = request.POST['tg_link']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.sport = sport
            user_profile.tg_link = tg_link
            user_profile.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            sport = request.POST['sport']
            tg_link = request.POST['tg_link']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.sport = sport
            user_profile.tg_link = tg_link
            user_profile.save()

        return redirect('settings')

    return render(request, 'setting.html', context)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

                # Log in user and redirect to settings page
                user_login = auth.authenticate(
                    username=username, password=password)
                auth.login(request, user_login)

                # create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is Invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
