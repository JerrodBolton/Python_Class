import tkinter as tk
from tkinter import ttk

# Function to display Pokémon information
def display_pokemon(pokemon):
    name = pokemon["name"]
    type_ = pokemon["type"]
    level = pokemon["level"]

    info_text = f"Name: {name}\nType: {type_}\nLevel: {level}"
    info_label.config(text=info_text)

# Function to handle button click event
def button_click():
    selected_pokemon = pokemon_listbox.get(tk.ACTIVE)
    display_pokemon(pokemon_data[selected_pokemon])

# Pokémon data
pokemon_data = {
    "Pikachu": {"name": "Pikachu", "type": "Electric", "level": 25},
    "Charizard": {"name": "Charizard", "type": "Fire/Flying", "level": 50},
    "Bulbasaur": {"name": "Bulbasaur", "type": "Grass/Poison", "level": 10},
}

# Create the main window
window = tk.Tk()
window.title("Pokédex")

# Create a frame for the listbox
listbox_frame = ttk.Frame(window, padding="10")
listbox_frame.pack()

# Create a label for the listbox
listbox_label = ttk.Label(listbox_frame, text="Select a Pokémon:")
listbox_label.pack()

# Create a listbox to display Pokémon names
pokemon_listbox = tk.Listbox(listbox_frame, width=20, height=10)
pokemon_listbox.pack()

# Add Pokémon names to the listbox
for pokemon in pokemon_data.values():
    pokemon_listbox.insert(tk.END, pokemon["name"])

# Create a frame for the information display
info_frame = ttk.Frame(window, padding="10")
info_frame.pack()

# Create a label to display Pokémon information
info_label = ttk.Label(info_frame, text="", font=("Arial", 12))
info_label.pack()

# Create a button frame
button_frame = ttk.Frame(window, padding="10")
button_frame.pack()

# Create a button to show selected Pokémon's information
button = ttk.Button(button_frame, text="Show Info", command=button_click)
button.pack()

# Set styles
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0")
style.configure("TButton", background="#ffd700", foreground="black", font=("Arial", 12, "bold"))
style.map("TButton", background=[("active", "#ffc500")])

# Start the main event loop
window.mainloop()
