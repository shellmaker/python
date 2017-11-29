#!//usr/bin/python
search = 'AudaUpdate ended NORMAL'
MsgOk='UPDATE REALIZED'
MsgNok='NOT_UPDATED'
def check():
	datafile = file('TESTE_PYTHON.txt')
	for line in datafile:
		if search in line:
			found = True
			break
		else:
			found = False
	return found

if check():
    print MsgOk
else:
    print MsgNok
