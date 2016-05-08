import web


urls = (
  '/', 'index',
  '/login', 'login'
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

class login:
	def GET(self):
		return render.login()

	def POST(self):
		raise web.seeother('/')


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()