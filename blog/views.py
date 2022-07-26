
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from blog.forms import TagForm, PostForm
from blog.utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin

from blog.models import Post, Tag
from django.views.generic import View

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact = slug)
#     return render(request, 'blog/post_detail.html', {'post': post})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
        # post = Post.objects.get(slug__iexact = slug)

        # post =get_object_or_404(Post, slug__iexact = slug)
        # return render(request, 'blog/post_detail.html', {'post': post})
  



# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact = slug)
#     return render(request, 'blog/tag_detail.html', {'tag': tag})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


    # def get(self, request, slug):
        # tag = Tag.objects.get(slug__iexact = slug)

        # tag =get_object_or_404(Tag, slug__iexact = slug)
        # return render(request, 'blog/post_detail.html', {'tag': tag})
    

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html', {'form': form})

    # def post(self, request):
    #     bound_form = TagForm(request.POST)

    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', {'form': bound_form})

class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'


    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update.html', {'form': bound_form, 'tag': tag})

    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact = slug)
    #     bound_form = TagForm(request.POST, instance=tag)

    #     if bound_form.is_valid():
    #         updated_tag = bound_form.save()
    #         return redirect(updated_tag)
    #     return render(request, 'blog/tag_update.html', {'form': bound_form, 'tag': tag})

class TagDelete(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'blog/tag_delete.html', {'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tags_list_url'))



class PostUpdate(ObjectUpdateMixin, View):

    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'


    # def get(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     bound_form = PostForm(instance=post)
    #     return render(request, 'blog/post_update.html', {'form': bound_form, 'post': post})

    # def post(self, request, slug):
    #     post = Post.objects.get(slug__iexact = slug)
    #     bound_form = TagForm(request.POST, instance=post)

    #     if bound_form.is_valid():
    #         updated_post = bound_form.save()
    #         return redirect(updated_post)
    #     return render(request, 'blog/post_update.html', {'form': bound_form, 'post': post})


class PostCreate(View):
    form_model = TagForm
    template = 'blog/post_create.html'


    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create.html', {'form': form})

    # def post(self, request):
    #     bound_form = PostForm(request.POST)

    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create.html', {'form': bound_form})
