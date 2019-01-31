import diaspy

c = diaspy.connection.Connection(pod='https://spyurk.am', 
	username='', 
	password='')
c.login()
stream=diaspy.streams.Stream(c)

def post(text):
	stream.post(text)