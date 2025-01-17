Acesta este un program în Python folosind ca și biblioteci ”TKINTER” pentru interfața grafică și ”PIL” pentru introducerea și modificarea imaginilor.
Aplicația are ca și scop calcularea sumei bacșișului și totalul notei de plată pe baza unui procent introdus de utilizator.
Interfața grafică a fost creată printr-o fereastră principală care are dimensiunea de 600x400 pixeli.
Se poate adauga și o imagine de fundal care să acopere întreaga suprafață a ferestrei.
Ca și widget-uri, această aplicație are două câmpuri de intrare pentru a permite utilizatorului să introducă valoarea notei de plată și procentul bacșișului.
Există două label-uri pentru a ne asigura că utilizatorul introduce informațiile corect. 
Butonul ”Calculează” declanșează funcția de calcul folosită pentru calcularea bacșișului.
Butonul ”Resetează” șterge automat toate datele introduse de utilizator in câmpurile de intrare și label-urile de rezultate, readucând aplicația la starea inițială,
Iar în final avem două label-uri folosite pentru afișarea rezultatelor finale.
Bacșișul se calculează pe baza procentului introdus de către utilizator,dacă procentul este 0,se afișează o imagine și prin apăsarea butonului ”Calculează” câmpul de intrare pentru bacșiș este resetat pentru a se putea introduce din nou un procent valid.
În cazul în care procentul este valid, aplicația rulează fară întrerupere și v-a afișa suma bacșișului și totalul notei de plată.
Aplicația nu permite utilizatorului să introducă alte date, cum ar fi litere, cuvinte sau semne de punctuație. 
În cazul în care utilizatorul introduce aceste date, v-a fi afișat un mesaj de către aplicație prin care să atenționeze utilizatorul. 
Aplicația previne și calcularea pentru 0 printr-o verificare suplimentară. 
În cazul în care utilizatorul introduce valoarea 0 atât la nota de plată, cât și la bacșiș, se v-a afișa un mesaj de eroare pentru atenționarea utilizatorului. 
Un astfel de mesaj apare și în cazul în care valoarea introdusă la nota de plată este 0, dar la procent avem o valoare validă.
