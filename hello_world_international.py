# Created by: Kay Lin
# Created on: 15-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-04
# This program displays Hello, World program, but with 3 buttons

import ui

def english_touch_up_inside(sender):
	#displays the English version
	view['hello_world_label'].text = ('Hello, World!')
	
def french_touch_up_inside(sender):
	#displays the French version
	view['hello_world_label'].text = ('Bonjour le monde!')
	
def spanish_touch_up_inside(sender):
	#displays the Spanish version
	view['hello_world_label'].text = ('Hola Mundo!')
				
view = ui.load_view()
view.present('sheet')
