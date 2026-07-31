"""Greeter app using Kivy BoxLayout with greet and clear functionality."""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemoApp(App):
    """Main app class for the BoxLayout greeter demo."""

    def build(self):
        """Load and return the kv layout."""
        return Builder.load_file('box_layout.kv')

    def handle_greet(self):
        """Greet the user by name using the text input field."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Clear the text input field and the output label."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


if __name__ == '__main__':
    BoxLayoutDemoApp().run()