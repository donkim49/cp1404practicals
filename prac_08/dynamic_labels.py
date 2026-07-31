"""Dynamic Labels app using Kivy - creates a Label widget for each name in a list."""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main app class for dynamically generating labels from a list of names."""

    def __init__(self, **kwargs):
        """Initialise the app with a list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Load and return the kv layout."""
        return Builder.load_file('dynamic_labels.kv')

    def on_start(self):
        """Dynamically create and add a Label widget for each name in the list."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == '__main__':
    DynamicLabelsApp().run()