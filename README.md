# proTask-modelling
Notes:
+ keine alternativen arbeitsplätze berücksichtigt
+ keine qualifikation bei personen berücksichtigt (Klasse Person wird noch nirgends verwendet)
+ personen - kann es arbeitsstationen geben bei denen keine maschine verwendet wird, aber personen nötig sind? -> könnte redundate daten zu personen auflösen
+ activity -> wenn eine activity immer eine fixe zeiteinheit hat, die nötig ist, kann das redundante speichern von timesteps in workplan entfernt werden, alternativ können timesteps für die sequenz verwendet werden, um parallele vorgänge zu ermöglichen
+ falls eine activity atomar genug ist um immer auf einem einzigen Arbeitsplatz durchgeführt zu werden, kann die Liste von arbeitsplätzen in Activity für alternative Arbeitsplätze verwendet werden
+ methoden/funktionen sind im Digramm noch ausgenommen, bisher nur beispielhafte methoden wie in Recipe um den Abstieg durch alle Materialien zu demonstrieren
+ information über ergebnis material ist in rezept an sich redundant
+ Im Moment ist ein Material mit den Submaterialien in Material selbst abgebildet,
das sollte möglicherweise geändert werden wenn das Material alternativ aus anderen  Materialien hergestellt werden kann -> gleiche funktionalität könnte auch über alternative rezepte erreicht werden (kann vereinfacht werden falls es ein "Default" Rezept für jedes material gibt)
![alt text](https://github.com/dhutter-fhv/proTask-modelling/blob/master/UML.png?raw=true)
