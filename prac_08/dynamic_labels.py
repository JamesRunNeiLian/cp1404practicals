from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Kivy App for dynamically creating labels from a list of names."""

    def build(self):
        """Build the Kivy app from the kv file."""
        # Sample list of names
        names = ["Alice", "Bob", "Charlie", "David"]
        # Load the kv file
        self.root = Builder.load_file('dynamic_labels.kv')

        return self.root