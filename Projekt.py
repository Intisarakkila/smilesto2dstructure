from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox
from PIL import Image, ImageTk

def show_molecule():
    MO_Code = entry.get()
    Mol = Chem.MolFromSmiles(MO_Code)

    if Mol:
        img = Draw.MolToImage(Mol)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk
    else:
        messagebox.showerror("Fehler", "Ungültiger SMILES-Code!")

# GUI
root = Tk()
root.title("Molekül-Graphische-Darstellung")
root.geometry("500x400")

label = Label(root, text="SMILES-Code Hier:")
label.pack()

entry = Entry(root)
entry.pack()
button = Button(root, text="Molekül anzeigen", command=show_molecule)
button.pack()
panel = Label(root)
panel.pack()
root.mainloop()
