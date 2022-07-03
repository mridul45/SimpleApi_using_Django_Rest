from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated



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


@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs,many=True)

    return Response({
        'status':True,
        'message':'Data Fetched',
        'data':serializer.data
    })


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


@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status':False,
                'message':'UID is required',
                'data':{}
            })

        obj = Todo.objects.get(uid=data.get('uid'))
        serializer = TodoSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
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

    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'invalid uid',
            'data':{}
        })


# Lets Learn about API views

class TodoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        todo_objs = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(todo_objs,many=True)

        return Response({
            'status':True,
            'message':'Data Fetched',
            'data':serializer.data
        })

    def post(self,request):
        try:
            data = request.data
            data['user'] = request.user.id
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


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


    @action(detail=False, methods=['post'])
    def add_date_to_todo(self,request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
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

        except Exception as e:
            print(e)
            return Response({
                    'status':False,
                    'message':'Something went wrong',
                }) 