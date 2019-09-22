from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label

from kivy.properties import StringProperty


class DynamicNameWidgets(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["John", "Jack", "Jill", "Jane"]

    def build(self):
        Window.size = (500, 300)
        self.title = "Dynamic Name Widgets"
        self.root = Builder.load_file('dynamic_name_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entry_box.add_widget(temp_label)


DynamicNameWidgets().run()

