def calcola_segni_zodiacale_e_ascendente():
    # Richiede la data di nascita
    giorno = int(input("Inserisci il giorno di nascita: "))
    mese = int(input("Inserisci il mese di nascita (in numero): "))
    anno = int(input("Inserisci l'anno di nascita (in formato YYYY): "))

    # Calcola il segno zodiacale
    segni_zodiacali = ['Capricorno', 'Acquario', 'Pesci', 'Ariete', 
'Toro', 'Gemelli', 'Cancro', 'Leone', 'Vergine', 'Bilancia', 'Scorpione', 
'Sagittario']
    giorni_per_segni = [20, 19, 20, 20, 20, 21, 22, 23, 22, 22, 21, 21]
    segno_zodiacale = segni_zodiacali[mese-1] if (giorno < 
giorni_per_segni[mese-1]) else segni_zodiacali[mese % 12]

    # Calcola l'ascendente
    ore_di_nascita = int(input("Inserisci l'ora di nascita (in formato 
HH): "))
    minuti_di_nascita = int(input("Inserisci i minuti di nascita (in 
formato MM): "))
    ora_di_nascita = ore_di_nascita + minuti_di_nascita/60.0
    fuso_orario = int(input("Inserisci il fuso orario di nascita (espresso 
in ore rispetto all'UTC): "))
    ora_di_nascita = ora_di_nascita - fuso_orario

    if ora_di_nascita < 0:
        ora_di_nascita = ora_di_nascita + 24.0

    segni_ascendente = ['Ariete', 'Toro', 'Gemelli', 'Cancro', 'Leone', 
'Vergine', 'Bilancia', 'Scorpione', 'Sagittario', 'Capricorno', 
'Acquario', 'Pesci']
    gradi_per_segni = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
    ora_di_nascita = ora_di_nascita * 15.0
    segno_ascendente = segni_ascendente[int(ora_di_nascita / 30)]

    # Restituisce i risultati
    print("Il tuo segno zodiacale è:", segno_zodiacale)
    print("Il tuo ascendente è:", segno_ascendente)

# Esegue il programma
calcola_segni_zodiacale_e_ascendente()
