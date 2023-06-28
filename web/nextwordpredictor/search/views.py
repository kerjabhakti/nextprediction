from django.shortcuts import render
from django.db.models import Q
from predictorapp.models import Buku

def search(request):
    search = request.GET.get('q')
    books = Buku.objects.all()

    if search:
        books = books.filter(
			Q(judul_buku__icontains=search)
        )
    
    context = {
		"data": books,
        "search": search,
	}
    
    return render(request, 'index.html', context)