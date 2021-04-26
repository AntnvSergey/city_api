# City_api

An app for providing information on geographic objects.

## Example usage
```
$ python api.py
 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
```
## GET information about the city by its geonameid

keys in dict is geonameid

```
$ curl http://127.0.0.1:8000/api/v1.0/1496747
{
    "1496747": {
        "name": "Novosibirsk",
        "asciiname": "Novosibirsk",
        "alternatenames": "Cen Ceper,Nobosimpirsk,Novasibirsk,Novo-Nikolaevsk,Novo-Nikolaievsk,Novo-Nikolaïevsk,Novonikolaevsk,Novonikolayevsk,Novosibir,Novosibir'sku,Novosibirs'k,Novosibirscum,Novosibirsk,Novosibirska,Novosibirskaj,Novosibirskas,Novosibirsko,Novosimpirsk,Novossibirsk,Novoszibirszk,Nowosibirsk,Nowosibirski,Nowosybirsk,OVB,Odsibiren' osh,Vil' Sibirkar,no wo sibiskh,nobosibileuseukeu,novosibirsk,novosibirska,novu~oshibirusuku,nwbwsybyrsq,nwfwsybyrsk,nwwsybrsk,nwwsybyrsk,xin xi bo li ya,Çĕн Çĕпĕр,Νοβοσιμπίρσκ,Νοβοσιμπιρσκ,Виль Сибиркар,Новасібірск,Новониколаевск,Новосибирск,Новосибирскай,Новосибирьскъ,Новосибірськ,Новосібір,Одсибирень ош,Նովոսիբիրսկ,נובוסיבירסק,نوفوسيبيرسك,نووسیبرسک,نووسیبیرسک,नोवोसिबिर्स्क,โนโวซีบีสค์,ნოვოსიბირსკი,ノヴォシビルスク,新西伯利亚,新西伯利亞,노보시비르스크",
        "latitude": "55.0415",
        "longitude": "82.9346",
        "feature class": "P",
        "feature code": "PPLA",
        "country code": "RU",
        "cc2": "",
        "admin1 code": "53",
        "admin2 code": "1496742",
        "admin3 code": "",
        "admin4 code": "",
        "population": "1419007",
        "elevation": "",
        "dem": "164",
        "timezone": "Asia/Novosibirsk",
        "modification date": "2019-09-05"
    }
}
```
## GET page with count of city

first argument - page, second - count of city on this page

```
$ http://127.0.0.1:8000/api/v1.0/pages/1/3
{
    "451747": {
        "name": "Zyabrikovo",
        "asciiname": "Zyabrikovo",
        "alternatenames": "",
        "latitude": "56.84665",
        "longitude": "34.7048",
        "feature class": "P",
        "feature code": "PPL",
        "country code": "RU",
        "cc2": "",
        "admin1 code": "77",
        "admin2 code": "",
        "admin3 code": "",
        "admin4 code": "",
        "population": "0",
        "elevation": "",
        "dem": "204",
        "timezone": "Europe/Moscow",
        "modification date": "2011-07-09"
    },
    "451748": {
        "name": "Znamenka",
        "asciiname": "Znamenka",
        "alternatenames": "",
        "latitude": "56.74087",
        "longitude": "34.02323",
        "feature class": "P",
        "feature code": "PPL",
        "country code": "RU",
        "cc2": "",
        "admin1 code": "77",
        "admin2 code": "",
        "admin3 code": "",
        "admin4 code": "",
        "population": "0",
        "elevation": "",
        "dem": "215",
        "timezone": "Europe/Moscow",
        "modification date": "2011-07-09"
    },
    "451749": {
        "name": "Zhukovo",
        "asciiname": "Zhukovo",
        "alternatenames": "",
        "latitude": "57.26429",
        "longitude": "34.20956",
        "feature class": "P",
        "feature code": "PPL",
        "country code": "RU",
        "cc2": "",
        "admin1 code": "77",
        "admin2 code": "",
        "admin3 code": "",
        "admin4 code": "",
        "population": "0",
        "elevation": "",
        "dem": "237",
        "timezone": "Europe/Moscow",
        "modification date": "2011-07-09"
    }
}
```
## GET cities by name

The city to the north is displayed first

