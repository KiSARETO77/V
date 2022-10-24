import amino
#rom amino import Client
from ujson import load as W
for A in W(open("accounts.json")):
	E,P,D=A["email"],A["password"],A["device"]
	Ç=amino.Client(deviceId=D,proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
	Ç.login(E,P)
	L=Ç.get_from_code("http://aminoapps.com/c/Dragon-ball-empire")
	O="0029e51c-6490-480c-9205-b70e262a16d1"
	C=64112096
	print(f"Login To {E}")
	try:
		Ç.join_video_chat_as_viewer(comId=C,chatId=O)
		print("Ok")
	except Exception as F:
		print(F)
		pass
