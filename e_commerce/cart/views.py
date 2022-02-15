from functools import partial
from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer, Deliveredform
from .models import CartItem
from django.shortcuts import get_object_or_404
from rest_framework import generics

class CartItemAddView(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)


class CartItemView(APIView):
    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        item = CartItem.objects.all()
        serializer = CartItemSerializer(item, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class CartUpdateView(APIView):
    def patch(self, request, id=None):
        item = CartItem.objects.get(id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CartDeleteView(APIView):
    def delete(self ,request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class OrderDetails(APIView):
     def post(self, request):
        serializer = Deliveredform(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

     def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = Deliveredform(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        item = CartItem.objects.all()
        serializer = Deliveredform(item, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

