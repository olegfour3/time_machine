import datetime

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.clock import Clock
from functools import partial
import pyperclip
from  kivy.uix.modalview import ModalView

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', False)
Config.set('kivy', 'window_icon', 'Time_Machine_26215.png')

started = False
hours = 0
minutes = 0
seconds = 0


class TimeMachine(App):
    def build(self):
        self.started = False
        self.days = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.title = 'TM'
        self.timer_event = None
        self.main_box = GridLayout(rows=2)
        inLayout = GridLayout(cols=3)
        self.lbl_timer = Label(text="00:00:00", font_size='70dp', font_name='arial.ttf')
        self.btn_start_stop = Button(text='START', font_size=20, font_name='arial.ttf')
        self.btn_reset = Button(text='RESET', font_size=20, font_name='arial.ttf')
        self.btn_copy = Button(text='COPY', font_size=20, font_name='arial.ttf')
        self.main_box.add_widget(self.lbl_timer)
        inLayout.add_widget(self.btn_start_stop)
        inLayout.add_widget(self.btn_reset)
        inLayout.add_widget(self.btn_copy)
        self.main_box.add_widget(inLayout)
        self.btn_start_stop.bind(on_press=self.start_stop)
        self.btn_reset.bind(on_press=self.reset)
        self.btn_copy.bind(on_press=self.copy_to_clipboard)

        return self.main_box

    def start_stop(self, button):
        if not self.started:
            button.text = 'PAUSE'
            self.timer_event = Clock.schedule_interval(partial(timer, self), 1)
        else:
            button.text = 'START'
            Clock.unschedule(self.timer_event)
        self.started = not self.started

    def reset(self, button):
        self.lbl_timer.text = "00:00:00"
        self.days = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0

    def copy_to_clipboard(self, button):
        time_str = f'{((self.days * 24 + self.hours) + (self.mins / 60 + self.secs / 60 / 60)):.2f} ч'
        pyperclip.copy(time_str)
        view = ModalView(size_hint=(0.6, 0.2))
        view.add_widget(Label(text='Copied to clipboard!'))
        view.open()


def timer(self, *_):
    time = datetime.time(self.hours, self.mins, self.secs)
    self.lbl_timer.text = f'{ ( str(self.days) + ". " ) if self.days > 0 else "" }{time}'
    if self.hours == 23 and self.mins == 59 and self.secs == 59:
        self.days += 1
        self.lbl_timer.font_size = '57dp'
        self.hours = 0
        self.mins = 0
        self.secs = -1
    if self.mins == 59 and self.secs == 59:
        self.hours += 1
        self.mins = 0
        self.secs = -1
    if self.secs == 59:
        self.mins += 1
        self.secs = -1

    self.secs += 1


if __name__ == '__main__':
    TimeMachine().run()

