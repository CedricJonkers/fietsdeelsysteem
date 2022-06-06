
# Werking

## 1) Het project runnen op de gewone manier.
***

- Eerst gaan het alle stations uitlezen.
- Vervolgens kan je kiezen of je de vorige configuratie wilt gebruiken of een nieuwe aan te maken(j/n).
> 1) kiest u j, dan leest het de opgeslagen json van gebruikers, fietstransporteurs en stations.

> 2) Het zet vervolgens de vorige configuratie terug. (de slots met de fietsen en de mensen die nog aan het fietsen zijn).
***
> 1) kiest u n, dan kan ge kiezen hoeveel gebruikers u wilt, de simulatie is toffer met een groot aantal mensen (bv. 5500).

> 2) Vervolgens kan u kiezen hoeveel fietstransporteurs u wilt (bv. 10).

> 3) Vervolgens verdelen de fietsttransporteurs een aantal fietsen(+/- 4000) over alle stations om random plaatsen.

> 4) Nadat ze hiermee klaar zijn kan je van start gaan.
***

* Er komt een eenvoudig keuze-menu tevoorschijn met een aantal opties.
![](img%5CCode_UQno9OgvkZ.png)

* Keuze 1 (Toon gebruikers): dit geeft de namen van al de gebruikers weer.
![](img%5CCode_CHUOJJU6Ua.png)

* Keuze 2 (Toon stations): dit geeft alle stations weer, met de info van de slots.
![](img%5CCode_kzIHqfB61S.png)

* Keuze 3 (check slots): in tegenstelling tot keuze 2 kan je hier de info van het station opzoeken via id (bv. 230830)
![](img%5CCode_QGoNDE2BPi.png)

* Keuze 4 (neem fiets): hierbij geef je de naam van de user mee, eerst achternaam en vervolgens voornaam, dit is hoofdlettergevoelig (bv. Philips Scott). Vervolgens geef je nog een station id mee (bv. 230830), de gebruiker ontgrendeld hiermee een fiets.
![](img%5CCode_y6Qb7eKXIo.png)

* Keuze 5 (voeg fiets toe): hierbij geef je terug een naam mee (bv. Philips Scott). Vervolgens geef je ook een station id mee (bv. 230829), de gebruiker heeft hiermee de fiets teruggebracht
![](img%5CCode_fU69oxwyFs.png)

* Keuze 6 (check fietsen): dit geeft een lijst terug met fietsen. Meer info hiervan (zie features).
![](img%5CCode_SXL9x5E0lW.png)

* Keuze 7 (verplaats fietsen): hiermee kan een fietstransporteur fietsen van een station naar een ander brengen. Meer info hiervan (zie featurs). Je geeft een fietstransporteur mee (bv. Hamlin Blanche)
![](img%5CCode_H5mckdU7Vy.png)

* Keuze 8 (generate html): hier zijn 4 opties.
![](img%5CCode_wCf6DcKz7o.png)
> 1. optie 1 (Fiets): hiermee kan u de status van een fiets opvragen (bv 4906).
![](img%5Cmsedge_VNFuwMc0op.png)
![](img%5Cmsedge_RY3Y7fEjfP.png)
> 2. optie 2 (Gebruiker): hiermee kan u de info + logs van de gebruiker zien (bv Philips Scott)
![](img%5Cmsedge_n7ckh5UhQR.png)
![](img%5Cmsedge_RY3Y7fEjfP.png)
> 3. optie 3 (Station): hiermee kan u de info voor een specifiek station vinden (bv 230829), de slots, de fietsen, en de logs.
![](img%5Cmsedge_Eol5C000mC.png)
![](img%5Cmsedge_oCsuEJhdhN.png)
![](img%5Cmsedge_DcmEGhpmhu.png)
> 4. optie 4 (Alles): dit is hetzelfde als optie 3, maar doet dit voor alle stations.
![](img%5Cmsedge_BJai2p8FwO.png)

* Keuze 9 (simulatie): het voert 10 seconden lang een simulatie uit, er worden fietsen genomen, teruggebracht. Dit omvat zowel gebruikers als fietstransporteurs.

* Keuze 10 (save and exit): dit slaagt alles op in nieuwe json files en worden ingelezen als je de volgende keer op bestaande configuratie accepteert.

## 2) Het project runnen met -s argument.
***
* als je een -s argument zet zal het ineens de simulatie runnen.

# features

## fietsen, en slots per station
***
* Per station wordt een lijst met slots bijgehouden, ook een lijst met fietsen.
* Wanneer een gebruiker een fiets neemt zal bij de slots de fiets weg zijn, maar in de lijst met fietsen zie je dat de gebruiker erbij staat. Vanaf dat de gebruiker zijn fiets bij een nieuw station brengt zal dit ook in de lijst worden getoond. Zo heb je steeds een beeld of een gebruiker een fiets heeft.
* vb. hier heeft Philips Scott de fiets met id 4915 genomen, we zien onderaan in de lijst van fietsen dat hij deze gebruikt. In de lijst met slots bezit slot 34 geen fiets meer. (foto 1)
* vb. als Philips Scott zijn fiets ergens terugbrengt zal dit in de lijst op niet in gebruik staat terug. (foto 2)
![](img%5CCode_YibJIZLrAr.png)
![](img%5CCode_IGW0xYjLAd.png)

## logging
***
* De logging tijdens het tonen van het project, buiten de simulatie:
![](img%5CCode_D8v8SaqCtT.png)

## html
***
* Het genereren van html werk en opent automatisch, buiten dat soms de eerste keer dat je het run de pagina moet sluiten en openen met live server. 

## simulatie
***
* Je kan de simulatie zo vaak mogelijk runnen als je wilt, er worden checks op alles gedaan zodat er geen errors zullen komen. (check of de gebruiker al een fiets heeft, check of het stations fietsen bevat, check of het station vol is,...), je kan de resultaten zien via het generaten van de html of in de logfile.

## fietstransporteurs werking
***
* Er wordt eerst gecheckt of er een station met teveel fietsen is (als het aantal fietsen groter is dan aantal slots*3/4)
* Vervolgens wordt er gecheckt of er een station met teweinig fietsen is als het aantal fietsen kleiner is dan aantal slots/3)
* als die allebei van toepassing is zet de fietstransporteur 1/3 van de fietsen in zijn wagen en verplaatst deze naar het station met teweinig fietsen.

# keuzes & moeilijkheden

* heb gekozen om de fietsen en slots zo per station op te slagen om zo steeds een beeld te krijgen over alle gebruikers die nog aan het fietsen zijn, de rest van de keuzes zijn uitgelegd in de features.
* moeilijkheden: het programma doet alles wat het moet doen, alle features zijn aanwezig. Toch is dit zeker niet op de meest propere manier gedaan. Dit vond ik toch wel moeilijk.

***
Jonkers Cédric

