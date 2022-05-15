masrafe_mahe_baad = eval(input())
sahmie_qabli =eval(input())
liter_1500 =60+sahmie_qabli
liter_3000=liter_1500-masrafe_mahe_baad
if liter_3000>=0:
	print((liter_1500-liter_3000)*1500)
else:
		print(liter_1500*1500+abs(liter_3000)*3000)

		