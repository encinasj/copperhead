#Django
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render,redirect
from django.views.generic import DeleteView
from django.shortcuts import render
from django.urls import reverse

#Models
from django.contrib.auth.models import User
from users.models import Profile
from inventory.models import Articles
#Forms
from users.forms import RegisterForm,ProfileForm

@csrf_exempt
def login_views(request, *args, **kwargs):
    #Login views
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html', {'error': 'Credenciales invalidas'})
    return render(request,'users/login.html')

@login_required
def logout_views(request):
    #view log out
    logout(request)
    return redirect('users:login')

@login_required
def users_register(request):
    users = User.objects.all()
    context = {
        'users' : users,
    }
    template_name = 'users/all_users.html'
    return render (request, template_name, context)

@login_required
def register(request):
    #Register view
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:l_register')
    else:
        form = RegisterForm()

    return render(
        request=request,
        template_name='users/register.html',
        context={'form': form}
        )

@login_required
def update_profile(request):
    #update user profile view
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            url = reverse('users:detail', kwargs={'username':request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()
    
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

class UserDetailView(LoginRequiredMixin,DeleteView):
    #User detail view
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        #add user to context
        context = super().get_context_data(**kwargs)
        name = self.get_object()
        context['articles'] = Articles.objects.filter(name=name).order_by('-created')
        return context
