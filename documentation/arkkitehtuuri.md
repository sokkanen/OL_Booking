# Arkkitehtuuri- ja tietokantakuvaus

## Yleistä

Ol-Booking on kirjoitettu Pythonilla ja HTML:llä. Keskeisimmät riippuvuudet ovat [Flask](http://flask.pocoo.org/docs/1.0/) ja [Jinja2](http://jinja.pocoo.org/docs/2.10/). Muut ohjelman riippuvuudet on listattu [requirements.txt](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/requirements.txt) -tiedostossa.

Ohjelmassa on neljä käyttäjäroolia. Nämä ovat:
* Pääkäyttäjä (Admin)
* Työntekijä (Worker)
* Rekisteröitynyt asiakas (Customer) ja
* Rekisteröitymätön asiakas.

Ohjelma rajaa / tarjoaa palveluita käyttäjäroolin perusteella. Tarkemmat käyttäjäroolien kuvaukset löytyvät [user stories](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/userstories.md) -tiedostosta.
## Tietokanta

#### Tietokantakaavio

![database](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/tietokanta.jpg)

Ohjelma käyttää paikallisesti SQlite -tietokannanhallintaa. Paikallinen tietokanta luodaan ohjelman ensimmäisen käynnistyksen yhteydessä tiedostoon olbooking.db. Ohjelmaan luodaan käynnistyksen yhteydessä ensimmäinen käyttäjä, jolla ohjelman käytön voi aloittaa.

Ensikirjautuminen:
* Käyttäjätunnus: 'testi'
* Salasana: 'testi'

Kun ohjelma on otettu käyttöön ja ohjelmaan on luotu haluttu pääkäyttäjätunnus, on suositeltavaa poistaa testikäyttäjä manuaalisesti seuraavin komennoin ohjelman kansiosta (\Ohjelman_polku\application\) käsin.
```
sqlite3 olbooking.db
```
```
DELETE FROM Account WHERE username = 'testi';
```
```
.exit
```

Herokussa ohjelma käyttää PostgreSQL:aa.

Herokussa toimivan ohjelman testikäyttäjän poistaminen onnistuu ohjelman paikallisesti kansiosta (\Ohjelman_polku\) seuraavin komentorivikomennoin:
```
heroku pg:psql
```
```
DELETE FROM account WHERE username = 'testi';
```
```
\q
```

### Tietokannan CREATE TABLE -lauseet tauluittain

#### Service
```
CREATE TABLE service (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	duration_hrs INTEGER, 
	duration_mins INTEGER, 
	cost_per_hour INTEGER, 
	PRIMARY KEY (id)
	)
```
#### Account
```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(10) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
	)
```
#### Worker
```
CREATE TABLE worker (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
	)
```
#### Customer
```
CREATE TABLE customer (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	email VARCHAR(144) NOT NULL, 
	address VARCHAR(144) NOT NULL, 
	phone VARCHAR(144) NOT NULL, 
	account_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
	)
```
#### Booking
```
CREATE TABLE booking (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	notes VARCHAR(150) NOT NULL, 
	confirmed INTEGER NOT NULL, 
	requested_date DATETIME NOT NULL, 
	customer_id INTEGER NOT NULL, 
	worker_id INTEGER, 
	service_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(customer_id) REFERENCES customer (id), 
	FOREIGN KEY(worker_id) REFERENCES worker (id), 
	FOREIGN KEY(service_id) REFERENCES service (id)
	)
```
#### Worker_Service
```
CREATE TABLE worker_service (
	worker_id INTEGER NOT NULL, 
	service_id INTEGER NOT NULL, 
	PRIMARY KEY (worker_id, service_id), 
	FOREIGN KEY(worker_id) REFERENCES worker (id), 
	FOREIGN KEY(service_id) REFERENCES service (id)
	)
```
## Ohjelman rakenne

#### Tiedostorakenne

Ohjelman tiedostorakenne keskeisimmiltä osiltaan on seuraava:
```
├── application
│   ├── account
│   │   ├── forms.py
│   │   ├── __init.py__
│   │   ├── models.py
│   │   └── views.py
│   ├── booking
│   │   ├── cal.py
│   │   ├── forms.py
│   │   ├── __init.py__
│   │   ├── models.py
│   │   └── views.py
│   ├── customer
│   │   ├── forms.py
│   │   ├── __init.py__
│   │   ├── models.py
│   ├── __init__.py
│   ├── models.py
│   ├── requirements.txt
│   ├── service
│   │   ├── forms.py
│   │   ├── __init.py__
│   │   ├── models.py
│   ├── templates
│   │   ├── account
│   │   │   ├── accounts.html
│   │   │   ├── loginform.html
│   │   │   ├── modinfo.html
│   │   │   └── register.html
│   │   ├── booking
│   │   │   ├── calendar.html
│   │   │   ├── list.html
│   │   │   ├── statistics.html
│   │   │   └── unreg_calendar.html
│   │   ├── index.html
│   │   ├── layout.html
│   │   ├── open.jpg
│   │   └── worker
│   │       └── list.html
│   ├── views.py
│   └── worker
│       ├── forms.py
│       ├── __init__.py
│       ├── models.py
│       └── views.py
├── Procfile
├── requirements.txt
├── run.py
```

Ohjelman keskeisimmät kokonaisuudet ovat Account, Booking, Customer, Service ja Worker
* Account: Ohjelman käyttäjätilitoiminnallisuudet. Jokaiseen käyttäjätiliin liittyy joko Customer tai Worker.
* Booking: Ohjelman varaustoiminnallisuudet (ml. kalenteriluokka cal.py)
* Customer: Asiakasluokka. Käyttäjäroolina Customer. Rekisteröityyn asiakkaaseen liittyy Account. Rekisteröitymätön asiakas pelkästään Customer.
* Service: Työntekijöiden (Worker) tarjoamista palveluista vastaava luokka.
* Worker: Työntekijäluokka. Käyttäjärooleina Worker ja Admin.
* Templates: Renderöitävät HTML-sivut.

## Ohjelman rakenteeseen jääneet heikkoudet

* Palveluvalikoiman lisääminen ja hallinnointi on kankeahkoa. Nykyisessä ohjelmistoversiossa jokaiselle palvelulle täytyy luoda oma rivi tietokantaan (esim. haravointi 100m2 ja haravointi 200m2). Yksikön määrittäminen tekisi ohjelmasta verrattain monimutkaisen, sillä jokaiselle eri tyyppiselle palvelulle jouduttaisiin määrittämään myös yksikkö (selkähieronta 1h on paljon parempi kuin selkähieronta 100m2...).
* Ohjelman nykyinen versio soveltuu pienyritykselle, jolla on verrattain vähän työntekijöitä, suppeahko palveluvalikoima ja vähän rekisteröityneitä asiakkaita. Nykyisessä muodossaan ohjelma ei palvele yhtään isomman yrityksen tarpeita. Isommalle tietomassalle tiedon filtteröinti ja valitseminen täytyisi rakentaa täysin toisella tulokulmalla.

## Jatkokehitysideat

* Ohjelmaan olisi verrattain helppoa luoda viestitoiminnallisuus, joka mahdollistaisi työntekijöiden ja asiakkaiden välisen viestinnän. Tämä on jätetty nykyisestä ohjelmaversiosta pois työn paisumisen välttämiseksi.
* Toinen - vielä pidemmälle viety - lisäys olisi automaattinen sähköpostinlähetys asiakkaalle varauksesta, varauksen vahvistamisesta jne.

