from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import CustomUser
from .serializers import UserSerailzers
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from account.permissions import IsManager,IsEmployee



# Admin 


class UsersListAdminView(APIView):
    permission_classes=[IsAdminUser]

    def get(self, request):
        users = CustomUser.objects.exclude(role='Admin')
        serializer = UserSerailzers(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerailzers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully", "user": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        user_id = request.GET.get('id') or request.data.get('id')
        if not user_id:
            return Response(
                {"error": "User ID is required for update"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_instance = get_object_or_404(CustomUser, id=user_id)
        serializer = UserSerailzers(user_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User updated successfully", "user": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user_id = request.GET.get('id') or request.data.get('id')
        if not user_id:
            return Response(
                {"error": "User ID is required for deletion"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_instance = get_object_or_404(CustomUser, id=user_id)
        user_instance.delete()
        return Response(
            {"message": f"User with ID {user_id} deleted successfully"},
            status=status.HTTP_200_OK
        )



# Managers



class UsersListManagerView(APIView):
    permission_classes=[IsManager]
    def get(self, request):
        users = CustomUser.objects.exclude(role='Admin')
        serializer = UserSerailzers(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




# Employees



class UserSelfProfileView(APIView):
    permission_classes=[IsEmployee]
    def get(self, request):
        user = request.user  
        serializer = UserSerailzers(user)
        return Response(serializer.data, status=200)

