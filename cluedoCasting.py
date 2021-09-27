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

geslacht = input ('Bent u een man of een vrouw?: \n')
if geslacht in ['man', 'Man', 'MAN', 'een man']:
    geelen1 = True
    groenewoud1 = True
    pimpel1 = True
if geslacht in ['vrouw', 'VROUW', 'Vrouw', 'een vrouw']:
    dewi1t = True
    roodhart1 = True
    blaauw1 = True
lengte = int(input ('Hoe lang bent u? Rond af in hele getallen, in cm: \n'))
if lengte >= 185:
    geelen2 = True
    pimpel2 = True
if lengte < 185:
    dewit2 = True
    groenewoud2 = True
    roodhart2 = True
    blaauw2 = True

leeftijd = int(input)('Hoe oud bent u? \n')
if leeftijd in range (18,25):              
    roodhart3 = True
elif leeftijd in range (30,40):            
    blaauw3 = True
    geelen3 = True
elif leeftijd in range (41, 55):
    dewit3 = True
    groenewoud3 = True
elif leeftijd >= 60:
    pimpel3 = True


gewicht = int(input ('Hoeveel weegt u? Rond af in hele getallen, in kg: \n'))
if gewicht >= 90:
    groenewoud4 = True
    dewit4 = True
else:
    geelen4 = True
    roodhart4 = True
    pimpel4 = True
    blaauw4 = True

haarkleur = input ('Welke kleur is u haar? Geef 1 duidelijke kleur: \n')
if haarkleur in ['blond','Blond''Blonde''BLOND']:
    geelen5 = True
if haarkleur in ['grijs','Grijs''GRIJS']:
    groenewoud5 = True
    pimpel5 = True
    dewit5 = True
if haarkleur in ['bruin','Bruin''BRUIN' 'brunette' 'Brunette' 'BRUNETTE' 'donker bruin''Donker bruin' 'DONKER BRUIN']:
    shade = input ('Licht of donker?: \n')
    if shade in ['licht' , 'licht bruin' , 'Licht bruin' , 'LICHT BRUIN']:
        blaauw5 = True
    else:
        roodhart5 = True

snor = input ('Heeft u een snor?: \n')
if snor in ['ja', 'j', 'J' 'Ja' 'JA']:
    pimpel6 = True

aantrekkelijk = input ('Wordt u beschouwd als "conventially attractive"?: \n')
if aantrekkelijk in ['ja', 'j', 'J' 'Ja' 'JA']:
    blaauw6 = True
    roodhart6 = True

# DE REQUIREMENTS PER PERSOON:
# GEELEN        geslacht = man  lengte = 185    leeftijd = 30-40    gewicht = <90  haarkleur = blond
# DEWIT             vrouw       <185        41-55       >90     grijs
# GROENEWOUD    
# ROODHART
# PIMPEL
# BLAAUW

if 
auditieGeelen = True