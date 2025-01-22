#importing all the needed libraries 
import requests
import json
import tkinter as tk
import random
from tkinter import Frame, Label
from PIL import Image, ImageTk 

# API URL 
url = "https://api.potterdb.com/v1/characters"

#Fetching data from the API
response = requests.get(url)

if response.status_code == 200:
    data = response.json() 

    # Removing null values from json file 
    for character in data["data"]:
        character_attributes = character["attributes"]
        # Creating a new file without the null values
        cleaned_attributes = {key: value for key, value in character_attributes.items() if value is not None}
        # upditing the attributes
        character["attributes"] = cleaned_attributes

    # saving the cleaned json file 
    with open("cleaned_characters.json", "w") as json_file:
        json.dump(data, json_file, indent=4)  

    print("Cleaned data saved to cleaned_characters.json")
else:
    print(f"Error fetching data: {response.status_code}")

# Loading the cleaned data
with open("cleaned_characters.json", "r") as json_file:
    characters_data = json.load(json_file)

# Frame Navigation
def show_frame(frame):
    main_page.place_forget()
    main_frame.place_forget()
    Instructions_frame.place_forget()
    Data_frame.place_forget()
    menu_frame.place_forget()
    frame.place(relwidth=1, relheight=1)

# Tkinter Setup
window = tk.Tk()
window.title("Wizard Finder")
window.geometry("642x407")
window.resizable(False, False)

# Frames
main_page = tk.Frame(window)
main_page.place(relwidth=1, relheight=1)

main_frame = Frame(window)
Instructions_frame = Frame(window)
Data_frame = Frame(window)
menu_frame = Frame(window)

# Main Page
img_main = Image.open(r'A2 - DDA\Images\main.png')  
resized_image_main = img_main.resize((642, 407))  
new_image_main = ImageTk.PhotoImage(resized_image_main) 

# Start button
Label(main_page, image=new_image_main).pack()
start_button = tk.Button(
    main_page,
    text="Start searching",
    font=('Bungee', 8),
    fg="white",
    bg="#00001B",
    borderwidth=0,
    activebackground="#00001B",
    command=lambda: show_frame(Data_frame)
)
start_button.place(x=260, y=182)

# Data Page
img_Data = Image.open("A2 - DDA\Images\Data.png")
resized_image_Data = img_Data.resize((642, 407))
new_image_Data = ImageTk.PhotoImage(resized_image_Data)

# Label for data replacing on the Data frame 
bg_label_data = Label(Data_frame, image=new_image_Data)
bg_label_data.image = new_image_Data 
bg_label_data.place(relwidth=1, relheight=1)  

def generate_data():
    # Clear previous widgets except for the background, menu button, and Generate button
    for widget in Data_frame.winfo_children():
        if widget not in [bg_label_data, menu_button, generate_button]:
            widget.destroy()

    # Generating random caharcters from the json file
    random_character = random.choice(characters_data["data"])
    character_attributes = random_character["attributes"]

    # getting characters details 
    name = character_attributes.get("name", "Unknown")
    born = character_attributes.get("born", "Unknown")
    gender = character_attributes.get("gender", "Unknown")
    species = character_attributes.get("species", "Unknown")
    house = character_attributes.get("house", "Unknown")
    wiki = character_attributes.get("wiki", "Unavailable")

    # Display character text details
    Label(Data_frame, text=f"Name: {name}", font=("Arial", 12, "bold"), bg="#0b1337", fg="white").pack(pady=(100, 10))
    Label(Data_frame, text=f"Born: {born}", font=("Arial", 10), bg="#0b1337", fg="white").pack(pady=(0, 10))
    Label(Data_frame, text=f"Gender: {gender}", font=("Arial", 10), bg="#0b1337", fg="white").pack(pady=(0, 10))
    Label(Data_frame, text=f"Species: {species}", font=("Arial", 10), bg="#0b1337", fg="white").pack(pady=(0, 10))
    Label(Data_frame, text=f"House: {house}", font=("Arial", 10), bg="#0b1337" , fg="white").pack(pady=(0, 10))
    Label(Data_frame, text=f"Wiki: {wiki}", font=("Arial", 10), fg="white", bg="#0b1337").pack(pady=(0, 20))


