import web


urls = (
  '/', 'index',
  '/login', 'login',
  '/upload', 'upload'
)


render = web.template.render('templates/')

class index:
	def GET(self):
		i = web.input(name=None)
		return render.index(i.name)

	def POST(self):
		data = web.data()
		print(data)
		return render.index('royluo')


class upload:
	def GET(self):
		return render.upload()

	def POST(self):
		x = web.input(myfile={})
		print(x.myfile.filename)
		print(x.myfile.value)
		raise web.seeother('/')


class login:
	def GET(self):
		return render.login()

	def POST(self):
		login = web.input()
		print(login.user)
		print(login.pwd)
		raise web.seeother('/')


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()