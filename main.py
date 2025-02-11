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
        total_label.config(text="")
        return

    try:
        nota_plata = float(nota_plata_entry.get())
        procent_bacsis = float(procent_bacsis_entry.get())

        if nota_plata == 0 and procent_bacsis > 0:
            messagebox.showinfo("Eroare", "Nota de plată nu poate fi 0.")
            return

        if nota_plata == 0 and procent_bacsis == 0:
            messagebox.showinfo("Eroare", "Atât nota de plată cât și bacșișul nu pot fi 0.")
            return

        bacsis = nota_plata * (procent_bacsis / 100)
        total = nota_plata + bacsis

        if bacsis == 0:
            rezultat_label.config(text="Bacșișul este de 0 Ron.")
            total_label.config(text=f"Totalul notei este de {total:.2f} Ron.")
            bacsis_zero_label.place(relx=0.5, rely=0.5, anchor="s")
            bacsis_zero_label.tkraise()
            imagine_vizibila = True
        else:
            rezultat_label.config(text=f"Bacșișul este de {bacsis:.2f} Ron.")
            total_label.config(text=f"Totalul notei este de {total:.2f} Ron.")

    except ValueError:
        rezultat_label.config(text="Introdu date valide!")
        total_label.config(text="")

def resetare():
    global imagine_vizibila
    nota_plata_entry.delete(0, tk.END)
    procent_bacsis_entry.delete(0, tk.END)
    rezultat_label.config(text="")
    total_label.config(text="")
    if imagine_vizibila:
        bacsis_zero_label.place_forget()
        imagine_vizibila = False

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

tk.Label(content_frame, text="Procent bacșiș (%):", bg="lightblue").grid(row=1, column=0, padx=10, pady=10, sticky="e")
procent_bacsis_entry = tk.Entry(content_frame)
procent_bacsis_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Butonul "Calculează"
calculeaza_button = tk.Button(content_frame, text="Calculează", command=calculeaza_bacsis)
calculeaza_button.grid(row=2, column=0, columnspan=2, pady=20)

#Butonul "Resetare"
resetare_button = tk.Button(content_frame, text="Resetare", command=resetare)
resetare_button.grid(row=2, column=1, columnspan=2, pady=10)

# Eticheta de rezultat
rezultat_label = tk.Label(content_frame, text="", bg="lightblue", font=("Arial", 12, "bold"))
rezultat_label.grid(row=3, column=0, columnspan=2, pady=10)

# Eticheta pentru total
total_label = tk.Label(content_frame, text="", bg="lightblue", font=("Arial", 12, "bold"))
total_label.grid(row=4, column=0, columnspan=2, pady=10)

# Rularea aplicației
root.mainloop()

