password = "a123456"
passwordin = input("請輸入密碼，可嘗試次數3次")
X = 3
X = int(X)
if passwordin == password:
	print("歡迎回來")
else:
	X=X-1
	while 0 < X < 3:
		print("密碼錯誤，請重新輸入，可輸入次數為：",X)
		passwordin1 = input()
		if passwordin1 == password:
			print("歡迎回來")
			break
		else: 
			X=X-1	
	while X == 0:
		print("-----密碼錯誤3次-----限制進入-----")
		break