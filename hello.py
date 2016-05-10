import web
import os
import time
import hashlib

web.config.debug = False
urls = (
	'/', 'Index',
  	'/login', 'Login',
  	'/upload', 'Upload',
  	'/reset', 'Reset'
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

	def GET(self):
		sess_id = web.cookies().get("roysite")
		if sess_id == None:
			return render.login()
		else:
			raise web.seeother('/')

	def POST(self):
		login = web.input()
		username = login.user
		password = login.passwd

		if username in account:
			if account[username] == password:
				session_id = hashlib.md5(password).hexdigest()
				session['roysite'] = session_id
				web.setcookie("roysite", session_id, 3600)
				raise web.seeother('/')
			else:
				raise web.seeother('/login')
		else:
			raise web.seeother('/login')


class Reset:
	def GET(self):
		session.kill()
		return "reset ok!"





if __name__ == "__main__":
	app.run()