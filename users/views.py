#Django
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.views.generic import DeleteView
from django.shortcuts import render
from django.urls import reverse
#Models
from django.contrib.auth.models import User
from users.models import Profile
from inventory.models import Articles
#Forms
from users.forms import SignupForm,ProfileForm

def login_views(request, *args, **kwargs):
    #Login views
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect('inv:feed')
        else:
            return render(request,'users/login.html', {'error': 'Invalid username and password'})
    return render(request,'users/login.html')

def signup(request):
    #Sign up view
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form.SigupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form':form}
    )

@login_required
def update_profile(request):
    #update user profile view
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILE)
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
        user = self.get_object()
        context['inventory'] = Articles.objects.filter(user=user).order_by('-created')
        return context

@login_required
def logout_view(request):
    #view log out
    logout(request)
    return redirect('user:login')