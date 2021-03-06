from rest_framework import request
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from notes.models import Note
from .serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    search_fields = ['id', 'user', 'titulo', 'texto', 'created_at']

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)