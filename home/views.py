from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics

# Create your views here.


class StudentGeneric(generics.ListAPIView,generics.CreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class StudentGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	lookup_field = "id"

class RegisterUser(APIView):

	def post(self, request):
		serializer = UserSerializer(data=request.data)

		if not serializer.is_valid():
			return Response({"status":404,"message":"Something went wrong"})

		serializer.save()
		user = User.objects.get(username=serializer.data['username'])
		refresh = RefreshToken.for_user(user)
		# print(data)
		return Response({"status":200,"payload":serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token),"message":"Sent"})

class StudentAPI(APIView):

	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self,request):
		student_objs = Student.objects.all()
		serializers = StudentSerializer(student_objs,many=True)
		return Response({"status":200,"payload":serializers.data})


	def post(self,request):
		data = request.data
		serializer = StudentSerializer(data=request.data)

		if not serializer.is_valid():
			return Response({"status":404,"message":"Something went wrong"})

		serializer.save()
		# print(data)
		return Response({"status":200,"payload":serializer.data,"message":"Sent"})


	def delete(self,request):
		try:
			student_obj = Student.objects.get(id=request.data['id'])
			student_obj.delete()
			return Response({"status":200,"message":"Successful"})

		except Exception as e:
			return Response({"status":403,"message":"Invalid request"})


	def patch(self,request):
		try:
			student_obj = Student.objects.get(id=request.data['id'])
			data = request.data
			serializer = StudentSerializer(student_obj,data=request.data,partial=True)

			if not serializer.is_valid():
				return Response({"status":404,"message":"Something went wrong"})

			serializer.save()
			# print(data)
			return Response({"status":200,"payload":serializer.data,"message":"Sent"})

		except Exception as e:
			return Response({"error":403,"message":"Invalid ID"})














# @api_view(['GET'])
# def home(request):
# 	student_objs = Student.objects.all()
# 	serializers = StudentSerializer(student_objs,many=True)
# 	return Response({"status":200,"payload":serializers.data})


# @api_view(['POST'])
# def post_student(request):
# 	data = request.data
# 	serializer = StudentSerializer(data=request.data)

# 	if not serializer.is_valid():
# 		return Response({"status":404,"message":"Something went wrong"})

# 	serializer.save()
# 	# print(data)
# 	return Response({"status":200,"payload":serializer.data,"message":"Sent"})


# @api_view(['PATCH'])
# def update_student(request,id):

# 	try:
# 		student_obj = Student.objects.get(id=id)
# 		data = request.data
# 		serializer = StudentSerializer(student_obj,data=request.data,partial=True)

# 		if not serializer.is_valid():
# 			return Response({"status":404,"message":"Something went wrong"})

# 		serializer.save()
# 		# print(data)
# 		return Response({"status":200,"payload":serializer.data,"message":"Sent"})

# 	except Exception as e:
# 		return Response({"error":403,"message":"Invalid ID"})


# @api_view(['DELETE'])
# def delete_student(request,id):

# 	try:
# 		student_obj = Student.objects.get(id=id)
# 		student_obj.delete()
# 		return Response({"status":200,"message":"Successful"})

# 	except Exception as e:
# 		return Response({"status":403,"message":"Invalid request"})



# @api_view(['GET'])
# def get_book(request):
# 	book_objs = Book.objects.all()
# 	serializer = BookSerializer(book_objs,many=True)

# 	return Response({"status":200,"payload":serializer.data})