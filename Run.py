import os, requests
from SFInsta import insfaj as Gram

if __name__ == '__main__':
	try:os.mkdir('/sdcard/Ress')
	except:pass
	try:os.mkdir('Data')
	except:pass
	try:
		Gram.License()
	except requests.exceptions.ConnectionError:
		print('Connection Close')
