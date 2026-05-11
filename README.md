# Tampere-talo-lähdekoodit

Tämä repositorio sisältää Python-skriptit työterveyskustannusdatan muuntamiseen, käsittelyyn ja visualisointiin.

Projektin tavoitteena on:
- muuntaa PDF-muotoinen lähtödata Exceliksi
- siistiä ja yhdistää data analyysiä varten
- muodostaa seloste- ja laboratoriokohtaisia yhteenvetoja
- tuottaa visualisointeja raportointia varten

## Kansiorakenne

Luo projektia varten ainakin seuraavat kansiot:

- `pdfs/` – vuoden PDF-tiedostot
- `excels/` – muunnetut ja jatkokäsitellyt Excel-tiedostot

## Työjärjestys

### 1. PDF -> Excel

Laita kaikki analysoitavan vuoden PDF-tiedostot kansioon `pdfs/`.

Aja:

pdfhandlingallfiles.py


Skripti muuntaa kaikki PDF-tiedostot yhdeksi Excel-tiedostoksi ja erottaa tiedot omille sheeteille PDF-tiedostojen mukaan.

Huom:
PDF-muunnoksen jälkeen Excel pitää tarkistaa ja siistiä käsin, koska dataan jää yleensä virheitä.

### 2. Selosteiden yhdistäminen
Aja:
```
seloste_adition.py
```
Tämä skripti yhdistää samat selosteet ja laskee niiden kustannussummat yhteen.

Tuloksena syntyy tiedosto tyyliin:
`selostesumma2025.xlsx`

Aja myös:
```
lkm_adition.py
```
Tämä skripti yhdistää samat selosteet ja laskee niiden Lkm-arvot yhteen.

Tuloksena syntyy tiedosto tyyliin:
`selostelkm2025.xlsx`

### 3. Visualisoinnit
Projektissa on erillisiä skriptejä visualisointeihin ja vertailuihin.

### Laboratoriot

- `labra_erikseen.py`
  Luo erilliset pylväsdiagrammit vuosille 2023, 2024 ja 2025

- `labra_summa.py`
  Vertaa laboratoriotutkimusten kustannuksia eri vuosina

- `labra_lkm.py`
  Vertaa laboratoriotutkimusten määriä eri vuosina

### Muut vertailut

- `monthly_comparisons.py`  
  Kuukausikohtaiset vertailut eri vuosien välillä

- `lkm_comparisons.py`  
  Käyttömäärien vertailu

- `not_labra_summa.py`   
  Muiden kuin laboratoriopalveluiden kustannusvertailu

- `not_labra_lkm.py`  
  Muiden kuin laboratoriopalveluiden määrien vertailu

- `09-autumn-service-usage.py`  
  Visualisoi syksyn (syyskuu–marraskuu) työterveyspalveluiden kustannusjakauman palvelukategorioittain eri vuosina.

- `10-autumn-top-services.py`  
  Visualisoi syksyn suurimmat yksittäiset palvelut ja vertailee niiden kustannuksia eri vuosien välillä.

## Tärkeää
Useimmissa skripteissä pitää muuttaa:

- Lähdetiedoston nimi
- Vuosiluku
- Tulostiedoston nimi

Tarkista aina skriptin kommentit ennen ajoa.

### Suositeltu käyttöjärjestys
- Luo pdfs/ ja excels/
- Lisää vuoden PDF:t kansioon pdfs/
- Aja pdfhandlingallfiles.py
- Siisti syntynyt Excel käsin
- Aja seloste_adition.py
- Aja lkm_adition.py
- Luo visualisoinnit tarvittavilla skripteillä
- Tuotokset
  
Projektin tuloksena syntyy:

- Yhdistettyjä Excel-tiedostoja
- Selostekohtaisia yhteenvetoja
- Määrien ja kustannusten vertailuja
- Laboratoriotutkimusten visualisointeja
- Laportointiin sopivia kuvaajia

## Huomio
Tämä ei ole täysin automaattinen järjestelmä.
PDF-muunnoksen jälkeen data vaatii yleensä käsin tehtävää tarkistusta ennen jatkoanalyysiä.
