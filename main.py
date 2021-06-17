import sys

import tkinter as tk
from tkinter import messagebox as msg
from loginPage import LoginPage

from settings import Settings
from appPage import AppPage

class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_menus()

		self.create_container()

		self.pages = {}
		self.create_appPage()
		self.create_appPage()
		self.create_loginPage()

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def create_loginPage(self):
		self.pages['loginPage'] = LoginPage(self.container, self)

	def create_menus(self):
		self.menuBar = tk.Menu(self)
		self.configure(menu=self.menuBar)

		self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
		self.fileMenu.add_command(label="New Contact")
		self.fileMenu.add_command(label="Open")
		self.fileMenu.add_command(label="Save")
		self.fileMenu.add_command(label="Exit", command=self.exit_program)

		self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
		self.helpMenu.add_command(label="About", command=self.show_about_info)

		self.menuBar.add_cascade(label="File", menu=self.fileMenu)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)


	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)


	def create_appPage(self):
		self.pages["appPage"] = AppPage(self.container, self.app)


	def show_about_info(self):
		msg.showinfo("About Contact App", "This apps created by\n1. Ria\n2. Nadya\n\nCopyright-2021"  "\nThis app will provide you more informations about variety of noodles such as stocks,expired dates, and so on and also this app can assist you to find noodles whatever you want. This app has the most complete information and up to date:). We hope you can utilize and enjoy this app." "\n**THANK YOU**")
		#msg.showwarning("About Contact App", "This apps created by\n1. Ali\n2. Budi\n\nCopyright-2021")
		#msg.showerror("About Contact App", "This apps created by\n1. Ali\n2. Budi\n\nCopyright-2021")



	def exit_program(self):
		respond = msg.askyesnocancel("Close Program", "Are you sure and really sure to close the program?")
		if respond:
			sys.exit()


		


class ContactApp:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	myContactApp = ContactApp()
	myContactApp.run()