import web
import os
import time
import hashlib

urls = (
  '/', 'Index',
  '/login', 'Login',
  '/upload', 'Upload',
  '/cookie', 'Cookie'
)

account = {"royluo":"123456"}


app = web.application(urls, globals())
render = web.template.render('templates/')
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store)


class Index:
	def GET(self):
		i = web.input(name=None)
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
	def _generate_session_id(self):
		session_id = 1
		return session_id

	def GET(self):
		print(self._generate_session_id())
		return render.login()

	def POST(self):
		login = web.input()
		username = login.user
		password = login.passwd

		if username in account:
			if account[username] == password:
				raise web.seeother('/')
			else:
				raise web.seeother('/login')
		else:
			raise web.seeother('/login')


class Cookie:
	def GET(self):
		i = web.input(age='25')
		web.setcookie("age", i.age, 3600)
		return "Age set in your cookie"



if __name__ == "__main__":
	app.run()