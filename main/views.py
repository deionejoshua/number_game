from django.shortcuts import render, HttpResponse, redirect
import random

def first_html(request):
    
    if 'rand_Num' not in request.session:
        request.session['rand_Num'] = random.randint(1,100)
    if 'user_input' in request.session:

        if request.session['rand_Num'] < request.session['user_input']:
            message = 'Number is too high try again'
        elif request.session['rand_Num'] > request.session['user_input']:
            message = 'Number is too low try again'
        elif request.session['rand_Num'] == request.session['user_input']:
            message = 'You are correct'
    else:
        message = ''
    context = {
            'message' : message
        }
    return render(request, 'first.html', context)
    

def random_int(request):
    request.session['user_input'] = int(request.POST['user_guess']) 
    return redirect('/')
