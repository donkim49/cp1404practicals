"""Squaring app using Kivy - takes a number input and displays its square."""
from kivy.app import App


class SquaringApp(App):
    """Main app class for the number squaring program."""

    def handle_calculate(self, value):
        """Calculate the square of the given value and display the result.

        Args:
            value: The string value from the text input field.
        """
        try:
            number = int(value)
            result = number ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"


if __name__ == '__main__':
    SquaringApp().run()