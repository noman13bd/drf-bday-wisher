from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer

class CustomerListApiView(APIView):

    def get(self, request, *args, **kwargs):
        bdays = Customer.objects.all()
        serializer = CustomerSerializer(bdays, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'bday': request.data.get('bday'),
        }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)