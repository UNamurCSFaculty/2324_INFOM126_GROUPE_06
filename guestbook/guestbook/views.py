from django.views.generic import ListView
from .models import Message
from .forms import MessageForm
from django.shortcuts import redirect

class MessageListView(ListView):
    """
    View for listing all messages in the guestbook.
    """
    model = Message
    template_name = 'guestbook/message_list.html'
    context_object_name = 'messages'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle the POST request for the view.
        """
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message-list')
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)