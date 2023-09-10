from .serializers import PlanSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Plan
from rest_framework.response import Response
from rest_framework import permissions


class ListCreatePlan(ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        data = {
            "message": "All my todos",
            "data": serializer.data  # Include the serialized data
        }

        return Response(data)


class DetailPlan(RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
