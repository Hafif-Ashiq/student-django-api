from django.shortcuts import render

from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import StudentSerializer,UserSerializer
from .models import *
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.hashers import check_password
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_students(request):
    try:
        data = Student.objects.all();
        serializer = StudentSerializer(data,many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response({
            "status" : 404 
        })

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_student(request):
    try:
        data = request.data
        # print(data)
        print(request.GET)
        student = Student.objects.filter(uid = data['uid'])[0]
        serializer = StudentSerializer(student)
        # if serialize.is_valid():
        return Response(serializer.data)
        
        # return Response(serialize.errors)

    except Exception as e:
        print(e)
        return Response({
            "status" : 404 
        })

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_student_id(request, id=0):
    try:
        # data = request.data
        # print(data)
        print(id)
        student = Student.objects.filter(uid = id)[0]
        serializer = StudentSerializer(student)
        # if serialize.is_valid():
        return Response(serializer.data)
        
        # return Response(serialize.errors)

    except Exception as e:
        print(e)
        return Response({
            "status" : 404 
        })




@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_student(request):
    
    try:
        data = request.data
        print("Data: " ,data)
        serializer = StudentSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)

        return Response(serializer.errors)
    except Exception as e:
        print(e)
        return Response({
            'status' : "Error Occured"
        })


@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_student(request):
    data = request.data
    obj = Student.objects.get(uid = data['uid'])
    serializer = StudentSerializer(obj,data = data,partial=True)    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
    return Response(serializer.errors)

@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_student_id(request,id):
    data = request.data
    obj = Student.objects.get(uid = id)
    serializer = StudentSerializer(obj,data = data,partial=True)    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
    return Response(serializer.errors)
    

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_student(request):
    data = request.data
    obj = Student.objects.filter(uid = data['uid'])
    obj.delete()
    return Response({
        'status' : "Deleted"
    })


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_student_id(request,id):
    # data = request.data
    obj = Student.objects.filter(uid = id)
    obj.delete()
    return Response({
        'status' : True
    })





class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = serializer.data['username'])
            token_obj , _ = Token.objects.get_or_create(user = user)
            return Response({
                'status' : 200,
                'token' : str(token_obj)
            })
        return Response(serializer.errors)


class LoginUser(APIView):
    def post(self,request):
        try:
            
            username=request.data["username"]
            password=request.data["password"]
            user = authenticate(request, username=username, password=password)
            
            
            if(user is not None):
                token_obj , _ = Token.objects.get_or_create(user = user)
                return Response({
                'status' : True,
                'token' : str(token_obj)
                
            })
            return Response({
                'status' : False
            })
        except Exception as e:
            print(e)
            return Response({
                'status' : False
            })
        
    
@api_view(['POST'])
def get_user(request):
    try:
        print(request.data)
        user_id = Token.objects.get(key=request.data['token']).user_id
        user = User.objects.get(id=user_id)

        return Response({
            'status' : True,
            "username": user.username 
        })
    except Exception as e:
        print(e)
        return Response({
            'status' : False,
            # "username": user.username 
        })



class student_api(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        print(request.user)
        try:
            data = Student.objects.all();
            serialize = StudentSerializer(data,many=True)
            return Response(serialize.data)
        except Exception as e:
            print(e)
            return Response({
                "status" : 404 
            })
        
    def post(self,request):
        try:
            data = request.data
            serializer = StudentSerializer(data= data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response(serializer.data)

            return Response(serializer.errors)
        except Exception as e:
            print(e)
            return Response({
                    "status" : "Error 404",
                    
                })

    def patch(self,request):
        data = request.data
        obj = Student.objects.get(uid = data['uid'])
        serializer = StudentSerializer(obj,data = data,partial=True)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors)
    
    def delete(self,request):
        data = request.data
        obj = Student.objects.filter(uid = data['uid'])
        obj.delete()
        return Response({
            'status' : True
        })
    


class StudentViewSet(viewsets.ModelViewSet):
    try:
        serializer_class = StudentSerializer
        queryset = Student.objects.all()
    except Exception as e:
        print(e)