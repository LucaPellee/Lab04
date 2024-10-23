import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self._dd_lingua = None
        self._dd_ricerca = None
        self._tf_testo = None
        self._btn_correzione = None
        self._lvOut = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        #ROW 1
        self._dd_lingua = ft.Dropdown(
            label="Lingua",
            options = [ft.dropdown.Option("italian"),
                       ft.dropdown.Option("english"),
                       ft.dropdown.Option("spanish")],
            width= 200,
            hint_text="Selezionare lingua del dizionario",
            on_change= self.__controller._leggiTendinaLingua
        )

        row1 = ft.Row([self._dd_lingua], alignment=ft.MainAxisAlignment.CENTER)
        #ROW 2
        self._dd_ricerca = ft.Dropdown(
            label = "Ricerca",
            options = [ft.dropdown.Option("Default"),
                       ft.dropdown.Option("Linear"),
                       ft.dropdown.Option("Dichotomic")],
            width = 200,
            hint_text="Selezionare il tipo di ricerca",
            on_change=self.__controller._leggiTendinaRicerca
        )

        self._tf_testo = ft.TextField(label = "Testo", width= 300)

        self._btn_correzione = ft.ElevatedButton(text = "Correggi",
                                                 on_click= self.__controller._handleSpellCheck)

        row2 = ft.Row([self._dd_ricerca, self._tf_testo, self._btn_correzione], alignment=ft.MainAxisAlignment.CENTER)
        #ROW 3
        self._lvOut = ft.ListView()

        row3 = ft.Row([self._lvOut], alignment=ft.MainAxisAlignment.CENTER)

        self.page.add(row1, row2, row3)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
