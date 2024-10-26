from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    korting=prijs*0.1
    tot_korting=prijs-korting
    uitvoer=f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {tot_korting} euro"
    return uitvoer
print(aanbieding_1("aardbei",4,0.1))

def inkomsten_totaal(inkomsten,btw):
    totaal=sum(inkomsten)
    bedrag_btW=totaal*btw
    uitvoer=f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag_btW} euro btw betaald dient te worden."
    return uitvoer
week_inkomsten=[220,430,125,160,205,90,345]
print(inkomsten_totaal(week_inkomsten,0.09))

def laag_en_hoog(mijn_lijst):
    hoogste_bedrag=max(mijn_lijst)
    laagste_bedrag=min(mijn_lijst)
    return[hoogste_bedrag,laagste_bedrag]
print(laag_en_hoog(week_inkomsten))

def gemiddelde(mijn_lijst):
    totaal=sum(mijn_lijst)
    gemid=totaal/len(mijn_lijst)
    uitvoer=f"De gemiddelde inkomsten deze week zijn {gemid} euro."
    return uitvoer
print(gemiddelde(week_inkomsten))

def meervoudig(invoer_lijst):
    tijdelijk=laag_en_hoog(invoer_lijst)
    return tijdelijk

invoer_lijst_1=[10,5,3,2,1,2,9]
print(meervoudig(invoer_lijst_1))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer