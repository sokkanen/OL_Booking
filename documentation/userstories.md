User Storyt
---------------------

### Rekisteröitymätön asiakas ###
Rekisteröitymättömänä asiakkaana haluan, että...
* .. voin tehdä varaukseni ilman rekisteröitymistä.
* .. voin tilata tai varata palveluita tarpeideni mukaan.
* .. näen ne ajankohdat, jolloin palveluntarjoajat ovat varattuina, jotta tiedän ajoittaa oman varaukseni.
```
SELECT Booking.requested_date, Worker.name, Service.duration_hrs, Service.duration_mins FROM Booking LEFT JOIN Worker ON Worker.id = Booking.worker_id LEFT JOIN Service ON Booking.service_id = Service.id WHERE Booking.confirmed = 1 GROUP BY Booking.requested_date, Worker.name, Service.duration_hrs, Service.duration_mins
```
* .. tietojani käsitellään luottamuksellisesti, jotta tietoni eivät joudu vääriin käsiin

### Rekisteröitynyt asiakas ###
Asiakkaana haluan, että...
* .. voin tilata tai varata palveluita tarpeideni mukaisesti
* .. näen ne ajankohdat, jolloin palveluntarjoajat ovat varattuina, jotta tiedän ajoittaa oman varaukseni.
```
SELECT Booking.requested_date, Worker.name, Service.duration_hrs, Service.duration_mins FROM Booking LEFT JOIN Worker ON Worker.id = Booking.worker_id LEFT JOIN Service ON Booking.service_id = Service.id WHERE Booking.confirmed = 1 GROUP BY Booking.requested_date, Worker.name, Service.duration_hrs, Service.duration_mins
```
* .. voin rekisteröityä varausjärjestelmään, jotta voin tarkastella tilauksiani
* .. näen varausjärjestelmästä kun tilaukseni on vahvistettu, jotta tiedän tilauksen olevan käsittelyssä.
* .. tietojani käsitellään luottamuksellisesti, jotta tietoni eivät joudu vääriin käsiin
* .. voin nähdä ja muokata minusta talletettuja tietoja.

### Työntekijä ###
Työntekijänä haluan, että...
* .. järjestelmä listaa tarjoamani palvelut, jotta asiakkaat voivat varata niitä.
* .. näen minulle tehtäväksi annetut varaukset, jotta voin tehdä työni suunnitelmallisesti.
```
SELECT * FROM Booking WHERE confirmed = 1 AND worker_id = ?
```
* .. näen tilauksen tehneen asiakkaan tiedot, jotta voin olla häneen yhteydessä.
* .. asiakkaat näkevät järjestelmästä mikäli olen jollakin ajanhetkellä varattuna, jotta minun palveluitani haluavat asiakkaat saavat niitä.
* .. voin lisätä järjestelmään työntekijävarauksen, jotta voin esimerkiksi merkitä kalenteriin vapaapäiväni.
* .. voin tarkastella asiakkaideni tietoja.

### Ylläpitäjä / Esimies ###
Ylläpitäjänä tai esimiehenä haluan, että...
* .. voin lisätä järjestelmään uusia ylläpitäjiä.
* .. voin lisätä ja poistaa työntekijöitä järjestelmästä.
* .. voin ylentää työntekijän järjestelmässä esimieheksi / ylläpitäjäksi
* .. voin lisätä järjestelmään yrityksen tarjoamia palveluita, ja määrittää ketkä työntekijöistä niitä tarjoavat.
```
SELECT service.id AS service_id, service.date_created AS service_date_created, service.date_modified AS service_date_modified, service.name AS service_name, service.duration_hrs AS service_duration_hrs, service.duration_mins AS service_duration_mins, service.cost_per_hour AS service_cost_per_hour, anon_1.worker_id AS anon_1_worker_id 
FROM (SELECT worker.id AS worker_id 
FROM worker) AS anon_1 JOIN worker_service AS worker_service_1 ON anon_1.worker_id = worker_service_1.worker_id JOIN service ON service.id = worker_service_1.service_id ORDER BY anon_1.worker_id
```
* .. näen kaikki järjestelmään tulleet tilaukset, jotta voin antaa tilauksia tehtäväksi työntekijöilleni.
```
SELECT booking.id AS booking_id, booking.date_created AS booking_date_created, booking.date_modified AS booking_date_modified, booking.notes AS booking_notes, booking.confirmed AS booking_confirmed, booking.requested_date AS booking_requested_date, booking.customer_id AS booking_customer_id, booking.worker_id AS booking_worker_id, booking.service_id AS booking_service_id 
FROM booking 
WHERE booking.confirmed = 0
```
* .. voin lisätä järjestelmään työntekijävarauksen, jotta voin esimerkiksi merkitä kalenteriin vapaapäiväni.
```
INSERT INTO booking (date_created, date_modified, notes, confirmed, requested_date, customer_id, worker_id, service_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
```
* .. voin hallinnoida kaikkia tilauksia.
* .. voin hallinnoida kaikkia järjestelmässä olevia asiakastietoja.
```
SELECT customer.id AS customer_id, customer.date_created AS customer_date_created, customer.date_modified AS customer_date_modified, customer.name AS customer_name, customer.email AS customer_email, customer.address AS customer_address, customer.phone AS customer_phone, customer.account_id AS customer_account_id 
FROM customer ORDER BY customer.name
```
```
SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.username AS account_username, account.password AS account_password, account.role AS account_role 
FROM account 
WHERE account.id = ?
```
* .. näen halutessani statistiikkaa - kuten arviot tuloista ja maksettavista arvonlisäveroista - varauksiin liittyen.
```
SELECT SUM(cost_per_hour * duration_hrs) + SUM(cost_per_hour * duration_mins / 60) FROM Service JOIN Booking ON Service.id = booking.service_id WHERE Booking.requested_date > ? and Booking.requested_date < ?
2019-02-19 23:48:19,151 INFO sqlalchemy.engine.base.Engine (datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
```
* .. ne käyttäjät, joilla ei ole riittäviä oikeuksia, eivät pääse näkemään kaikkia tilauksia, asiakkaita tai statistiikkaa, eivätkä muokkaamaan työntekijä- tai palvelutietoja.
