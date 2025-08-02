from nicegui import ui

def home():
    with ui.column().classes('w-full h-screen items-center justify-center'):
        ui.label('Bienvenue sur le gestionnaire de buget personnel')
        ui.label('Veuillez enregistrer votre nom afin de débuter.')
        nom = ui.input('Nom', placeholder='Sosane')
        navig = ui.button('Naviguer vers la page de budget', on_click=lambda: ui.navigate.to(f'/budget?nom={nom.value}'))
        navig.disable()

        def check_input():
            if nom.value:
                navig.enable()
            else:
                navig.disable()
                
        nom.on_value_change(check_input)