from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import ContentBlocks, Options, Publications, Colors

def news(request):
    data = Publications.objects.all()
    paginator = Paginator(data, 3)

    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'news.html', {"page_obj": data})

def page(request, slug):
    post = get_object_or_404(Publications, slug=slug)
    elements = ContentBlocks.objects.filter(page=post.page_id)

    data = list(map(test, elements))
    print(data)
    return render(request, 'page.html', {'elements': data, 'post': post})

def test(elem):
    result = dict()
    result['content'] = elem.content
    if elem.color is None:
        result['color'] = '#000000'
    else:
        result['color'] = Colors.objects.get(name=elem.color).code
    result['image'] = elem.image
    result['tag_open'] = []
    result['tag_close'] = []
    for el in elem.options.all():
        result.setdefault('tag_open', []).append(el.tag_open)
        result.setdefault('tag_close', []).insert(0, el.tag_close)
    return result