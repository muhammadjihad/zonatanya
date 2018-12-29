from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, Bertanya

def index(request):

	login_form = LoginForm()
	formBertanya = Bertanya()

	context = {
		'judul' : 'zonatanya',
		'deskripsi' : 'Platform zonabelajar untuk para siswa bertanya',
		'tagNavbar' : 'Zona Tanya',
		'tagJumbotron' : 'Zona Tanya',
		'deskJumbotron' : 'Platform tanya jawab terbesar di indonesia',
		'loginform' : login_form,
		'formBertanya' : formBertanya,
	}
	
		

	return render (request, 'index.html', context)

