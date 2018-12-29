from django.shortcuts import render
from .forms import PostingPost, FormJawab
from .models import Penanya
from django.http import HttpResponse
# Create your views here.

def index(request):
	penanya = Penanya.objects.all()
	postingan = PostingPost()

	context = {
		'judul' : 'Tanya Tanya',
		'deskripsi' : 'Platform zonabelajar untuk para siswa bertanya',
		'tagNavbar' : 'Menu Bertanya',
		'tagJumbotron' : 'TANYA TANYA',
		'deskJumbotron' : 'Silakan Bertanya! :)',
		'info_penanya'	: penanya,
		'data_postingan' : postingan,
	}

	if request.method == 'POST':

		Penanya.objects.create(
				nama = request.POST.get('nama'),
				kategoriPertanyaan = request.POST.get('kategori'),
				babPertanyaan = request.POST.get('bab'),
				pertanyaan = request.POST.get('pertanyaan')
			)

	return render(request,'penanya/index.html', context)

def detail(request, slugInput):

	postingan = Penanya.objects.get(slug = slugInput)

	context = {
		'judul' : 'Pertanyaan',
		'data_pertanyaan' : postingan,
		'tagJumbotron' : 'TANYA TANYA',

	}

	return render(request, 'penanya/detail.html', context)

def jawab(request):

	formJawaban = FormJawab()

	context = {
		'judul' : 'Selamat Menjawab',
		'heading' : 'Selamat Menjawab',
		'formJawaban' : formJawaban,

	}

	return render (request, 'penanya/jawab.html', context)