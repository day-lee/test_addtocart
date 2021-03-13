from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy


# ListView: will allow us to list querysets into the DB, do a query set for us. Look up all the records in the DB and bring them back
# so we can list ot one our webpage. All blog posts

# DetailView: brings back one record. One blog post.

# why use? it will do lots of work for us. -> what work?

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

# not using request
class HomeView(ListView):
    model = Customer
    template_name = 'home.html'

    # categories drop down : pass context
    def get_context_data(self, *args, **kwargs):
        cat_menu = Tag.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context



from django.shortcuts import render

# Create your views here.
