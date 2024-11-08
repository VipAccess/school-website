from django.shortcuts import render, redirect, get_object_or_404

from .models import ContentBlocks, Options, Publications, Colors


# from .forms import PageForm, ContentBlockForm
# from .models import Publications

def create_page(request):
    pass
    # if request.method == "POST":
    #     form = PageForm(request.POST)
    #     if form.is_valid():
    #         page = form.save()
    #         return redirect('edit_page', page_id=page.id)
    # else:
    #     form = PageForm()
    # return render(request, 'create_page.html', {'form': form})

def edit_page(request, page_id):
    pass
    # page = Publications.objects.get(id=page_id)
    # if request.method == "POST":
    #     block_form = ContentBlockForm(request.POST, request.FILES)
    #     if block_form.is_valid():
    #         content_block = block_form.save(commit=False)
    #         content_block.page = page
    #         content_block.save()
    #         return redirect('edit_page', page_id=page.id)
    # else:
    #     block_form = ContentBlockForm()
    #
    # content_blocks = page.content_blocks.all()
    # return render(request, 'edit_page.html', {
    #     'page': page,
    #     'block_form': block_form,
    #     'content_blocks': content_blocks,
    # })

def news(request):
    data = Publications.objects.all()
    return render(request, 'news.html', {'data': data})

def page(request, slug):
    post = get_object_or_404(Publications, slug=slug)
    elements = ContentBlocks.objects.filter(page=post.page_id)

    data = list(map(test, elements))
    return render(request, 'page.html', {'elements': data, 'post': post})

def test(elem):
    result = dict()
    result['type'] = elem.block_type
    result['content'] = elem.content
    result['color'] = Colors.objects.get(name=elem.color).code
    result['image'] = elem.image
    result['url'] = elem.url
    result['npp'] = elem.npp
    result['tag_open'] = []
    result['tag_close'] = []
    for el in elem.options.all():
        result.setdefault('tag_open', []).append(el.tag_open)
        result.setdefault('tag_close', []).insert(0, el.tag_close)
    return result