import mysql.connector
cnx = mysql.connector.connect(user='Berzerk234', password='1111',
                              host='127.0.0.1',
                              database='calculator')
cnx.close()

print("Ноль в качестве знака операции завершит работу программы")
answer = float(0)
while True:

	s = input("Знак (+,-,*,/): ")
	if s == '0': break
	if s in ('+','-','*','/'):
		x = float(input("x="))
		y = float(input("y="))
		if s == '+':
			answer = x + y
			print("%.2f" % (answer))
		if s == '-':
			answer = x - y
			print("%.2f" % (answer))
		if s == '*':
			answer = x * y
			print("%.2f" % (answer))
		if s == '/':
			if y != 0:
				answer = x / y
				print("%.2f" % (answer))
			else:
				print("Деление на ноль!")
	else:
		print("Неверный знак операции!")