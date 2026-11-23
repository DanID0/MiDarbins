# Vai pēc četriem mērījumiem var noteikt pingvīna sugu?

Lēmumu koks pareizi noteica sugu **68 no 69** testa pingvīniem. Vienīgā kļūda bija `Chinstrap` pingvīns, kura knābja un pleznas garums novirzīja to uz zaru, kurā biežāk sastopama suga `Adelie`.

## Dati un tīrīšana

Palmer Station LTER pētnieki un Kristen Gorman no 2007. līdz 2009. gadam ievāca datus par pieaugušiem pingvīniem trīs Palmera arhipelāga salās Antarktikā. Projektā izmantots publiskais *palmerpenguins* CSV ar 344 rindām un astoņām kolonnām. Katra rinda apraksta vienu putnu. Prognozējamā kolonna ir `species`, un tās vērtības ir `Adelie`, `Chinstrap` un `Gentoo`. [Datu kopas apraksts](https://allisonhorst.github.io/palmerpenguins/)

Modelim vajadzīgs knābja garums un dziļums, pleznas garums un ķermeņa masa. Diviem putniem visu četru mērījumu vietā bija ierakstīts `NA`. Abas rindas izmetu, jo tajās nebija neviena mērījuma, uz kura balstīt prognozi. **No 344 rindām palika 342.** Citu iemeslu dēļ izmesto rindu skaits bija 0.

Dzimums nebija norādīts 11 putniem. Divi no tiem bija jau izmestie putni, bet pārējiem deviņiem bija visi vajadzīgie mērījumi, tāpēc tos saglabāju. Salu, gadu un dzimumu ievades kolonnās neiekļāvu, jo mērķis bija pārbaudīt, ko var secināt tikai no ķermeņa mērījumiem.

## Rezultāts pret bāzes līniju

Treniņam izmantoju 273 putnus un pārbaudei atliku 69. Biežākā suga treniņa datos bija `Adelie` (121 no 273). Tāpēc vienkāršākais minējums katram testa putnam ir `Adelie`.

| Paņēmiens | Pareizas atbildes testā | Precizitāte |
| --- | ---: | ---: |
| Vienmēr minēt `Adelie` | 30 no 69 | 43,48 % |
| Lēmumu koks ar četriem mērījumiem | 68 no 69 | 98,55 % |

Uz tiem pašiem 69 putniem koks deva **par 38 pareizām atbildēm vairāk**. Ieguvums šajā pārbaudē ir liels — 55,07 procentpunkti. Cits testa putnu sastāvs varētu dot citu rezultātu.

## Kuri mērījumi palīdzēja visvairāk?

| Kolonna | Svarīgums kokā | Ko rāda treniņa dati |
| --- | ---: | --- |
| `flipper_length_mm` (pleznas garums) | 55,2 % | `Gentoo` vidējais pleznas garums bija 216,9 mm, `Adelie` 190,0 mm un `Chinstrap` 196,6 mm. |
| `bill_length_mm` (knābja garums) | 36,5 % | `Chinstrap` knābis vidēji bija 49,0 mm garš, savukārt `Adelie` tikai 38,9 mm. |

Svarīguma rādītājs apraksta, cik liela daļa no kopējā sugu sajaukuma samazinājuma kokā panākta ar konkrētās kolonnas dalījumiem. Pleznas garums ir pirmais koka jautājums un palīdz nošķirt daudzus `Gentoo`. Starp putniem ar īsākām pleznām noder knābja garums. Abu mērījumu vieta saraksta augšgalā tāpēc šķiet loģiska.

## Viena kļūda soli pa solim

Faila `tirs.csv` **298. rindā**, skaitot virsrakstu kā pirmo rindu, ir šāds testa putns.

| Knābja garums | Knābja dziļums | Pleznas garums | Masa | Patiesā suga | Prognoze |
| ---: | ---: | ---: | ---: | --- | --- |
| 43,2 mm | 16,6 mm | 187 mm | 2900 g | `Chinstrap` | `Adelie` |

Pleznas garums 187 mm ir zem koka pirmās robežas 206,5 mm. Tālāk koks divreiz pārbauda knābja garumu. Putna 43,2 mm ietilpst intervālā virs 42,30 mm līdz 43,35 mm ieskaitot. Šajā gala grupā treniņa laikā nonāca pieci `Adelie` un trīs `Chinstrap` putni, tāpēc koks izvēlējās vairākuma sugu. Abām sugām šādi mērījumi pārklājas, un šī putna gadījumā vairākuma atbilde bija kļūdaina.

## Lietojuma robeža

Ar šo modeli nedrīkst automātiski piešķirt sugu katram pingvīnam pasaules savvaļas novērojumu datubāzē. Piemēram, arī imperatorpingvīnam tas piešķirtu vienu no trim apmācībā redzētajām sugām, jo modelim nav atbildes “cita suga”.

## Pašvērtējums

Izdevās izveidot atkārtojamu pārbaudi un izsekot vienai prognozei līdz konkrētam koka zaram.
Neizdevās pareizi atpazīt vienu `Chinstrap` pingvīnu, kuram mērījumi pārklājās ar `Adelie` mērījumiem.
Nākamreiz pārbaudītu modeli ar vairākiem treniņa un testa dalījumiem, lai redzētu, cik ļoti precizitāte ir atkarīga no izvēlētajiem testa putniem.
