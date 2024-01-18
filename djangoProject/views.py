from django.shortcuts import render,redirect


def basex(request):
    return render(request, 'Main/base.html')