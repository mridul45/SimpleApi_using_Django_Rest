from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *

# Create your views here.
@api_view(['GET','POST','PATCH']) # --> here we need to specify the methods we wat to apply ot if we try to test POST method error will we thrown.
def home(request):

    if request.method == 'GET':
        return Response({
            'status':200,
            'message':'Django Rest framework is working',
            'method-called':'You called GET method'
        })

    elif request.method == 'POST':
        return Response({
            'status':200,
            'message':'Django Rest framework is working',
            'method-called':'You called POST method'
        })

    elif request.method == 'PATCH':
        return Response({
            'status':200,
            'message':'Django Rest framework is working',
            'method-called':'You called PATCH method'
        })

    else:
        return Response({
            'message':'No such call'
        })

# the above is a get api
# The api_view decorator converts the django function into an api


@api_view(['POST'])
def post_todo(request):
    
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'status':True,
            'message':'Success Operation',
            'data':serializer.data
        })
        
        
        
        return Response({
            'status':False,
            'message':'invalid data',
            'data':serializer.errors
        })

        print(data)
        return Response({
            'status':True,
            'message':'Success todo created',
        })

    except Exception as e:
        print(e)
    return Response({
            'status':False,
            'message':'Something went wrong',
        })