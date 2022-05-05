from curses.ascii import NUL
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Tutorial,Docunent

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    print("########### ICI tutorial_list ######################## ")
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    #imageTexte = {'data': "kfdmkfdln"}
    Document_list = Docunent.objects.all()
    for t in Document_list:
        if t.NNI != '' :
            return JsonResponse({'data':t.NumeroDocument})
    imageTexte = {'Erreur': "Null"}
    return JsonResponse(imageTexte)


 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    # GET all published tutorials
    return

@api_view(['GET', 'POST', 'DELETE'])
def saveCartData(request):
    print(request.data)
    data = request.data
    nom = data['nom']
    NNI = data['NNI']

    imageTexte = {'done': "ok"}
    return JsonResponse(imageTexte)