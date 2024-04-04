from character import Character
from game import Game

name_character = input("Digite o nome do seu personagem: ")

game = Game()
race_chosen = game.choose_race()
strength_character = game.generator()
dexterity_character = game.generator()
constitution_character = game.generator()
wisdom_character = game.generator()
intelligence_character = game.generator()
charisma_character = game.generator()

#Aplicar bonus
#bonus_strength = game.aplicar_bonus_strength(race_chosen)
#strength_character += bonus_strength

#bonus_dexterity = game.aplicar_bonus_dexterity(race_chosen)
#dexterity_character += bonus_dexterity

character = Character(name_character, race_chosen, strength_character, dexterity_character, constitution_character, wisdom_character,\
                        intelligence_character, charisma_character)

#if race_chosen == "Dwarf":
#    subbreed = game.chosen_subbreed_dwarf()
#    bonus_strength = game.aplicar_bonus_strength_dwarf(subbreed)
#    strength_character += bonus_strength

print("\nVocê criou um personagem chamado", character.name, "da raça", character.race)
if character.race == "Anão" and character.subbreed:
    print("Sub-raça:", character.subbreed)
elif character.race == "Elfo" and character.subbreed:
    print("Sub-raça:", character.subbreed)
elif character.race == "Barbaro" and character.subbreed:
    print("Sub-raça:", character.subbreed)
elif character.race == "Gnomo" and character.subbreed:
    print("Sub-raça:", character.subbreed)

print("Força:", character.strength)
print("Descrição da força:", character.description_strength())

print("\nDestreza:", character.dexterity)
print("Descrição da destreza:", character.description_dexterity())

print("\nConstituição:", character.constitution)
print("Descrição da constituição:", character.description_constitution())

print("\nSabedoria:", character.wisdom)
print("Descrição da sabedoria:", character.description_wisdom())

print("\nInteligencia:", character.intelligence)
print("Descrição da inteligencia:", character.description_intelligence())

print("\nCarisma:", character.charisma)
print("Descrição da carisma:", character.description_charisma())