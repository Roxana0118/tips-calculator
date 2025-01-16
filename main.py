import tkinter as tk
from PIL import Image, ImageTk

from tkinter import messagebox

def calculeaza_bacsis():
    try:
        nota_plata = float(nota_plata_entry.get())
        procent_bacsis = float(procent_bacsis_entry.get())

        bacsis = (procent_bacsis / 100) * nota_plata
        total = nota_plata + bacsis

        rezultat_label.config(text=f"Bacsis: {bacsis:.2f} lei Total de plată: {total:.2f} Ron")
    except ValueError:
        messagebox.showerror("Eroare", "Te rog introdu valori valide.")



# Crearea ferestrei principale
root = tk.Tk()
root.title("Calculator Bacsis")

# Încarcăm imaginea de fundal
background_image = Image.open("euro.jpg")  # Înlocuiește cu calea imaginii tale
background_image = background_image.resize((300, 200), Image.Resampling.LANCZOS)  # Redimensionare imagine
bg_image = ImageTk.PhotoImage(background_image)

# Creăm un Label pentru fundal și îl plasăm
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)  # Setăm să ocupe întreaga fereastră

# Crearea și plasarea widget-urilor
tk.Label(root, text="Nota de plată totală (Ron):").grid(row=0, column=0, padx=10, pady=10)
nota_plata_entry = tk.Entry(root)
nota_plata_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Procent bacsis (%):").grid(row=1, column=0, padx=10, pady=10)
procent_bacsis_entry = tk.Entry(root)
procent_bacsis_entry.grid(row=1, column=1, padx=10, pady=10)

calculeaza_button = tk.Button(root, text="Calculează", command=calculeaza_bacsis)
calculeaza_button.grid(row=2, columnspan=2, pady=10)

rezultat_label = tk.Label(root, text="")
rezultat_label.grid(row=3, columnspan=2, pady=10)

# Rularea aplicației
root.mainloop()


