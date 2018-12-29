from django import forms

class LoginForm(forms.Form):

	username = forms.CharField(
			widget=forms.Textarea(
					attrs = {
						'placeholder' : 'Username'
					}
				),
		)
	password = forms.CharField()

	tahun = range(1950, 2018, 1)
	tanggal_lahir = forms.DateField(
				widget=forms.SelectDateWidget(
					years = tahun,
					attrs = {
						'class' : 'costum-select costum-select-sm'
					})
			)
	email = forms.EmailField()
	pilihan = (
			('P', 'Pria'),
			('W', 'Wanita'),
		)
	gender = forms.ChoiceField(
		choices=pilihan,
		widget=forms.RadioSelect
		)

class Bertanya(forms.Form):

	mata_pelajaran = forms.CharField(
			max_length=25,
			widget=forms.TextInput(
					attrs = {
						'placeholder' 	: 'Masukkan Kategori Mata Pelajaran',
						'class'			: 'form-group form-control',
					}
				)

		)

	bab				= forms.CharField(
			max_length=25,
			widget=forms.TextInput(
					attrs = {
						'placeholder'	: 'Masukkan Bab Kategori',
						'class'			: 'form-group form-control',

					}
				)
		)

	pertanyaan 		= forms.CharField(
			max_length=300,
			widget=forms.Textarea(
					attrs = {
						'placeholder' 	: 'Masukkan Pertanyaan',
						'class'			: 'form-group form-control',

					}
				)
		)

	foto_pertanyaan = forms.ImageField()