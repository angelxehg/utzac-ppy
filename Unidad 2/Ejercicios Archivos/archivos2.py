from io import open
import pickle


class Character:

    def __init__(self, name, life, attack, defense, reach):
        self.name = name
        self.life = life
        self.attack = attack
        self.defense = defense
        self.reach = reach

    def __str__(self):
        return "{} => {} life, {} attack, {} defense, {} reach".format(
            self.name, self.life, self.attack, self.defense, self.reach)


class Manager:
    characters = []

    def __init__(self):
        self.load()

    def add(self, c: Character):
        for temp_c in self.characters:
            if temp_c.name == c.name:
                return
        self.characters.append(c)
        self.save()

    def remove(self, name):
        for temp_c in self.characters:
            if temp_c.name == name:
                self.characters.remove(temp_c)
                self.save()
                print("Character {} removed!".format(name))

    def show(self):
        if len(self.characters) == 0:
            print("Empty manager!")
            return
        for c in self.characters:
            print(c)

    def load(self):
        file = open('characters.pkg1', 'ab+')
        file.seek(0)
        try:
            self.characters = pickle.load(file)
        except:
            pass
        finally:
            file.close()
            print("Loaded {} characters".format(len(self.characters)))

    def save(self):
        file = open('characters.pkg1', 'wb')
        pickle.dump(self.characters, file)
        file.close()


G = Manager()
G.add(Character("Caballero", 4, 2, 4, 2))
G.add(Character("Guerrero", 2, 4, 2, 4))
G.add(Character("Arquero", 2, 4, 1, 8))
G.show()
G.remove("Arquero")
G.show()
