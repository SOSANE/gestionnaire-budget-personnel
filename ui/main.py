from nicegui import ui

ui.dark_mode(True)

with ui.row():
    with ui.card():
        ui.label('Budget prévue')
        with ui.row():
            with ui.column():
                ui.label('Revenus')
                # Revenus
                salaire = ui.input('Salaire', value=2400).props('clearable')
                allocation = ui.input('Allocation', value=200).props('clearable')
                pension = ui.input('Pension', value=500).props('clearable')
                interet = ui.input('Intérêt', value=30).props('clearable')
                autres = ui.input('Autres', value=0).props('clearable')

            with ui.column():
                ui.label('Dépenses fixes')
                # Dépenses fixes
                loyer = ui.input('Loyer', value=850).props('clearable')
                electricite = ui.input('Electricité', value=97).props('clearable')
                assurance_habitation = ui.input('Assurance habitation', value=18).props('clearable')
                assurance_voiture = ui.input('Assurance voiture', value=55).props('clearable')
                credit_voiture = ui.input('Crédit voiture', value=90).props('clearable')
                mutuelle = ui.input('Mutuelle', value=65).props('clearable')
                internet = ui.input('Internet', value=35).props('clearable')
                forfait_mobile = ui.input('Forfait mobile', value=15).props('clearable')
                gym = ui.input('Gym', value=30).props('clearable')
                abonnements_externe = ui.input('Abonnements externe', value=10.99).props('clearable')
        ui.button('Confirmer budget prévue', on_click=lambda: ui.label('Click!'))
    with ui.card():
        ui.label('Budget réelle')
        with ui.row():
            with ui.column():
                ui.label('Revenus')
                # Revenus
                salaire = ui.input('Salaire', value=2400).props('clearable')
                allocation = ui.input('Allocation', value=200).props('clearable')
                pension = ui.input('Pension', value=500).props('clearable')
                interet = ui.input('Intérêt', value=30).props('clearable')
                autres = ui.input('Autres', value=0).props('clearable')

            with ui.column():
                ui.label('Dépenses fixes')
                # Dépenses fixes
                loyer = ui.input('Loyer', value=850).props('clearable')
                electricite = ui.input('Electricité', value=97).props('clearable')
                assurance_habitation = ui.input('Assurance habitation', value=18).props('clearable')
                assurance_voiture = ui.input('Assurance voiture', value=55).props('clearable')
                credit_voiture = ui.input('Crédit voiture', value=90).props('clearable')
                mutuelle = ui.input('Mutuelle', value=65).props('clearable')
                internet = ui.input('Internet', value=35).props('clearable')
                forfait_mobile = ui.input('Forfait mobile', value=15).props('clearable')
                gym = ui.input('Gym', value=30).props('clearable')
                abonnements_externe = ui.input('Abonnements externe', value=10.99).props('clearable')
        ui.button('Confirmer budget réelle', on_click=lambda: ui.label('Click!'))


ui.run()