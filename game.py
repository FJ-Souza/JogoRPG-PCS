import random

class Game:

    def choose_race(self):
        print("Escolha sua raça:")
        print("1 - Anão")
        print("2 - Elfo")
        print("3 - Barbaro")
        print("4 - Humano")
        print("5 - Draconato")
        print("6 - Gnomo")
        print("7 - Ladrão")
        choice = input("Digite o número correspondente a sua escolha: ")
        if choice == "1":
            return self.choose_subbreed_dwarf()
        elif choice == "2":
            return self.choose_subbreed_elf()
        elif choice == "3":
            return self.choose_subbreed_barbaro()
        elif choice == "4":
            return "Humano"
        elif choice == "5":
            return "Draconato"
        elif choice == "6":
            return self.choose_subbreed_gnome()
        elif choice == "7":
            return "Ladrão"
        else:
            print("Opção inválida. por favor, escolha uma opção válida.")
            return self.choose_race()
        
    def choose_subbreed_dwarf(self):
        print("Escolha sua sub-raça:")
        print("1 - Anão da Colina")
        print("2 - Anão da montanha")
        print("3 - Continuar como Anão padrão")
        choice = input("Digite o número correspondente a sua escolha: ")
        if choice == "1":
            return "Anão da Colina"
        elif choice == "2":
            return "Anão da Montanha"
        elif choice == "3":
            return "Anão"
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            return self.choose_subbreed_dwarf()

    def choose_subbreed_elf(self):
        print("1 - Alto Elfo")
        print("2 - Elfo da Floresta")
        print("3 - Elfo Negro")
        print("4 - Continuar como Elfo padrão")
        choice = input("Digite o número correspondente a sua escolha: ")
        if choice == "1":
            return "Alto Elfo"
        elif choice == "2":
            return "Elfo da Floresta"
        elif choice == "3":
            return "Elfo Negro"
        elif choice == "4":
            return "Elfo"
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            return self.choose_subbreed_elf()

    def choose_subbreed_barbaro(self):
        print("1 - Pés Leves")
        print("2 - Robusto")
        print("3 - Continuar como Barbaro padrão")
        choice = input("Digite o número correspondente a sua choice: ")
        if choice == "1":
            return "Pés Leves"
        elif choice == "2":
            return "Robusto"
        elif choice == "3":
            return "Barbaro"
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            return self.choose_subbreed_barbaro()

    def choose_subbreed_gnome(self):
        print("1 - Gnomo da Floresta")
        print("2 - Gnomo da Pedra")
        print("3 - Continuar como Gnome padrão")
        choice = input("Digite o número correspondente a sua escolha: ")
        if choice == "1":
            return "Gnomo da Floresta"
        elif choice == "2":
            return "Gnomo da Pedra"
        elif choice == "3":
            return "Gnomo"
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            return self.choose_subbreed_gnome()
        
    def generator(self):
        return random.randint(0, 21)
    
#    def aplicar_bonus_forca(self, race):
#        bonus = 0
#        if race == "Human":
#            bonus == 1
#        elif race == "Dragonborn":
#            bonus == 2
#        elif race == "Mountain Dwarf":
#            bonus == 2

#    def aplicar_bonus_destreza(self, race, subbreed):
#       bonus = 0
#        if race == "Elf":
#            bonus == 2
#        elif race == "Barbaro":
#            bonus == 2
#        elif race == "Human":
#            bonus == 1

#        if subbreed == "Gnomo da Floresta":
#           bonus == 1

