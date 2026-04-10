from tkinter import *
import os
class Pokemon:
    def __init__(self, entry, name, hp, attack, defense, types, description):
        self.entry = entry
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.types = types
        self.description = description
        
    
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

bulbasur = Pokemon(1, 'Bulbasur', 45, 49, 49, ['Grass', 'Poison'], 'For some time after its birth,/' \
' it uses the nutrients that are packed into the seed on its back in order to grow.' )

ivysaur = Pokemon(2, 'Ivysaur', 60, 62, 63, ['Grass', 'Poison'], 'The more sunlight Ivysaur bathes in,/' \
' the more strength wells up within it, allowing the bud on its back to grow larger.')

venusaur = Pokemon(3, 'Venusaur', 80, 82, 83, ['Grass', 'Poison'], 'While it basks in the sun, /' \
'it can convert the light into energy. As a result, it is more powerful in the summertime.'  )

charmander = Pokemon(4, "Charmander", 39, 52, 43, ["Fire"], "The flame on its tail shows the strength of its/" \
" life-force. If Charmander is weak, the flame also burns weakly." )

charmeleon = Pokemon(5, "Charmeleon", 58, 64, 58, ["Fire"], "When it swings its burning tail," \
" the temperature around it rises higher and higher, tormenting its opponents."  )

charizard = Pokemon(6, "Charizard", 78, 84, 78, ["Fire", "Flying"], "If Charizard becomes truly angered, " \
"the flame at the tip of its tail burns in a light blue shade.")

squirtle = Pokemon(7, "Squirtle", 44, 48, 65, ["Water"], "After birth, " \
"its back swells and hardens into a shell. It sprays a potent foam from its mouth." )

wartortle = Pokemon(8, "Wartortle", 59, 63, 80, ["Water"], "Wartortle\'s long, furry tail is a symbol of longevity, so this Pokémon is quite popular among older people." ) 

blastoise = Pokemon(9, "Blastoise", 79, 83, 10, ["Water"], "It deliberately increases its body weight " \
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

#colors
BG_DARK    = "#1a1a2e"
RED_MAIN   = "#c0392b"
RED_DARK   = "#922b21"
RED_LIGHT  = "#e74c3c"
SCREEN_BG  = "#1a3a1a"
SCREEN_TXT = "#39ff14"
HINGE      = "#555555"
PLASTIC    = "#2c2c2c"
WHITE      = "#f0f0f0"
YELLOW     = "#f1c40f"
BLUE_LED   = "#3498db"

#Welcome title






def search_pokemon():
    user_input = entry_box.get().strip().lower()

    if user_input in pokedex:
        pokemon = pokedex[user_input]

        entry_label.config(text=f"Entry number: {pokemon.entry}")
        name_label.config(text=f"Name: {pokemon.name}")
        hp_label.config(text=f"HP: {pokemon.hp}")
        attack_label.config(text=f"Attack: {pokemon.attack}")
        defense_label.config(text=f"Defense: {pokemon.defense}")
        types_label.config(text=f"Types: {', '.join(pokemon.types)}")
        description_label.config(text=f"Description: {pokemon.description}")

        if user_input in image_dictionary:
            image_label.config(image=image_dictionary[user_input])
            image_label.image = image_dictionary[user_input]
    else:
        entry_label.config(text="Entry number: N/A")
        name_label.config(text="Name: N/A")
        hp_label.config(text="HP: N/A")
        attack_label.config(text="Attack: N/A")
        defense_label.config(text="Defense: N/A")
        types_label.config(text="Types: N/A")
        description_label.config(text="Description: No Pokémon found with that name.")
        image_label.config(image="")

window = Tk()
window.title("Pokédex")
window.geometry("1000x1020")
window.config(bg="#2c2c2c")

#design
canvas = Canvas(window, width=1000, height=1020, bg="#2c2c2c", highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_rectangle(1, 1, 1020, 1000, fill="#9c1212", outline="")



#Title
main_frame = Frame(canvas, bg="#c21010")
canvas.create_window((0, 0), anchor="nw", window=main_frame,)
welcome_label = Label(main_frame, text = "Welcome to the Pokédex", font=("Times New Roman", 24, "bold"), bg="#2c2c2c", fg="white")
welcome_label.grid(row=0, column=0, columnspan=3, pady=2)

#Search box
search_prompt = Label(main_frame, text = "What Pokémon are you looking for?", font=("Times New Roman", 16), bg="#2c2c2c", fg="white")
search_prompt.grid(row=1, column=0, sticky="e", padx=10, pady=5)

entry_box = Entry(main_frame, width=30)
entry_box.grid(row=1, column=1, padx=10, pady=5)

search_button = Button(main_frame, text="Search", command=search_pokemon)
search_button.grid(row=1, column=2, padx=10, pady=5)

#info labels
entry_label = Label(main_frame, text = "Entry number: ", font=("Times New Roman", 14), bg="#2c2c2c", fg="white")
entry_label.grid(row=2, column=0, columnspan=3, sticky="w", padx=10, pady=5)

name_label = Label(main_frame, text = "Name: ", font=("Times New Roman", 14), bg="#2c2c2c", fg="white")
name_label.grid(row=3, column=0, columnspan=3, sticky="w", padx=10, pady=5)

hp_label = Label(main_frame, text = "HP: ", font=("Times New Roman", 14), bg="#2c2c2c", fg="white")
hp_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=10, pady=5)

attack_label = Label(main_frame, text = "Attack: ", font=("Times New Roman", 14), bg="#2c2c2c", fg="white")
attack_label.grid(row=5, column=0, columnspan=3, sticky="w", padx=10, pady=5)

defense_label = Label(main_frame, text = "Defense: ", font=("Times New Roman", 14), bg="#2c2c2c", fg="white")
defense_label.grid(row=6, column=0, columnspan=3, sticky="w", padx=10, pady=5)

types_label = Label(main_frame, text = "Types: ", font=("Times New Roman", 14), bg="#2c2c2c", fg="white")
types_label.grid(row=7, column=0, columnspan=3, sticky="w", padx=10, pady=5)

description_label = Label(main_frame, text = "Description: ", font=("Times New Roman", 14), bg="#2c2c2c", fg="white", wraplength=900, justify="left")
description_label.grid(row=8, column=0, columnspan=3, sticky="w", padx=10, pady=5)

#Image
image_label = Label(main_frame, bg="#2c2c2c")
image_label.grid(row=9, column=0, columnspan=3, pady=10)

def load_image(filename):
    base_path = os.path.dirname(__file__)
    return PhotoImage(file=os.path.join(base_path, filename))

charmander_img = load_image("004.png")
charmeleon_img = load_image("005.png")
charizard_img = load_image("006.png")

image_dictionary = {
    "charmander": charmander_img,
    "charmeleon": charmeleon_img,
    "charizard": charizard_img
}



window.mainloop()