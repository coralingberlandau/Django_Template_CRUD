from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .models import Book
from .serializer import BookSerializer

@api_view(['GET'])
def index(req):
   return Response({'hello': 'world'})

@api_view(['GET'])
def test(req):
   return Response({'test': 'success'})

# register 
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response({'Success': 'new user born'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def priverty(req):
  return Response({'priverty': 'success'})

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def book_view(request, id=None):
   if request.method == 'GET':
       if id is not None:
           book = get_object_or_404(Book, pk=id)  # single
           return Response(BookSerializer(book, many=False).data)
       else:
           return Response(BookSerializer(Book.objects.all(), many=True).data)
   elif request.method == 'POST':
       prod_serializer = BookSerializer(data=request.data)
       if prod_serializer.is_valid():
           prod_serializer.save()
           return Response({'message': 'book created successfully'})
       else:
           return Response(prod_serializer.errors)
   elif request.method in ['PUT', 'PATCH']:
       try:
           book = Book.objects.get(id=id)
       except Book.DoesNotExist:
           return Response("not found")
       ser = BookSerializer(data=request.data)
       old_task = Book.objects.get(id=id)
       ser.update(old_task, request.data)
       return Response({'message': 'book update successfully'})
   elif request.method == 'DELETE':
       try:
           book = Book.objects.get(id=id)
       except Book.DoesNotExist:
           return Response("not found")
       book.delete()
       return Response({'message': 'book deleted successfully'})