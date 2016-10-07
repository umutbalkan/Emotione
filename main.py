# icon.py

import pygtk, gtk, sys

class PyApp(gtk.Window):
	def __init__(self):
		super(PyApp, self).__init__()

		self.set_title("emotione")
		self.set_size_request(300, 175)
		self.set_position(gtk.WIN_POS_CENTER)


		self.fixed = gtk.Fixed()
		self.add(self.fixed)
		btn_analyse = gtk.Button("Analyse")


		self.fixed.put(btn_analyse, 50, 50)

		btn_analyse.set_tooltip_text(":)")

		try:
			self.set_icon_from_file("icon.png")
		except Exception, e:
			print e.message
			print "hello error"
			sys.exit(1)

		self.connect("destroy", gtk.main_quit)

		self.show_all()

PyApp()
gtk.main()