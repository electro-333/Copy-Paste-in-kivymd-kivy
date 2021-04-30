from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.app import MDApp
from kivy.core.clipboard import Clipboard

KV = '''
ScreenManager:
	Clip:
<Clip>:
#:import Clipboard kivy.core.clipboard.Clipboard
	name:"clipb"
	MDFloatLayout:
		md_bg_color:[100/255,100/255,100/255,1]
		
		MDIconButton:
			icon:"content-copy"
			pos_hint:{"center_x":.4,"center_y":.3}
			
			
			################solution one############
			
			
			#on_press:Clipboard.copy(test.text)
			
			#########################################
			
			
			# solution two from the functions
			
			
			on_press : app.copy()
			
		MDIconButton:
			icon:"content-paste"
			pos_hint:{"center_x":.7,"center_y":.3}
			############# solution one ###############
			
			#on_release:test.text = Clipboard.paste()
			
			
			#########################################
			
			#solution two from the functions
			
			on_release : app.paste()
			
		MDTextField:
			id:test
			size_hint:.5,.2
			mode:"rectangle"
			pos_hint:{"center_x":.5,"center_y":.5}
			color_mode:'custom'
			line_color_focus:[0/255,0/255,0/255,1]
		
'''
class Clip(Screen):
	pass
sm = ScreenManager()
sm.add_widget(Clip(name = 'clipb'))

class Main(MDApp):
	def build(self):
		self.app1=Builder.load_string(KV)
		return self.app1
		
	def copy(self):
		text = self.app1.get_screen('clipb').ids.test.text
		Clipboard.copy(text)
		
	def paste(self):
		text = Clipboard.paste()
		self.app1.get_screen('clipb').ids.test.text = text
		
		
	
		
Main().run()
		
