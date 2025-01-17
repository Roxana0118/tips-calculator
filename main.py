import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

imagine_vizibila = False

def calculeaza_bacsis():
    global imagine_vizibila

    # Dacă imaginea este vizibilă, o ascundem și resetăm câmpurile de intrare
    if imagine_vizibila:
        bacsis_zero_label.place_forget()
        imagine_vizibila = False
        procent_bacsis_entry.delete(0, tk.END)
        rezultat_label.config(text="")
        return

    try:
        nota_plata = float(nota_plata_entry.get())
        procent_bacsis = float(procent_bacsis_entry.get())
        bacsis = nota_plata * (procent_bacsis / 100)

        if bacsis == 0:
            rezultat_label.config(text="Bacșișul este 0 Ron.")
            bacsis_zero_label.place(relx=0.5, rely=0.5, anchor="s")
            bacsis_zero_label.tkraise()
            imagine_vizibila = True
        else:
            rezultat_label.config(text=f"Bacșișul este {bacsis:.2f} Ron.")

    except ValueError:
        rezultat_label.config(text="Introdu date valide!")

# Crearea ferestrei principale
root = tk.Tk()
root.title("Calculator Bacsis")

# Setarea dimensiunii ferestrei
root.geometry("600x400")  # Dimensiunea ferestrei: 600x400 pixeli

# Încarcăm imaginea de fundal
background_image = Image.open("euro.jpg")  # Înlocuiește cu calea imaginii tale
background_image = background_image.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensionare la dimensiunea ferestrei
bg_image = ImageTk.PhotoImage(background_image)

# Creăm un Label pentru fundal și îl plasăm
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)  # Setăm să ocupe întreaga fereastră

# Încarcăm imaginea pentru bacșișul 0
bacsis_zero_image = Image.open("saracie.jpg")  # Înlocuiește cu calea imaginii tale
bacsis_zero_image = bacsis_zero_image.resize((200, 200), Image.Resampling.LANCZOS)
bacsis_zero_photo = ImageTk.PhotoImage(bacsis_zero_image)

# Creăm un Label pentru imaginea de bacșiș 0
bacsis_zero_label = tk.Label(root, image=bacsis_zero_photo)

# Crearea unui frame pentru widget-uri, centrat
content_frame = tk.Frame(root, bg="lightblue")
content_frame.pack(expand=True)  # Centrarea frame-ului în fereastră

# Crearea și plasarea widget-urilor în frame
tk.Label(content_frame, text="Nota de plată totală (Ron):", bg="lightblue").grid(row=0, column=0, padx=10, pady=10, sticky="e")
nota_plata_entry = tk.Entry(content_frame)
nota_plata_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

tk.Label(content_frame, text="Procent bacsis (%):", bg="lightblue").grid(row=1, column=0, padx=10, pady=10, sticky="e")
procent_bacsis_entry = tk.Entry(content_frame)
procent_bacsis_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Butonul "Calculează"
calculeaza_button = tk.Button(content_frame, text="Calculează", command=calculeaza_bacsis)
calculeaza_button.grid(row=2, column=0, columnspan=2, pady=20)

# Eticheta de rezultat
rezultat_label = tk.Label(content_frame, text="", bg="lightblue", font=("Arial", 12, "bold"))
rezultat_label.grid(row=3, column=0, columnspan=2, pady=10)

# Rularea aplicației
root.mainloop()

