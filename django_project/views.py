import requests
from django.http import response
from django.shortcuts import render

def home(request):
  # Using apis 

  # Example 
  reponse2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = reponse2.json()
  result2 = data2["message"]




  
  return render(request, 'templates/index.html',{'result2': result2})