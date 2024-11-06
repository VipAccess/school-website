from http.client import HTTPResponse

from django.shortcuts import render, redirect
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
    #data = Publications.objects.all()
    return render(request, 'news.html')