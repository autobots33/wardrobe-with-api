import token
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token    
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes,api_view
#from rentapp import serializers



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getUser(request,format=None):
    user=User.objects.all()
    content = {
        'user': str(request.user),  
        'auth': str(request.auth),  
    }
    return Response(content)
    #serializer=UserSerializer(user,many=True)
   # return Response(serializer.data)

 
"""  if request.method=='GET':
        user=User.objects.all()
        
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
"""

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
def addUser(request):
    serializer=UserSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        user= serializer.save()
        toek=Token.objects.get(user=User).key
        data['token']=token
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    else:
        data=serializer.errors
    return Response(data)




@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateUser(request,id,format=None):
    user=User.objects.get(pk=id)
    serializer=UserSerializer(user,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED) 





@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteUser(request,id,format=None):
    user=User.objects.get(pk=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

""" @api_view(['GET','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def User_detail(request,id,format=None):
    
    try:
        user=User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_NOT_FOUND)
    
    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data)
    elif request.method=='PUT': 
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """

         