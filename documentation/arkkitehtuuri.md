# Arkkitehtuuri- ja tietokantakuvaus

## Yleistä

Ol-Booking:n keskeisimmät toteutusvälineet ovat Python 3, [Flask](http://flask.pocoo.org/docs/1.0/) ja [Jinja2](http://jinja.pocoo.org/docs/2.10/). Muut ohjelman riippuvuudet on listattu [requirements.txt](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/requirements.txt) -tiedostossa.

## Tietokannan CREATE TABLE -lauseet tauluittain

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

