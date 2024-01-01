from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, Clock
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.core.window import Window

Window.size = (800, 500)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '500')
Config.write()


class SpaceLayout(RelativeLayout):
    """space main layout"""
    space_width = NumericProperty()
    space_height = NumericProperty()

    def __init__(self, **kwargs):
        super(SpaceLayout, self).__init__(**kwargs)

        # Update the screen 60 times per second.
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        print(self.space_width)
        print(self.space_height)


class SpaceApp(App):
    pass


SpaceApp().run()
