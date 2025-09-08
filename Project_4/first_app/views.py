from django.shortcuts import render
from . forms import ContactForm

# Create your views here.
def index(request):
    data= [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  },
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
  },
  {
    "userId": 1,
    "id": 4,
    "title": "eum et est occaecati",
    "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
  },
  {
    "userId": 1,
    "id": 5,
    "title": "nesciunt quas odio",
    "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
  }]
    return render(request,'index.html',{'data':data})

def about(request):
    return render(request,'index.html',{'id':id})

def submit_form(request):
    if request.method == 'POST':
        name= request.POST.get('username')
        email= request.POST.get('email')
        select= request.POST.get('select')
        return render(request, 'form.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request,'./form.html')
    

def DjangoForm(request):
    if request.method=='POST':
      form=ContactForm(request.POST, request.FILES)
      if form.is_valid():
          file=form.cleaned_data['file'] 
          with open('first_app/upload/'+file.name,'wb+') as destination:
              for chunk in file.chunks():
                  destination.write(chunk) 
          print(form.cleaned_data)
          return render(request,'django_form.html', {'form': form})
    else:
        form=ContactForm()
        return render(request,'django_form.html', {'form': form})
    
