
import flet as ft


def main(page: ft.Page):
    page.title = "The Computer Inside Your Computer"
    page.padding = 0

    def create_window(title, items):
        window = ft.Container(
            width=450,
            height=300,
            bgcolor="#10182B",
            border_radius=15,
            padding=20,
            left=150,
            top=100,
            visible=False,
        )

        def close_window(e):
            window.visible = False
            page.update()

        window.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(title, size=22, color="white"),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color="white",
                            on_click=close_window,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(color="white"),
                *[ft.Text(item, color="white") for item in items],
            ]
        )

        return window

    files_window = create_window(
        "Files", ["Documents", "Pictures", "Downloads"]
    )

    youtube_window = create_window(
        "YouTube", ["search", "watch", "upload"]
    )

    google_window = create_window(
        "Google", ["search", "research", "upload"]
    )

    settings_window = create_window(
        "Settings", ["search", "background", "language"]
    )

    profile_window = create_window(
        "Profile", ["search", "visit", "upload"]
    )

    # CALCULATOR

    calculator_display = ft.Text(
        "0",
        size=32,
        color="white",
        text_align=ft.TextAlign.RIGHT,
    )

    first_number = None
    operation = None
    new_number = True

    secret_window = ft.Container(
        width=350,
        height=200,
        bgcolor="#241B42",
        border_radius=15,
        padding=20,
        left=400,
        top=150,
        visible=False,
        content=ft.Column(
            controls=[
                ft.Text("🔓 SECRET UNLOCKED!", size=25, color="yellow"),
                ft.Text("You found the hidden code!", color="white", size=16),
                ft.Button(
                    content="Close",
                    on_click=lambda e: close_secret(),
                ),
            ]
        ),
    )

    def close_secret():
        secret_window.visible = False
        page.update()

    def calculator_click(e):
        nonlocal first_number, operation, new_number

        value = e.control.data

        if value == "C":
            calculator_display.value = "0"
            first_number = None
            operation = None
            new_number = True

        elif value in ["+", "-", "×", "÷"]:
            if calculator_display.value == "Error":
                return

            first_number = float(calculator_display.value)
            operation = value
            new_number = True

        elif value == "=":
            if first_number is not None and operation is not None:
                second_number = float(calculator_display.value)

                if operation == "+":
                    result = first_number + second_number
                elif operation == "-":
                    result = first_number - second_number
                elif operation == "×":
                    result = first_number * second_number
                elif operation == "÷":
                    if second_number == 0:
                        calculator_display.value = "Error"
                        first_number = None
                        operation = None
                        new_number = True
                        page.update()
                        return

                    result = first_number / second_number

                calculator_display.value = str(round(result, 8))
                first_number = None
                operation = None
                new_number = True

        elif value == ".":
            if new_number or calculator_display.value == "Error":
                calculator_display.value = "0."
                new_number = False
            elif "." not in calculator_display.value:
                calculator_display.value += "."

        else:
            if new_number or calculator_display.value in ["0", "Error"]:
                calculator_display.value = value
                new_number = False
            else:
                calculator_display.value += value

        
        if calculator_display.value == "1408":
            desktop.image = ft.DecorationImage(
            src="win.jpg",
            fit=ft.BoxFit.COVER,
    )

        page.update()

    calculator_window = ft.Container(
        width=340,
        height=480,
        bgcolor="#10182B",
        border_radius=15,
        padding=20,
        left=150,
        top=100,
        visible=False,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Calculator", size=22, color="white"),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color="white",
                            on_click=lambda e: close_calculator(),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Divider(color="white"),

                ft.Container(
                    content=calculator_display,
                    alignment=ft.Alignment(1, 0),
                    padding=10,
                    bgcolor="#263451",
                    border_radius=8,
                    width=290,
                ),

                *[
                    ft.Row(
                        controls=[
                            ft.Button(
                                content=value,
                                data=value,
                                width=60,
                                height=50,
                                on_click=calculator_click,
                            )
                            for value in row
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )
                    for row in [
                        ["7", "8", "9", "÷"],
                        ["4", "5", "6", "×"],
                        ["1", "2", "3", "-"],
                        ["C", "0", ".", "+"],
                        ["="],
                    ]
                ],
            ],
            spacing=8,
        ),
    )

    def close_calculator():
        calculator_window.visible = False
        page.update()

    def open_window(window):
        window.visible = True
        page.update()

    def desktop_icon(icon, name, color, top, action=None):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(icon, size=45, color=color),
                    ft.Text(name, color="white"),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
            ),
            left=30,
            top=top,
            on_click=action,
        )

    desktop = ft.Container(
        expand=True,
        image=ft.DecorationImage(
            src="https://picsum.photos/id/1018/1600/900",
            fit=ft.BoxFit.COVER,
        ),
        content=ft.Stack(
            controls=[
                desktop_icon(
                    ft.Icons.FOLDER,
                    "Files",
                    "yellow",
                    30,
                    lambda e: open_window(files_window),
                ),

                desktop_icon(
                    ft.Icons.LANGUAGE,
                    "Google",
                    "blue",
                    130,
                    lambda e: open_window(google_window),
                ),

                desktop_icon(
                    ft.Icons.PLAY_ARROW,
                    "YouTube",
                    "red",
                    230,
                    lambda e: open_window(youtube_window),
                ),

                desktop_icon(
                    ft.Icons.SETTINGS,
                    "Settings",
                    "gray",
                    330,
                    lambda e: open_window(settings_window),
                ),

                desktop_icon(
                    ft.Icons.PERSON,
                    "Profile",
                    "black",
                    430,
                    lambda e: open_window(profile_window),
                ),

                desktop_icon(
                    ft.Icons.CALCULATE,
                    "Calculator",
                    "orange",
                    530,
                    lambda e: open_window(calculator_window),
                ),

                # PROFILE PICTURE
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            ft.CircleAvatar(
                                foreground_image_src="https://picsum.photos/id/237/200/300",
                                radius=25,
                            ),
                            ft.Container(
                                width=14,
                                height=14,
                                bgcolor=ft.Colors.GREEN,
                                border_radius=7,
                                right=0,
                                bottom=0,
                            ),
                        ],
                        width=50,
                        height=50,
                    ),
                    right=30,
                    top=30,
                ),

                files_window,
                youtube_window,
                google_window,
                settings_window,
                calculator_window,
                profile_window,
                secret_window,
            ],
            expand=True,
        ),
    )

    page.add(desktop)


ft.run(main, assets_dir="assets")