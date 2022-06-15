from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Contacts


# Create your views here.
from .serializers import ContactsSerializer


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

#
# class ContactsAPIList(generics.ListCreateAPIView):  # GET and POST
#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializer
#
#
# class ContactsAPIUpdate(generics.UpdateAPIView):
#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializer
#
#
# class ContactsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializer



