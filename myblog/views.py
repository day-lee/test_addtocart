from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#ListView: will allow us to list querysets into the DB, do a query set for us. Look up all the records in the DB and bring them back
#so we can list ot one our webpage. All blog posts

#DetailView: brings back one record. One blog post.

#why use? it will do lots of work for us. -> what work?

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

#not using request
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-post_date']

    #categories drop down : pass context
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.replace('-', ' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    #categories drop down : pass context
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'
    #fields = '__all__' # it's from our model.
    # fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')