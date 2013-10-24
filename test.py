import api.azapi

def test():
	artist = raw_input("Insert artist: ")
	title = raw_input("Insert title: ")
	
	api.azapi.generating(artist, title, save=True)
	
	
if __name__ == '__main__':
	test()

