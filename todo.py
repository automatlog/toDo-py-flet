import flet as ft

class Task(ft.UserControl):
    def build(self):
         return ft.Text(value='A task')

class ToDo(ft.UserControl):
    def build(self):
        self. input = ft. TextField (hint_text= 'What should be done?', expand=True)
        self. tasks = ft.Column()

        view = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text( value='ToDos', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.Row(
                     controls=[
                         self.input,
                        ft.FloatingActionButton(icon=ft.icons.ADD,on_click=self.add_clicked)
                    ]
                )
            ]
        )
        return view




def main (page: ft. Page):
    page.window_height = 600
    page.window_width = 400
    page. title = 'ToDo'

    todo = ToDo()
    page.add(todo)

ft.app(target=main)