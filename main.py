from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView


class TaskItem(OneLineAvatarIconListItem):
    text = StringProperty()

    def __init__(self, task_text, delete_callback, **kwargs):
        super().__init__(**kwargs)
        self.text = task_text
        self.delete_callback = delete_callback

        self.right_icon = MDIconButton(icon="delete", on_release=self.delete_task)
        self.add_widget(self.right_icon)

    def delete_task(self, *args):
        self.delete_callback(self)


class ToDoApp(MDApp):
    def build(self):
        self.title = "To-Do List"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"

        self.screen = MDScreen()

        self.task_list = MDList()
        scroll = ScrollView()
        scroll.add_widget(self.task_list)
        self.screen.add_widget(scroll)

        self.add_task_button = MDFloatingActionButton(
            icon="plus",
            pos_hint={"center_x": 0.9, "center_y": 0.1},
            on_release=self.show_add_task_dialog,
        )
        self.screen.add_widget(self.add_task_button)

        return self.screen

    def show_add_task_dialog(self, *args):
        self.task_input = MDTextField(hint_text="Enter Task : ")
        self.dialog = MDDialog(
            title="Add",
            type="custom",
            content_cls=self.task_input,
            buttons=[
                MDIconButton(icon="check", on_release=self.add_task),
                MDIconButton(icon="close", on_release=self.close_dialog),
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def add_task(self, *args):
        task_text = self.task_input.text.strip()
        if task_text:
            item = TaskItem(task_text, delete_callback=self.remove_task)
            self.task_list.add_widget(item)
        self.close_dialog()

    def remove_task(self, task_widget):
        self.task_list.remove_widget(task_widget)


if __name__ == '__main__':
    ToDoApp().run()
