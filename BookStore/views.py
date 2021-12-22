from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

class PostListView(generic.ListView):
    template_name = 'post_list.html'
    queryset = models.Post.objects.all()

    def get_queryset(self):
        return models.Post.objects.all()

class PostDetailView(generic.DetailView):
    template_name = 'post_detail.html'

    def get_object(self,**kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)

class PostCreateView(generic.CreateView):
    template_name = 'add_post.html'
    form_class = forms.PostForm
    success_url = '/posts/'
    queryset = models.Post.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)

class PostUpdateView(generic.UpdateView):
    template_name = 'add_post.html'
    form_class = forms.PostForm
    success_url = '/posts/'


    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id = post_id)


    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form=form)

class PostDeleteView(generic.DeleteView):
    template_name = 'post_delete.html'
    success_url = '/posts/'
    def get_object(self,**kwargs):
        post_id = self.kwargs.get("id")
        return get_object_or_404(models.Post,id=post_id)


# def get_posts(request):
#     post = models.Post.objects.all()
#     return render(request, 'post_list.html', {'post': post})
#
#
# def post_detail(request, id):
#     try:
#         post = models.Post.objects.get(id=id)
#         try:
#             comment= models.Comment.objects.filter(post_id=id).order_by('created_date')
#         except models.Comment.DoesNotExist:
#             return HttpResponse("No Comments")
#     except models.Post.DoesNotExist:
#         raise Http404('Post does not exist')
#
#     return render(request, 'post_detail.html', {'post': post, 'post_comment': comment})
#
#
# def add_post(request):
#     method = request.method
#     if method == "POST":
#         form = forms.PostForm(request.POST, request.FILES)
#         print(form.data)
#         models.Post.objects.create(title=form.data['title'],
#                                    description=form.data['description'],
#                                    image=form.data['image'])
#         return HttpResponse('Post Created Successfully')
#     else:
#         form = forms.PostForm()
#
#     return render(request, 'add_post.html', {'form': form})
#
# def add_comment(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.CommentForm(request.POST, request.FILES)
#         print(form.data)
#         if form.is_valid():
#             form.save()
#             return  HttpResponse("Comment Created")
#     else:
#         form= forms.CommentForm()
#     return render(request, 'add_comment.html', {'form':form})
#
#
#
