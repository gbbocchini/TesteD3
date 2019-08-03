from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import ModelFormMixin, DeleteView, UpdateView
from .models import Note
from django.contrib.auth import get_user_model
from braces.views import SelectRelatedMixin


User = get_user_model()


class CreateNote(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    model = Note
    fields = ['titulo', 'texto']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)
    
    
class DetailNote(LoginRequiredMixin, DetailView):
    model = Note   

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class ListNote(LoginRequiredMixin, ListView):
    model = Note

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class DeleteNote(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:list')
    
      
class UpdateNote(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['titulo', 'texto']
    template_name_suffix = '_update_form'
