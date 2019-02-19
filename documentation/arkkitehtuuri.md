# Arkkitehtuuri- ja tietokantakuvaus

## Yleistä

Ol-Booking on kirjoitettu Pythonilla. Keskeisimmät riippuvuudet ovat [Flask](http://flask.pocoo.org/docs/1.0/) ja [Jinja2](http://jinja.pocoo.org/docs/2.10/). Muut ohjelman riippuvuudet on listattu [requirements.txt](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/requirements.txt) -tiedostossa.

Ohjelmassa on neljä käyttäjäroolia. Nämä ovat:
* Pääkäyttäjä (Admin)
* Työntekijä (Worker)
* Rekisteröitynyt asiakas (Customer) ja
* Rekisteröitymätön asiakas.

Ohjelma rajaa / tarjoaa palveluita käyttäjäroolin perusteella. Tarkemmat käyttäjäroolien kuvaukset löytyvät [user stories](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/userstories.md) -tiedostosta.
## Tietokanta

Ohjelma käyttää paikallisesti SQlite -tietokannanhallintaa. Paikallinen tietokanta luodaan ohjelman ensimmäisen käynnistyksen yhteydessä tiedostoon olbooking.db. Ohjelmaan luodaan käynnistyksen yhteydessä ensimmäinen käyttäjä, jolla ohjelman käytön voi aloittaa.

Ensikirjautuminen:
* Käyttäjätunnus: 'testi'
* Salasana: 'testi'

Kun ohjelma on otettu käyttöön ja ohjelmaan on luotu haluttu käyttäjätunnus, on suositeltavaa poistaa testikäyttäjä manuaalisesti seuraavin komennoin ohjelman kansiosta (\Ohjelman_polku\application\) käsin.
```
sqlite3 olbooking.db
```
```
DELETE FROM Account WHERE id = 1;
```
```
.exit
```

Herokussa ohjelma käyttää PostgreSQL:aa.

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

#### Tietokantakaavio

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

### Käyttöliittymä

### Tietokanta

### Muuta

