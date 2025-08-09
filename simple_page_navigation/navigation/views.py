from django.shortcuts import render


def about(request):
    return render(request,'navigation/about.html')
# Create your views here.
def contact(request):
    return render(request,'navigation/contact.html')
