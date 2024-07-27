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

    def handle_calculate(self, text):
        """Handle calculation (could be button press or other call)."""
        print("Calculating kilometers")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        print("Incrementing/Decrementing miles")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)
        # TextInput on_text event will trigger handle_calculate

    def update_result(self, miles):
        """Update the output label with the converted value."""
        print("Updating result")
        self.output_km = str(miles * CONVERSION_FACTOR)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or return 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0

