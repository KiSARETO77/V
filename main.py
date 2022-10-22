import amino
#rom amino import Client
from ujson import load as W
for A in W(open("accounts.json")):
	E,P,D=A["email"],A["password"],A["device"]
	Ç=amino.Client(deviceId=D,proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
	Ç.login(E,P)
	L=Ç.get_from_code("http://aminoapps.com/c/anime-empire-1")
	O="59e378d4-1897-4e21-ab42-63861568727f"
	C=3434136
	print(f"Login To {E}")
	try:
		Ç.join_video_chat_as_viewer(comId=C,chatId=O)
		print("Ok")
	except Exception as F:
		print(F)
		pass
