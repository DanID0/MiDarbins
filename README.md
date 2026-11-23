# Pingvīna sugas prognozēšana

Vai pēc knābja garuma, knābja dziļuma, pleznas garuma un ķermeņa masas var atšķirt trīs pingvīnu sugas? Projekts tīra mērījumus, apmāca lēmumu koku un salīdzina tā atbildes ar vienkāršu minējumu. Iegūtie skaitļi un vienas kļūdas skaidrojums ir failā [rezultati.md](rezultati.md).

## Palaišana Windows vidē

Atver PowerShell projekta mapē. Projekts pārbaudīts ar Python 3.12. Ja šeit jau ir mape `.venv` ar uzstādītām bibliotēkām, vari uzreiz palaist abus skriptus.

Jaunā projekta kopijā vienreiz izveido virtuālo vidi un uzstādi bibliotēkas. `pandas` nolasa CSV un ļauj atlasīt tabulas rindas un kolonnas. `scikit-learn` sadala datus, apmāca koku un aprēķina precizitāti.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Palaid šīs divas komandas pēc kārtas.

```powershell
.\.venv\Scripts\python.exe 01_tirisana.py
.\.venv\Scripts\python.exe 02_modelis.py
```

Pirmais skripts no [avota CSV](dati/penguins.csv) izveido `tirs.csv` un izdrukā rindu skaitu. Otrais nolasa `tirs.csv` un terminālī parāda abus precizitātes rādītājus, divas svarīgākās kolonnas un pirmo kļūdaino testa prognozi. Datu izcelsme un licence ir failā [AVOTS.txt](dati/AVOTS.txt).

## Kā izsekot kodam

1. **Atlasīt kolonnas, tad rindas.** Funkcija `clean_penguins` vispirms atlasa sugu un četrus mērījumus. Tad `dropna()` izmet rindas ar tukšu vērtību kādā no šīm piecām kolonnām. Tādā veidā pingvīns ar nezināmu dzimumu joprojām der, ja tam ir visi četri mērījumi.
2. **Atdalīt jautājumu no atbildes.** `features` satur mērījumus, bet `species` satur zināmo sugu. `train_test_split` sadala abus kopā, lai katra atbilde paliktu pie pareizā putna. `stratify=species` saglabā aptuveni vienādas sugu proporcijas abās daļās. Fiksēts `random_state` ļauj atkārtot eksperimentu.
3. **Iemācīties nosacījumus.** Lēmumu koks darbojas kā secīgi `if` nosacījumi. Ar `fit` tas no treniņa piemēriem izvēlas mērījumus un robežvērtības, kas vislabāk sadala putnus grupās ar vienu dominējošo sugu. `max_depth=3` ierobežo vienas prognozes ceļu līdz trim jautājumiem. Ar `predict` koks piemēro šos nosacījumus testa mērījumiem.
4. **Pārbaudīt, vai mācīšanās palīdzēja.** `value_counts()` saskaita katras sugas treniņa piemērus, un `idxmax()` atgriež biežākās sugas nosaukumu. Bāzes līnija dod šo vienu atbildi par katru testa putnu. `accuracy_score` abos gadījumos aprēķina pareizo atbilžu daļu.
5. **Pārbaudīt vienu kļūdu.** Funkcijā `print_first_error` izteiksme `zip(...)` sapāro katru patieso testa sugu ar prognozi tajā pašā secībā. Pie pirmās nesakritības `loc[index]` atrod konkrētā putna mērījumus. Pēc izdrukātā rindas numura piemēru var atrast failā `tirs.csv`.
