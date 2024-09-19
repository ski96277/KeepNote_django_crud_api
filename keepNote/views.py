from django.http import JsonResponse
from .models import NoteModel
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import responses
from rest_framework import status

@api_view(['GET','POST'])
def note_list(request):
    if request.method == 'GET':
        note = NoteModel.objects.all()
        serializer = NoteSerializer(note,many=True)
        return JsonResponse({'notes':serializer.data},safe=False)
        
    if request.method == 'POST':
        serializer = NoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'note':serializer.data},status=status.HTTP_201_CREATED)
        return JsonResponse({'message':'Data parse is failed'})
    return JsonResponse({'message':'Method is not supported'})

@api_view(['GET','DELETE','PUT'])
def note_details(request,id):
    #get note item by id
    try:
        note  = NoteModel.objects.get(pk = id)
    except NoteModel.DoesNotExist:
        return JsonResponse({"message":"Note not found"})
    
    if request.method == "PUT":
        serializer = NoteSerializer(note,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'note': serializer.data})
        return JsonResponse({'message':"Data is not valid"})

    
    elif request.method == "DELETE":
        note.delete()

        return JsonResponse({'message':'Deleted Note'})
    elif request.method == "GET":
        serializer = NoteSerializer(note)

        return JsonResponse({'note':serializer.data})

        