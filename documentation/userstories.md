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
* .. näen kaikki järjestelmään tulleet tilaukset, jotta voin antaa tilauksia tehtäväksi työntekijöilleni.
* .. voin lisätä järjestelmään työntekijävarauksen, jotta voin esimerkiksi merkitä kalenteriin vapaapäiväni.
* .. voin hallinnoida kaikkia tilauksia.
* .. voin hallinnoida kaikkia järjestelmässä olevia asiakastietoja.
* .. näen halutessani statistiikkaa - kuten arviot tuloista ja maksettavista arvonlisäveroista - varauksiin liittyen.
```
SELECT SUM(cost_per_hour * duration_hrs) + SUM(cost_per_hour * duration_mins / 60) FROM Service JOIN Booking ON Service.id = booking.service_id WHERE Booking.requested_date > ? and Booking.requested_date < ?
2019-02-19 23:48:19,151 INFO sqlalchemy.engine.base.Engine (datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
```
* .. ne käyttäjät, joilla ei ole riittäviä oikeuksia, eivät pääse näkemään kaikkia tilauksia, asiakkaita tai statistiikkaa, eivätkä muokkaamaan työntekijä- tai palvelutietoja.
