from nicegui import ui
from pages.budget_page import budget
from pages.home_page import home

def switchmode():
    with ui.header().classes('items-center justify-between'):
        current_mode = ui.dark_mode(value=True)
        ui.switch(on_change=current_mode.toggle)
        ui.markdown('#### Gestionnaire de Budget')

def footer():
    with ui.footer().classes('justify-center'):
        ui.label('© 2025 Gestionnaire de Budget')

@ui.page('/')
def go_to_home():
    switchmode()
    home()
    footer()

@ui.page('/budget')
def go_to_bugdet_page(nom: str):
    switchmode()
    budget(nom)
    footer()

ui.run()
