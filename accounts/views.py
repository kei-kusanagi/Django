from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        print('SUBMITTED REG')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')    

    #cap 8 ep 49 // 7:08