```
$ curl http://127.0.0.1:8000/api/v1.0/city/Москва/Санкт-Петербург
{
    "498817": {
        "name": "Saint Petersburg",
        "asciiname": "Saint Petersburg",
        "alternatenames": "Agia Petroupole,Betuyrbukh,Cankt-Peterburg,LED,Leningrad,Leningrado,Lungsod ng Sankt-Peterburg,Peterburg,Peterburgo,Peterburi,Petersburg,Petrapilis,Petrograd,Petrogrado,Petrohrad,Petropolis,Petursborg,Pietari,Piiteri,Piter,Pétursborg,SPb,Saint Petersbourg,Saint Petersburg,Saint Pétersbourg,Saint-Petersbourg,Saint-Pétersbourg,San Petersburgo,San Pietroburgo,San Pietruburgu,Sankt Peitersbuerg,Sankt Peterburg,Sankt Peterburgas,Sankt Petersborg,Sankt Petersburg,Sankt Peterzburg,Sankt Péitersbuerg,Sankt-Peterburg,Sankt-Peterburgo,Sankt-Peterburq,Sankt-Petersburg,Sankti Petursborg,Sankti Pétursborg,Sanktpeterburga,Sanktpēterburga,Sant Petersburg,Sant Petersburgo,Sant-Petersbourg,Santa Peterburg,Sao Petersburgo,Sint Petersbork,Sint-Petersburg,St Petersburg,St. Petersburg,St.-Petersburg,Szentpetervar,Szentpétervár,São Petersburgo,leningeuladeu,sangteupeteleubuleukeu,sankt. peterburg,sankutopeteruburuku,sant btrsbrgh,seinteupiteojeubeogeu,sent pi te xrs beirk,senta pitarsabarga,sheng bi de bao,sn ptrzbwrg,snqt ptrbwrg,Αγία Πετρούπολη,Бетъырбух,Ленинград,Петербург,Петроград,Питер,СПб,Санкт Петербург,Санкт Петерзбург,Санкт-Петербург,Սանկտ Պետերբուրգ,סנקט פטרבורג,سانت بطرسبرغ,سن پترزبورگ,সেন্ট পিটার্সবার্গ,เซนต์ปีเตอร์สเบิร์ก,სანკტ-პეტერბურგი,სანქტ-პეტერბურგი,サンクトペテルブルク,圣彼得堡,레닌그라드,상트페테르부르크,세인트피터즈버그",
        "latitude": "59.93863",
        "longitude": "30.31413",
        "feature class": "P",
        "feature code": "PPLA",
        "country code": "RU",
        "cc2": "",
        "admin1 code": "66",
        "admin2 code": "",
        "admin3 code": "",
        "admin4 code": "",
        "population": "5028000",
        "elevation": "",
        "dem": "11",
        "timezone": "Europe/Moscow",
        "modification date": "2020-09-02"
    },
    "524901": {
        "name": "Moscow",
        "asciiname": "Moscow",
        "alternatenames": "MOW,Maeskuy,Maskav,Maskava,Maskva,Mat-xco-va,Matxcova,Matxcơva,Mosca,Moscfa,Moscha,Mosco,Moscou,Moscova,Moscovo,Moscow,Moscoƿ,Moscu,Moscua,Moscòu,Moscó,Moscù,Moscú,Moskva,Moska,Moskau,Mosko,Moskokh,Moskou,Moskov,Moskova,Moskovu,Moskow,Moskowa,Mosku,Moskuas,Moskva,Moskvo,Moskwa,Moszkva,Muskav,Musko,Mát-xcơ-va,Mòskwa,Məskeu,Məskəү,masko,maskw,mo si ke,moseukeuba,mosko,mosukuwa,mskw,mwskva,mwskw,mwsqbh,mx s ko,Μόσχα,Мæскуы,Маскав,Масква,Москва,Москова,Москох,Москъва,Мускав,Муско,Мәскеу,Мәскәү,Մոսկվա,מאָסקװע,מאסקווע,מוסקבה,ماسکو,مسکو,موسكو,موسكۋا,ܡܘܣܩܒܐ,मास्को,मॉस्को,মস্কো,மாஸ்கோ,มอสโก,མོ་སི་ཁོ།,მოსკოვი,ሞስኮ,モスクワ,莫斯科,모스크바",
        "latitude": "55.75222",
        "longitude": "37.61556",
        "feature class": "P",
        "feature code": "PPLC",
        "country code": "RU",
        "cc2": "",
        "admin1 code": "48",
        "admin2 code": "",
        "admin3 code": "",
        "admin4 code": "",
        "population": "10381222",
        "elevation": "",
        "dem": "144",
        "timezone": "Europe/Moscow",
        "modification date": "2020-03-31"
    }
}
```

## GET city names by part city name

```
$ curl http://127.0.0.1:8000/api/v1.0/help/анкт
{
    "анкт": [
        "Санкт Петербург",
        "Санкт Петерзбург",
        "Санкт-Петербург"
    ]
}
```
