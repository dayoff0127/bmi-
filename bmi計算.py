h = input('請輸入身高(cm)')
w = input('請輸入體重(kg)')
h = int(h)
w = int(w)
h = h/100
bmi = w / h / h

if bmi < 18.5 :
	print('你的bmi為', bmi, '過輕')
elif bmi >= 18.5 and bmi < 24 :
	print('你的bmi為', bmi, '正常')
elif bmi >= 24 and bmi < 27 :
	print('你的bmi為', bmi, '過重')
elif bmi >= 27 and bmi <30 :
	print('你的bmi為', bmi, '輕度肥胖')
elif bmi >= 30 and bmi <35 :
	print('你的bmi為', bmi, '中度肥胖')
else :
	print('你的bmi為', bmi, '重度肥胖')