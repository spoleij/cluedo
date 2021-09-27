# Steph Poleij
# 99033734

print ("Welkom bij Talent's Action.\nWij zoeken geschikte acteurs voor ons opkomende project, Cluedo!\nBeantwoord eerst de volgende vragen.")
naam = input ('Wat is uw naam?: \n')

#Verzin zelf onderscheidende criteria die je gebruikt op mensen wel of niet uit te nodigen voor een auditie voor één van de rollen.
#Verzin minimaal 2 criteria waaraan alle acteurs moeten voldoen. :
opleiding = int(input ('Hoeveel jaar heeft u gestudeerd in het theater?: \n'))
if opleiding >= 2:
    reqOpleiding = True

huilen= input ('Kunt u huilen op commando?: \n')
if huilen in ['ja', 'j', 'J' 'Ja' 'JA']:
    reqHuilen = True

#Per personage/rol in de film verzin je minimaal 3 criteria. 
#Denk aan lengte, gewicht, haarkleur, gender, leeftijd, persoonlijkheid, of iets anders.

lengte = int(input ('Hoe lang bent u? Rond af in hele getallen, in cm: \n'))
if lengte >= 185:
    geelen = True
    pimpel = True
if lengte < 185:
    dewit = True
    groenewoud = True
    roodhart = True
    Blaauw = True

leeftijd = int

gewicht = int(input ('Hoeveel weegt u? Rond af in hele getallen, in kg: \n'))
if gewicht >= 90:
    groenewoud = True
    dewit = True

haarkleur = input ('Welke kleur is u haar? Geef 1 duidelijke kleur: \n')
if haarkleur in ['blond','Blond''Blonde''BLOND']:
    geelen = True
if haarkleur in ['grijs','Grijs''GRIJS']:
    groenewoud = True
    pimpel = True
    dewit = True
if haarkleur in ['bruin','Bruin''BRUIN' 'brunette' 'Brunette' 'BRUNETTE' 'donker bruin''Donker bruin' 'DONKER BRUIN']:
    shade = input ('Licht of donker?: \n')
    if shade in ['licht' , 'licht bruin' , 'Licht bruin' , 'LICHT BRUIN']:
        Blaauw = True
    else:
        roodhart = True

snor = input ('Heeft u een snor?: \n')
if snor in ['ja', 'j', 'J' 'Ja' 'JA']:
    pimpel = True

aantrekkelijk = input ('Wordt u beschouwd als "conventially attractive"?: \n')
if aantrekkelijk in ['ja', 'j', 'J' 'Ja' 'JA']:
    Blaauw = True
    roodhart = True

# DE REQUIREMENTS PER PERSOON:
# GEELEN                            haarkleur = blond
# DEWIT
# GROENEWOUD
# ROODHART
# PIMPEL
# BLAAUW