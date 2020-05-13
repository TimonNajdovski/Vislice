import model

def izpis_igre(igra):
    tekst = (
        '===========================================\n'
        'Število preostalih poskusov: {stevilo_preostalih_poskusov} \n\n'
        '       {pravilni_del_gesla}\n\n'
        'Neuspeli poskusi: {neuspesni_poskusi}\n'
        '==========================================='
    ).format(
        stevilo_preostalih_poskusov = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla = igra.pravilni_del_gesla(),
        neuspesni_poskusi = igra.nepravilni_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        'Wipiiiii, zmaga! Geslo je bilo: {geslo}\n\n'
        'Potreboval si {n} poskusov.\n\n'
        'Želiš igrati še enkrat?'
    ).format(
        geslo = igra.pravilni_del_gesla(),
        n = igra.stevilo_napak
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        'Boooo, Poraz! Geslo je bilo: {geslo}\n\n'
        'Želiš igrati še enkrat?'
    ).format(
        geslo = igra.geslo
    )
    return tekst

def izpis_napake1():
    return '######## Ena črka naenkrat prosim ########'

def izpis_napake2():
    return '######## Dovoljene so samo črke ########'


def zahtevaj_vnos():
    return input('Črka = ')

def nova_igra_vnos():
    return input('Pritisni 1 za novo igro: ')

def pozeni_vmesnik():

    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        rezultat_ugiba = igra.ugibaj(poskus)

        if rezultat_ugiba == model.VEC_KOT_CRKA:
            print(izpis_napake1())
        if rezultat_ugiba == model.NI_CRKA:
            print(izpis_napake2())
        if rezultat_ugiba == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif rezultat_ugiba == model.PORAZ:
            print(izpis_poraza(igra))
            break
    if nova_igra_vnos() == 1:
        pozeni_vmesnik()
    else:
        return
pozeni_vmesnik()        