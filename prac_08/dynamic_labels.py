from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        # Define a list of names
        names = ["Alice", "Bob", "Charlie", "Diana"]

        # Create a BoxLayout to hold the Labels
        layout = BoxLayout(orientation='vertical')

        # Loop through the names and create a Label for each
        for name in names:
            label = Label(text=name, size_hint_y=None, height=40)
            layout.add_widget(label)

        return layout

if __name__ == '__main__':
    DynamicLabelsApp().run()
