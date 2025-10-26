defkullanici='xyz'
defparola='1234'

while(True):
	kullanici=input('Kullanici Adi:')
	parola=input('Parola:')
	if((kullanici==defkullanici)and(parola==defparola)):
		print('Hosgeldiniz ',kullanici)
		break
	elif((kullanici!=defkullanici)and(parola==defparola)):
		print('Kullanici Adinizi Yanlis Girdiniz')
	elif((kullanici==defkullanici)and(parola!=defparola)):
		print('Sifrenizi mi Unuttunuz?')
		print('Sifreyi Degistirmek Ister misiniz? (E/H)')
		cevap=input()
		if(cevap=='E'):
			yeniparola=input('Yeni Parolayi Giriniz:')
			print('Lutfen Bekleyiniz...')
			defparola=yeniparola
			print('Sifre Basariyla Degistirildi')
		else:
			print('Tekrar Deneyin')