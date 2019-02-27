User Storyt
---------------------

### Rekisteröitymätön asiakas ###
Rekisteröitymättömänä asiakkaana haluan, että...
* .. voin tehdä varaukseni ilman rekisteröitymistä.
```
INSERT INTO booking (date_created, date_modified, notes, confirmed, requested_date, customer_id, worker_id, service_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
```
* .. näen ne ajankohdat, jolloin palveluntarjoajat ovat varattuina, jotta tiedän ajoittaa oman varaukseni.
```
SELECT Booking.requested_date, Worker.name, Service.duration_hrs, Service.duration_mins FROM Booking LEFT JOIN Worker ON Worker.id = Booking.worker_id LEFT JOIN Service ON Booking.service_id = Service.id WHERE Booking.confirmed = 1 GROUP BY Booking.requested_date, Worker.name, Service.duration_hrs, Service.duration_mins
```
* .. tietojani käsitellään luottamuksellisesti, jotta tietoni eivät joudu vääriin käsiin

### Rekisteröitynyt asiakas ###
Asiakkaana haluan, että...
* .. voin tilata tai varata palveluita tarpeideni mukaisesti
```
INSERT INTO booking (date_created, date_modified, notes, confirmed, requested_date, customer_id, worker_id, service_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
```
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
```
INSERT INTO booking (date_created, date_modified, notes, confirmed, requested_date, customer_id, worker_id, service_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
```
* .. voin tarkastella asiakkaideni tietoja.

### Ylläpitäjä / Esimies ###
Ylläpitäjänä tai esimiehenä haluan, että...
* .. voin lisätä järjestelmään uusia työntekijöitä ja ylläpitäjiä.
```
INSERT INTO account (date_created, date_modified, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```
```
INSERT INTO worker (date_created, date_modified, name, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
```
* .. voin poistaa työntekijöitä järjestelmästä.
```
 DELETE FROM worker WHERE worker.id = ?
```
```
DELETE FROM account WHERE account.id = ?
```
* .. voin ylentää työntekijän järjestelmässä esimieheksi / ylläpitäjäksi
```
UPDATE account SET date_modified=CURRENT_TIMESTAMP, role=? WHERE account.id = ?
```
* .. voin lisätä järjestelmään yrityksen tarjoamia palveluita, ja määrittää ketkä työntekijöistä niitä tarjoavat.
```
INSERT INTO service (date_created, date_modified, name, duration_hrs, duration_mins, cost_per_hour) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```
```
INSERT INTO worker_service (worker_id, service_id) VALUES (?, ?)
```
* .. näen kaikki järjestelmään tulleet tilaukset, jotta voin antaa tilauksia tehtäväksi työntekijöilleni.
```
SELECT booking.id AS booking_id, booking.date_created AS booking_date_created, booking.date_modified AS booking_date_modified, booking.notes AS booking_notes, booking.confirmed AS booking_confirmed, booking.requested_date AS booking_requested_date, booking.customer_id AS booking_customer_id, booking.worker_id AS booking_worker_id, booking.service_id AS booking_service_id 
FROM booking 
WHERE booking.confirmed = 0
```
* .. voin poistaa tilauksia.
```
DELETE FROM booking WHERE booking.id = ?
```
* .. voin lisätä järjestelmään työntekijävarauksen, jotta voin esimerkiksi merkitä kalenteriin vapaapäiväni.
```
INSERT INTO booking (date_created, date_modified, notes, confirmed, requested_date, customer_id, worker_id, service_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
```
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
```
UPDATE customer SET date_modified=CURRENT_TIMESTAMP, address=? WHERE customer.id = ?
```
```
DELETE FROM customer WHERE customer.id = ?
```
* .. näen halutessani statistiikkaa - kuten arviot tuloista ja maksettavista arvonlisäveroista - varauksiin liittyen.
```
**SELECT SUM(cost_per_hour * duration_hrs) + SUM(cost_per_hour * duration_mins / 60) FROM Service JOIN Booking ON Service.id = booking.service_id WHERE Booking.requested_date > ? and Booking.requested_date < ?**
```
```
SELECT COUNT(id) FROM Booking WHERE Booking.requested_date > ? and Booking.requested_date < ?
```
* näen mitkä 3 palvelua ovat kaikkein suosituimmat tilausmäärien perusteella:
```
**SELECT COUNT(booking.id) AS amount, service.name as service FROM booking INNER JOIN service ON service.id = booking.service_id  GROUP BY service.name HAVING COUNT(booking.id) > 0 ORDER BY COUNT(booking.id) DESC LIMIT 3**
```
* .. ne käyttäjät, joilla ei ole riittäviä oikeuksia, eivät pääse näkemään kaikkia tilauksia, asiakkaita tai statistiikkaa, eivätkä muokkaamaan työntekijä- tai palvelutietoja.
