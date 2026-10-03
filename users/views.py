from django.shortcuts import render, redirect
from users.forms import UserForm, UserUpdateForm
from .models import User
# Create your views here.

def list_users(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm()

    return render(request, 'users/create.html', {'form': form})

def update_user(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')

    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'users/update.html', {'form': form})

def delete_user(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()

    return redirect('list_users')