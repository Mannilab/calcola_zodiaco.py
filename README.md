# calcola_zodiaco.py

Semplice esempio di script in Python per calcolare segno zodiacale ed ascendente in base alla propria data ed alla ora di nasvit - da inserire in progetti più elaborati. Oltre a quesze informazioni, viene chiesto anche, ai fini dell'ascendente, l'Utc. L'UTC (Coordinated Universal Time) è il fuso orario di riferimento da cui vengono calcolati tutti gli altri fusi orari del mondo. Per il calcolo dell'ascendente in astrologia, l'UTC è fondamentale perché:

1. L'orario di nascita deve essere convertito in UTC

L'orario di nascita fornito è spesso in ora locale.

Deve essere convertito in UTC sottraendo o aggiungendo il fuso orario della località di nascita.

Bisogna considerare l'eventuale ora legale in vigore al momento della nascita.


Ecco alcuni esempi di UTC per diverse città europee:

Orario Standard (senza ora legale)

Roma (Italia) → UTC+1

Parigi (Francia) → UTC+1

Madrid (Spagna) → UTC+1

Londra (Regno Unito) → UTC+0


Orario Estivo (con ora legale, solitamente da fine marzo a fine ottobre)

Roma (Italia) → UTC+2

Parigi (Francia) → UTC+2

Madrid (Spagna) → UTC+2

Londra (Regno Unito) → UTC+1


Se devi calcolare l'ascendente, devi verificare se l'ora di nascita rientrava nell'orario solare o nell'ora legale, perché questo cambia il valore di UTC da usare. 



