from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sample_api import serializers



class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list Of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most controle over your application logic',
            'Is mapped mannually to URLs'
        ]

        return Response({'message': 'Hello!','an_apiview': an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
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

    def put(self,request,pk=None):
        """Handel updating an object"""
        return Response({'message': 'PUT'})

    def patch(self,request,pk=None):
        """Handel partial update of an object"""
        return Response({'message': 'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'message': 'DELETE'})