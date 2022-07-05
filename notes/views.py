from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()



#to filter records by username
class NoteList(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(user=username)
        return queryset


class NoteListed(APIView):
    """
    Retrieve, update or delete a note instance.
    """
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Note = self.get_object(pk)
        serializer = NoteSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Note = self.get_object(pk)
        serializer = NoteSerializer(Note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Note = self.get_object(pk)
        Note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)