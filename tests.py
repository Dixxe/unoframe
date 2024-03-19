import unoframe

# test for card gen and field mechanic
'''
uno = unoframe.Uno(unoframe.Card(2, 'red'), True, 106, {})

uno.give_card(5, "Dixxe")

cards = uno.get_cards('Dixxe')

for card in cards:
    print(f"{card.color}, {card.number}")

print(uno.get_field().number)

test = input("Какую карту положишь? ")

uno.lay_card(cards[int(test)], 'Dixxe')

cards = uno.get_cards('Dixxe')
print("##########")
for card in cards:
    print(f"{card.color}, {card.number}")

print(uno.get_field().color)
'''
uno = unoframe.Uno(unoframe.Card(3, 'blue'), True, 20, {})

uno.give_card(6, "Dixxe")
uno.give_card(6, "Nixxie")
uno.give_card(6, "Bixxie")

while True:
    cards = uno.get_cards(uno.player_on_demand)
    i=-1
    for card in cards:
        i += 1
        try: print(f"{i}: {card.color}, {card.ability}")
        except Exception: print(f"{i}: {card.color}, {card.number}")

    print(f"*На поле лежит карта {uno.get_field().color} цвета и {uno.get_field().number} цифрой")

    test = input(f"Какую карту положишь, {uno.player_on_demand}? ")

    print(uno.lay_card(cards[int(test)], uno.player_on_demand))