# Menu icons
menu_icon_img = Image.open("A2 - DDA\Images\Menu.png").resize((32, 32)) 
menu_icon = ImageTk.PhotoImage(menu_icon_img)

# Menu button
menu_button = tk.Button(
    Data_frame, image=menu_icon, bg="#000066", borderwidth=0 , activebackground="#000066",
    command=lambda: show_frame(menu_frame)
)
menu_button.place(x=10, y=10)  

# Generate button
generate_button = tk.Button(
    Data_frame,
    text="Generate Data",
    font=('Bungee', 6),
    fg="white",
    bg="#C396E5",
    borderwidth=0,
    activebackground="#C396E5",
    command=generate_data  # Generating data function 
)
generate_button.place(x=283, y=305)


# Menu page
img_menu = Image.open(r'A2 - DDA\Images\menuscreen.png')  
resized_image_menu = img_menu.resize((642, 407))  
new_image_menu = ImageTk.PhotoImage(resized_image_menu) 
Label(menu_frame, image=new_image_menu).pack()

close_icon_img = Image.open("A2 - DDA\Images\close.png").resize((22, 22)) 
close_icon = ImageTk.PhotoImage(close_icon_img)

back_button = tk.Button(
    menu_frame, image=close_icon, bg="#645a95", borderwidth=0 , activebackground="#645a95",
    command=lambda: show_frame(Data_frame)
)
back_button.place(x=10, y=10)  

# Home button
Label(menu_frame, image=new_image_menu).pack()
Home_button = tk.Button(
    menu_frame,
    text="Home",
    font=('Bungee', 12),
    fg="white",
    bg="#5f548d",
    borderwidth=0,
    activebackground="#5c5289",
    command=lambda: show_frame(main_page)
)
Home_button.place(x=20, y=45)

# Instructions button
Label(menu_frame, image=new_image_menu).pack()
Instructions_button = tk.Button(
    menu_frame,
    text="Instructions",
    font=('Bungee', 12),
    fg="white",
    bg="#5f548d",
    borderwidth=0,
    activebackground="#5c5289",
    command=lambda: show_frame(Instructions_frame)
)
Instructions_button.place(x=20, y=85)

# Exit button
Label(menu_frame, image=new_image_menu).pack()
Exit_button = tk.Button(
    menu_frame,
    text="Exit",
    font=('Bungee', 12),
    fg="white",
    bg="#5f548d",
    borderwidth=0,
    activebackground="#5c5289",
    command=window.destroy
)
Exit_button.place(x=20, y=125)

# Create Generate button
generate2_button = tk.Button(
    menu_frame,
    text="Generate Data",
    font=('Bungee', 6),
    fg="white",
    bg="#C396E5",
    borderwidth=0,
    activebackground="#C396E5",
)
generate2_button.place(x=283, y=305)

# Instructions page
img_Instructions = Image.open(r'A2 - DDA\Images\Instructions.png')  
resized_image_Instructions = img_Instructions.resize((642, 407))  
new_image_Instructions = ImageTk.PhotoImage(resized_image_Instructions) 
Label(Instructions_frame, image=new_image_Instructions).pack()

# Instructions heading
instructions_heading = Label(
    Instructions_frame,
    text="Instructions",
    font=("Bungee", 10, "bold"),  
    bg="#6C537F",
    fg="white"
)
instructions_heading.place(x=257, y=18)  

# instructions text
instructions_text = Label(
    Instructions_frame,
    text="Follow these instructions to explore the wizard app:\n\n" #/n for new line instructions
         "1. Explore the wizard database.\n"
         "2. Click on the generate data button to view details.\n"
         "3. Use the Go Back button to return to the main page.\n"
         "4. Use the menu to exit the app or go to the homepage.",
    font=("Bungee", 10), 
    bg="#6C537F",
    fg="white",
    justify="left"  
)
instructions_text.place(x=50, y=100)  

# Go back button
goBack_icon_img = Image.open("A2 - DDA\Images\Go Back.png").resize((22, 22)) 
goBack_icon = ImageTk.PhotoImage(goBack_icon_img)

go_back_button = tk.Button(
    Instructions_frame,
    image=goBack_icon,
    bg="#010418",
    borderwidth=0,
    activebackground="#010418",
    command=lambda: show_frame(Data_frame)  
)
go_back_button.place(x=10, y=10)

window.mainloop()
