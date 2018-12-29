from django import forms

class PostingPost(forms.Form):
	#NAMA
	nama 	= forms.CharField(
				max_length=50,
				widget = forms.TextInput(
						attrs = {
							'placeholder' : 'Input Your Name'
						}
					)
				)
	#KATEGORI
	pilihan_kategori = ('matematika', 'fisika', 'kimia')
	kategori = forms.ChoiceField(
				choices=pilihan_kategori,
				widget=forms.Select()

			)
	#SUBBAB
	subbab = forms.CharField(
				max_length=50,
				widget=forms.TextInput(
						attrs = {
							'placeholder' : 'Bab'
						}
					)
				)
			


	pertanyaan = forms.CharField(
				max_length=350,
				widget = forms.Textarea(
						attrs = {
							'placeholder' : 'Silakan isi pertanyaan kamu'
						}
					)
			)


class FormJawab(forms.Form):

	nama 	= forms.CharField(
			max_length=50,
			widget=forms.TextInput(
					attrs = {
						'placeholder' 	: 'Masukkan Nama Kamu',
						'class'			: 'form-group form-control',

					}
				)

		)

	jawaban = forms.CharField(
			max_length=250,
			widget= forms.Textarea(
					attrs = {
						'placeholder' : 'Masukkan Jawaban',
						'class' : 'form-group form-control',
					}
				)	
		)