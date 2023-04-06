from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import viewsets
from profiles_api import serializers



class HelloApiView(APIView):
    '''Test API View'''
    # Serializer acts like a Form for APIs
    # It offers field(s) to make use of POST, PUT and PATCH methods.
    # In this case we have added a 'name' field which can be used to add or update the name
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Returns a list of APIView features'''

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        '''Create a Hello message wih our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''
    # Consider then as Djangio function based views and Class based views
    # APIView set is function based, ViewSet is Class based

    serializer_class = serializers.HelloSerializer

    # URL defines in router executes this LIST function to begin with
    def list(self, request):
        '''Return a Hello Message'''
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        '''Create a new Hello Message like POST method'''
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message, 'http_method': 'POST'})
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        
    
    def retrieve(self, request, pk=None):
        '''Handle getting an object by its ID field like GET method'''

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        '''Handle updating an object by its ID field'''

        return Response({'http_method': 'PUT'})
    
    
    def partial_update(self, request, pk=None):
        '''Handle updating part of an object by its ID field'''

        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        '''Handle removing an object by its ID field'''

        return Response({'http_method': 'DELETE'})