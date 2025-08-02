from nicegui import ui

# TODO: Refactoring

def budget(nom: str):
    ui.label(f'Bienvenue, {nom}!')
    ui.button('Retourner sur la page principale', on_click=ui.navigate.back)
    def update():
        revenue_p = echart_rev.options["series"][0]["data"]
        dep_p = echart_dep.options["series"][0]["data"]
        revenue_r = echart_rev.options["series"][1]["data"]
        dep_r = echart_dep.options["series"][1]["data"]

        rev_values_p = [
            salaire_p.value,
            allocation_p.value,
            pension_p.value,
            interet_p.value,
            autres_p.value,
        ]

        dep_values_p = [
            loyer_p.value,
            electricite_p.value,
            assurance_habitation_p.value,
            assurance_voiture_p.value,
            credit_voiture_p.value,
            mutuelle_p.value,
            internet_p.value,
            forfait_mobile_p.value,
            gym_p.value,
            abonnements_externe_p.value,
        ]

        rev_values_r = [
            salaire_r.value,
            allocation_r.value,
            pension_r.value,
            interet_r.value,
            autres_r.value,
        ]
        dep_values_r = [
            loyer_r.value,
            electricite_r.value,
            assurance_habitation_r.value,
            assurance_voiture_r.value,
            credit_voiture_r.value,
            mutuelle_r.value,
            internet_r.value,
            forfait_mobile_r.value,
            gym_r.value,
            abonnements_externe_r.value,
        ]

        for x in range(len(revenue_p)):
            revenue_p[x] = rev_values_p[x]
        for x in range(len(revenue_r)):
            revenue_r[x] = rev_values_r[x]
        for x in range(len(dep_p)):
            dep_p[x] = dep_values_p[x]
        for x in range(len(dep_r)):
            dep_r[x] = dep_values_r[x]

        echart_rev.update()
        echart_dep.update()

    with ui.row().classes("w-full justify-center items-center"):
        with ui.card():
            ui.label("Budget prévue")
            with ui.row():
                with ui.column():
                    ui.label("Revenus")
                    # Revenus
                    salaire_p = ui.input("Salaire", value=2400).props("clearable")
                    allocation_p = ui.input("Allocation", value=200).props("clearable")
                    pension_p = ui.input("Pension", value=500).props("clearable")
                    interet_p = ui.input("Intérêt", value=30).props("clearable")
                    autres_p = ui.input("Autres", value=0).props("clearable")

                with ui.column():
                    ui.label("Dépenses fixes")
                    # Dépenses fixes
                    loyer_p = ui.input("Loyer", value=850).props("clearable")
                    electricite_p = ui.input("Electricité", value=97).props("clearable")
                    assurance_habitation_p = ui.input(
                        "Assurance habitation", value=18
                    ).props("clearable")
                    assurance_voiture_p = ui.input("Assurance voiture", value=55).props(
                        "clearable"
                    )
                    credit_voiture_p = ui.input("Crédit voiture", value=90).props(
                        "clearable"
                    )
                    mutuelle_p = ui.input("Mutuelle", value=65).props("clearable")
                    internet_p = ui.input("Internet", value=35).props("clearable")
                    forfait_mobile_p = ui.input("Forfait mobile", value=15).props(
                        "clearable"
                    )
                    gym_p = ui.input("Gym", value=30).props("clearable")
                    abonnements_externe_p = ui.input(
                        "Abonnements externes", value=10.99
                    ).props("clearable")

        with ui.card():
            ui.label("Budget réelle")
            with ui.row():
                with ui.column():
                    ui.label("Revenus")
                    # Revenus
                    salaire_r = ui.input("Salaire", value=2400).props("clearable")
                    allocation_r = ui.input("Allocation", value=200).props("clearable")
                    pension_r = ui.input("Pension", value=500).props("clearable")
                    interet_r = ui.input("Intérêt", value=30).props("clearable")
                    autres_r = ui.input("Autres", value=0).props("clearable")

                with ui.column():
                    ui.label("Dépenses fixes")
                    # Dépenses fixes
                    loyer_r = ui.input("Loyer", value=850).props("clearable")
                    electricite_r = ui.input("Electricité", value=97).props("clearable")
                    assurance_habitation_r = ui.input(
                        "Assurance habitation", value=18
                    ).props("clearable")
                    assurance_voiture_r = ui.input("Assurance voiture", value=55).props(
                        "clearable"
                    )
                    credit_voiture_r = ui.input("Crédit voiture", value=90).props(
                        "clearable"
                    )
                    mutuelle_r = ui.input("Mutuelle", value=65).props("clearable")
                    internet_r = ui.input("Internet", value=35).props("clearable")
                    forfait_mobile_r = ui.input("Forfait mobile", value=15).props(
                        "clearable"
                    )
                    gym_r = ui.input("Gym", value=30).props("clearable")
                    abonnements_externe_r = ui.input(
                        "Abonnements externes", value=10.99
                    ).props("clearable")


    with ui.row().classes("w-full justify-center items-center"):
        ui.button("Confirmer le budget", on_click=update)

    echart_rev = ui.echart(
        {
            "tooltip": {"trigger": "item"},
            "xAxis": {"type": "value"},
            "yAxis": {
                "type": "category",
                "data": ["Salaire", "Allocation", "Pension", "Intérêt", "Autres"],
                "inverse": True,
            },
            "legend": {"textStyle": {"color": "gray"}},
            "series": [
                {
                    "type": "bar",
                    "name": "Revenus prévues",
                    "data": [
                        salaire_p.value,
                        allocation_p.value,
                        pension_p.value,
                        interet_p.value,
                        autres_p.value,
                    ],
                },
                {
                    "type": "bar",
                    "name": "Revenus réelles",
                    "data": [
                        salaire_r.value,
                        allocation_r.value,
                        pension_r.value,
                        interet_r.value,
                        autres_r.value,
                    ],
                },
            ],
        }
    )

    echart_dep = ui.echart(
        {
            "tooltip": {"trigger": "item"},
            "xAxis": {"type": "value"},
            "yAxis": {
                "type": "category",
                "data": [
                    "Loyer",
                    "Electricité",
                    "Assurance habitation",
                    "Assurance voiture",
                    "Crédit voiture",
                    "Mutuelle",
                    "Internet",
                    "Forfait mobile",
                    "Gym",
                    "Abonnements externes",
                ],
                "inverse": True,
            },
            "legend": {"textStyle": {"color": "gray"}},
            "series": [
                {
                    "type": "bar",
                    "name": "Dépenses prévues",
                    "data": [
                        loyer_p.value,
                        electricite_p.value,
                        assurance_habitation_p.value,
                        assurance_voiture_p.value,
                        credit_voiture_p.value,
                        mutuelle_p.value,
                        interet_p.value,
                        forfait_mobile_p.value,
                        gym_p.value,
                        abonnements_externe_p.value,
                    ],
                },
                {
                    "type": "bar",
                    "name": "Dépenses réelles",
                    "data": [
                        loyer_r.value,
                        electricite_r.value,
                        assurance_habitation_r.value,
                        assurance_voiture_r.value,
                        credit_voiture_r.value,
                        mutuelle_r.value,
                        interet_r.value,
                        forfait_mobile_r.value,
                        gym_r.value,
                        abonnements_externe_r.value,
                    ],
                },
            ],
        }
    )

    # TODO: Relier à update()
    dep_pie = ui.echart(
        {
            "title": {"text":"Diagramme circulaire de vos dépenses réelles","subtext":"Suivez-vous votre budget?","left":"center"},
            "tooltip": {"trigger": "item"},
            "legend": {"orient": "vertical", "left": "left", "textStyle": {"color": "gray"}},
            "series": [
                {
                    "type": "pie",
                    "name": "Dépenses réelles",
                    "radius": "65%",
                    "data": [
                        {"value": loyer_r.value, "name": loyer_r.label},
                        {"value": electricite_r.value, "name": electricite_r.label},
                        {"value": assurance_habitation_r.value, "name": assurance_habitation_r.label},
                        {"value": assurance_voiture_r.value, "name": assurance_voiture_r.label},
                        {"value": credit_voiture_r.value, "name": credit_voiture_r.label},
                        {"value": mutuelle_r.value, "name": mutuelle_r.label},
                        {"value": interet_r.value, "name": interet_r.label},
                        {"value": forfait_mobile_r.value, "name": forfait_mobile_r.label},
                        {"value": gym_r.value, "name": gym_r.label},
                        {"value": abonnements_externe_r.value, "name": abonnements_externe_r.label},
                    ],
                },
            ],
        }
    ).classes('w-full border').style("height: 456px")

