# proTask-modelling
Notes:
+ keine alternativen Arbeitsplätze berücksichtigt
+ keine Qualifikation bei Personen berücksichtigt (Klasse Person wird noch nicht verwendet)
+ Personen - kann es Arbeitsstationen geben bei denen keine Maschine verwendet wird, aber Personen nötig sind? -> könnte redundate Daten zu Personen auflösen
+ Activity -> wenn eine Activity immer eine fixe Zeiteinheit hat, die nötig ist, kann das redundante Speichern von Timesteps in Workplan entfernt werden, alternativ können Timesteps für die Sequenz verwendet werden, um parallele Vorgänge zu ermöglichen
+ falls eine Activity atomar genug ist um immer auf einem einzigen Arbeitsplatz durchgeführt zu werden, kann die Liste von Arbeitsplätzen in Activity für alternative Arbeitsplätze verwendet werden
+ Methoden/Funktionen sind im Diagramm noch ausgenommen, bisher nur beispielhafte Methoden wie in Recipe um den Abstieg durch alle Materialien zu demonstrieren
+ Information über Ergebnis Material ist in Rezept an sich redundant
+ Im Moment ist ein Material mit den Submaterialien in Material selbst abgebildet,
das sollte möglicherweise geändert werden wenn das Material alternativ aus anderen  Materialien hergestellt werden kann -> gleiche Funktionalität könnte auch über alternative Rezepte erreicht werden (kann vereinfacht werden falls es ein "Default" Rezept für jedes Material gibt)
![alt text](https://github.com/dhutter-fhv/proTask-modelling/blob/master/UML.png?raw=true)
