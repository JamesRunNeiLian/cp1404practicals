from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934  # Constant for conversion from miles to kilometres

class MilesConverterApp(App):
    """Kivy App for converting miles to kilometers."""
    output_km = StringProperty()  # StringProperty for automatic label update

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root