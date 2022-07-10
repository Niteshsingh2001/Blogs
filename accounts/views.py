from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signin(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(username = user_name,password = password)
        if user is None:
            cont = {"error" : "Something went wrong!! "}
            return render(request,'account.html',cont)
        else:
            login(request,user)
            cont = {"name" :user,"status":True}
            return render(request,'account.html',cont)

    return render(request,'account.html')

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts/')

    return render(request,'signout.html')


def reg(request):

    x =UserCreationForm(request.POST or None)

    cont = {"f":x}
    if x.is_valid():
        x.save()
        return redirect ("/")


    return render(request,'reg.html',cont)