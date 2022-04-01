#Party

wetter = input("Wochenendwetter - 'Sonnig' oder 'Regnerisch': ")

if wetter.upper() == "SONNIG":
    print("Gartenparty")
    print("GebmaVolgas")
elif wetter.lower() == "regnerisch":
    print("Kellerparty")
    print("Auch drinnen kanns rinnen")
else:
    print("bitte entweder 'Sonnig' oder 'Regnerisch' eingeben!")