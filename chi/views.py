from django.shortcuts import render, get_object_or_404
from .models import Post, FAQ, Useful, Contact


def index(request):
    posts = Post.objects.all().order_by('-search_count')
    context = {
        'posts': posts,
    }
    return render(request, "chi/index.html", context)


def faq(request):
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs
    }
    return render(request, 'chi/FAQ.html', context)


def useful(request):
    usefuls = Useful.objects.all()
    context = {
        'usefuls': usefuls
    }
    return render(request, 'chi/Useful_Information.html', context)


def contact(request):
    result1 = request.POST.get("result1", "")
    result2 = request.POST.get("result2", "")
    result3 = request.POST.get("result3", "")
    if result1 == "" or result2 == "" or result3 == "":
        a = 0
    elif result1 == "회사명" or result2 == "-를 포함하여 적어주세요" or result3 == "이름":
        a = 1
    else:
        Contact.objects.create(company=result1, tel=result2, writer=result3)

    return render(request, 'chi/Contact.html')


def search(request):
    if request.method == "POST":
        posts = Post.objects.all().order_by('-search_count')
        result = request.POST.get("result", "")
        results = posts.filter(search_s__icontains=result)
        if results.exists():
            for post in posts:
                if post.search_s == result:
                    post.search_count += 1
                    post.save()
                    stores = Post.objects.all().order_by('-update_at')
                    context = {
                        'stores': stores,
                        'posts': posts,
                    }
                    return render(request, 'chi/search.html', context)
        else:
            Post.objects.create(search_s=result)
            stores = Post.objects.all().order_by('-update_at')
            posts = Post.objects.all().order_by('-search_count')
            context = {
                'stores': stores,
                'posts': posts
            }
            return render(request, 'chi/search.html', context)
    else:
        stores = Post.objects.all().order_by('-update_at')
        posts = Post.objects.all().order_by('-search_count')
        context = {
            'stores': stores,
            'posts': posts
        }
        return render(request, 'chi/search.html', context)


def detail_faq(request, post_id):
    faq = get_object_or_404(FAQ, pk=post_id)
    return render(request, 'chi/detail.html', {'post': faq})


def detail_useful(request, post_id):
    useful = get_object_or_404(Useful, pk=post_id)
    return render(request, 'chi/detail.html', {'post': useful})