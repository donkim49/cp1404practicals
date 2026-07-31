"""CP1404/CP5632 Practical - Miles to Kilometres converter Kivy app."""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_PER_MILE = 1.60934


class ConvertMilesKmApp(App):
    """Kivy app to convert miles to kilometres with up/down increment buttons."""

    output_text = StringProperty("0.0 km")

    def build(self):
        """Load and return the kv layout."""
        return Builder.load_file('convert_miles_km.kv')

    def convert(self, value):
        """Convert miles value to kilometres and update the output label.

        If value is invalid, set output to 0.0 km.
        """
        try:
            miles = float(value)
            km = miles * KM_PER_MILE
            self.output_text = f"{km:.2f} km"
        except ValueError:
            self.output_text = "0.0 km"

    def handle_increment(self, value, increment):
        """Increment the miles input by the given amount and convert.

        If value is invalid or empty, treat it as 0.
        """
        try:
            miles = float(value)
        except ValueError:
            miles = 0
        miles += increment
        self.root.ids.input_miles.text = str(miles)
        self.convert(miles)


if __name__ == '__main__':
    ConvertMilesKmApp().run()
