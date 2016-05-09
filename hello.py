import web


urls = (
  '/', 'Index',
  '/login', 'Login',
  '/upload', 'Upload',
  '/cookie', 'Cookie'
)


render = web.template.render('templates/')

class Index:
	def GET(self):
		i = web.input(name=None)
		age = web.cookies().get('age')
		if None == age:
			print("cookie not exist")
		else:
			print(age)
		return render.index(i.name)

	def POST(self):
		data = web.data()
		print(data)
		return render.index('royluo')


class Upload:
	def GET(self):
		return render.upload()

	def POST(self):
		x = web.input(myfile={})
		filename = x.myfile.filename
		if 'myfile' in x:
			fout = open(filename,'w')
			fout.write(x.myfile.file.read())
			fout.close()
		raise web.seeother('/upload')


class Login:
	def GET(self):
		return render.login()

	def POST(self):
		login = web.input()
		print(login.user)
		print(login.pwd)
		raise web.seeother('/')


class Cookie:
	def GET(self):
		i = web.input(age='25')
		web.setcookie("age", i.age, 3600)
		return "Age set in your cookie"



if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()