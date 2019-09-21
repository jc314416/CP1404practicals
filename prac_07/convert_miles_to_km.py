from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKm(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.handle_input()
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        value = self.handle_input()
        value += increment
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def handle_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKm().run()
