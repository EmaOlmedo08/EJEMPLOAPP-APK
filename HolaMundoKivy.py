import kivy 
import kivy.app
import kivy.uix.label 

class FirstApp(kivy.app.App):
    def build(self):
        return kivy.uix.label.Label(text="Hola Mundo")
FirstApp().run()
