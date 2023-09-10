from rest_framework import generics
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class SignUpView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "You have been signed up successfully"
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
