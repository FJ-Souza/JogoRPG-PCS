
class Character:

    def __init__(self, name, race, strength, dexterity, constitution, wisdom, intelligence, charisma, subbreed=None):
        self.name = name
        self.race = race
        self.subbreed = subbreed
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    def description_strength(self):
        if self.strength < 0:
            return "Força não definida."
        elif self.strength == 0:
            return "Incorpóreo"
        elif 1 <= self.strength <= 5:
            return "Incapaz"
        elif 6 <= self.strength <= 9:
            return "Fraco"
        elif 10 <= self.strength <= 11:
            return "Mediano"
        elif 12 <= self.strength <= 15:
            return "Forte"
        elif 16 <= self.strength <= 20:
            return "Super Poderoso"
        elif self.strength >= 21:
            return "Imbatível"
        
    def description_dexterity(self):
        if self.dexterity < 0:
            return "Força não definida."
        elif self.dexterity == 0:
            return "Desacordado"
        elif 1 <= self.dexterity <= 5:
            return "Abatido"
        elif 6 <= self.dexterity <= 9:
            return "Desajeitado"
        elif 10 <= self.dexterity <= 11:
            return "Regular"
        elif 12 <= self.dexterity <= 15:
            return "Agil"
        elif 16 <= self.dexterity <= 20:
            return "Ninja"
        elif self.dexterity >= 21:
            return "Imperceptível"
        
    def description_constitution(self):
        if self.constitution < 0:
            return "Força não definida."
        elif self.constitution == 0:
            return "Espectro"
        elif 1 <= self.constitution <= 5:
            return "Enfermo"
        elif 6 <= self.constitution <= 9:
            return "Frágil"
        elif 10 <= self.constitution <= 11:
            return "Saudável"
        elif 12 <= self.constitution <= 15:
            return "Durão"
        elif 16 <= self.constitution <= 20:
            return "Super Resistente"
        elif self.constitution >= 21:
            return "Imortal"
        

    def description_wisdom(self):
        if self.wisdom < 0:
            return "Força não definida."
        elif self.wisdom == 0:
            return "Inconsciente"
        elif 1 <= self.wisdom <= 5:
            return "Irracional"
        elif 6 <= self.wisdom <= 9:
            return "Desatento"
        elif 10 <= self.wisdom <= 11:
            return "Simples"
        elif 12 <= self.wisdom <= 15:
            return "Perspicaz"
        elif 16 <= self.wisdom <= 20:
            return "Filósofo"
        elif self.wisdom >= 21:
            return "Iluminado"
        
    
    def description_intelligence(self):
        if self.intelligence < 0:
            return "Força não definida."
        elif self.intelligence == 0:
            return "Inanimado"
        elif 1 <= self.intelligence <= 5:
            return "Incivilizado"
        elif 6 <= self.intelligence <= 9:
            return "Parvo"
        elif 10 <= self.intelligence <= 11:
            return "Mediocre"
        elif 12 <= self.intelligence <= 15:
            return "Estudado"
        elif 16 <= self.intelligence <= 20:
            return "Gênio"
        elif self.intelligence >= 21:
            return "Onisciente"

    def description_charisma(self):
        if self.charisma < 0:
            return "Força não definida."
        elif self.charisma == 0:
            return "Aberração"
        elif 1 <= self.charisma <= 5:
            return "Inexpressivo"
        elif 6 <= self.charisma <= 9:
            return "Rude"
        elif 10 <= self.charisma <= 11:
            return "Sociável"
        elif 12 <= self.charisma <= 15:
            return "Persuasivo"
        elif 16 <= self.charisma <= 20:
            return "Influente"
        elif self.charisma >= 21:
            return "Ídolo"