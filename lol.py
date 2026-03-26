class Pokemon:
    def __init__(self, entry, name, hp, attack, defense, types, description):
        self.entry = entry
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.types = types
        self.description = description
        
    def speak(self):
        print(self.name + "," + self.name + '!')
    
    def display_details(self):
        print("Entry number:\t" + str(self.entry))
        print("Name" + self.name)
        print(" Attack:", str(self.attack) )
        print("hp:", str(self.hp))
        print("defense :", str(self.defense))

        if len(self.types) == 1:
            print("Types:\t" + self.types[0])
        else:
            print("Types:", self.types[0] + "," + self.types[1])

    
        print("Description:" + self.description)

bulbasur = Pokemon(1, 'Bulbasur', 45, 49, 49, ['Grass, poison'], 'For some time after its birth,/' \
' it uses the nutrients that are packed into the seed on its back in order to grow.' )

ivysaur = Pokemon(2, 'Ivysaur', 60, 62, 63, ['Grass', 'Posion'], 'The more sunlight Ivysaur bathes in,/' \
' the more strength wells up within it, allowing the bud on its back to grow larger.')

venusaur = Pokemon(3, 'Venusaur', 80, 82, 83, ['Grass', 'Poison'], 'While it basks in the sun, /' \
'it can convert the light into energy. As a result, it is more powerful in the summertime.'  )

charmander = Pokemon(4, "Charmander", 39, 52, 43, "Fire", "The flame on its tail shows the strength of its/" \
" life-force. If Charmander is weak, the flame also burns weakly." )

charmeleon = Pokemon(5, "Charmeleon", 58, 64, 58, "Fire", "When it swings its burning tail,/" \
" the temperature around it rises higher and higher, tormenting its opponents."  )

charizard = Pokemon(6, "Charizard", 78, 84, 78, ["Fire", "Flying"], "If Charizard becomes truly angered, " \
"the flame at the tip of its tail burns in a light blue shade.")

squirtle = Pokemon(7, "Squirtle", 44, 48, 65, "Water", "After birth, " \
"its back swells and hardens into a shell. It sprays a potent foam from its mouth." )

wartortle = Pokemon(8, "Wartortle", 59, 63, 80, "Water", "Wartortle\'s long, furry tail is a symbol of longevity, so this Pokémon is quite popular among older people." ) 

blastoise = Pokemon(9, "Blastoise", 79, 83, 10, "Water", "It deliberately increases its body weight " \
"so it can withstand the recoil of the water jets it fires.")

pokedex = {'bulbasur': bulbasur,
           "ivysaur" : ivysaur,
           "venusaur" : venusaur,
           "charmander" : charmander,
           "charmeleon" : charmeleon,
           "charizard": charizard,
           "squirtle" : squirtle,
           "wartortle" : wartortle,
           "blastoise" : blastoise
           }
user_input = input("What Pokemon are tou looking for? : ").lower()

if user_input in pokedex:
    pokedex[user_input].display_details()
else:
    print("Pokemon not found")