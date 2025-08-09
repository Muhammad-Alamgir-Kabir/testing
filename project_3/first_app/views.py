from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
     d={'Author':'Rahim', 'Age': 20 , 'lst':['python','is','Best'],'birthday':datetime.datetime.now(), 'courses': [
          
          {
               'id': 1,
               'name':'Alamgir',
               'fee':5000 

          },
          {
               'id': 2,
               'name':'Kabir',
               'fee':10000

          },
          {
               'id': 3,
               'name':'Bablu',
               'fee':15000

          }
            
     ]}
     return render(request,'home.html',d)

