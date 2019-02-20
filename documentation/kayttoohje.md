# Käyttöohje

Ohjeen sisällysluettelo:
- Yleistä
- Rekisteröitymätön asiakas
- Rekisteröitynyt asiakas
- Työntekijä
- Pääkäyttäjä

## Yleistä

Ohjelman etusivu näyttää seuraavalta.

![frontpage](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/frontpage.jpg)

Etusivulta pääsee ilman rekisteröitymistä näkymiin Booking, Login ja Register.

* Booking (linkki yläpalkissa). Booking-näkymässä voi tehdä varauksen myös rekisteröitymättömänä asiakkaana.
___________
* Register (linkki yläpalkissa oikealla). Register-sivulla on mahdollista luoda uusi asiakastili.

![register](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/register.jpg)

Rekisteröitymisen kentät ovat seuraavat:
* Name: Asiakkaan nimi. Kenttä on pakollinen, 3-50 merkkiä.
* Username: Käyttäjätunnus järjestelmään. Kenttä on pakollinen, 3-30 merkkiä.
* Password ja Repeat password: Käyttäjän salasana. Pakollinen, 5-100 merkkiä.
* Email: Asikkaan sähköpostiosoite. Kenttä on pakollinen. Kenttä tarkastaa, että syöte on validin muotoinen sähköpostiosoite.
* Address: Asikkaan osoite. Kenttä on pakollinen. 5-100 merkkiä.
* Phone: Asiakkaan puhelinnumero. Kenttä on pakollinen, 5-20 merkkiä.-
___________
* Login (linkki yläpalkissa oikealla). Kirjautuminen kaikille käyttäjäryhmille aiemmin luodulla käyttäjätunnuksella.

![login](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/login.jpg)

## Rekisteröitymätön asiakas

Viemällä hiiren kursorin päivämäärän kohdalle, asiakas näkee tällä hetkellä järjestelmässä olevat, vahvistetut varaukset ko. päivälle.

![unreg_booking_res](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/unreg_booking_res.jpg)
__________
Rekisteröitymätön asiakas voi tehdä palveluvarauksen Booking-näkymässä.

![unreg_booking](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/unreg_booking.jpg)

Varauksen kentät ovat seuraavat:
* Päivä ja aika: Päivän voi valita painamalla päivämäärän painiketta tai (selaimesta riippuen) suoraan kentästä. Järjestelmä ei anna tehdä varausta menneille päiville.
* Service: Alasvetovalikosta valitaan palvelu, jonka asiakas haluaa varata.
* Notes: Viesti palveluntuottajalle. Kenttä ei ole pakollinen, max 150 merkkiä.
* Name: Asiakkaan nimi. Kenttä on pakollinen, 3-50 merkkiä.
* Email: Asikkaan sähköpostiosoite. Kenttä on pakollinen. Kenttä tarkastaa, että syöte on validin muotoinen sähköpostiosoite.
* Address: Asikkaan osoite. Kenttä on pakollinen, 5-100 merkkiä.
* Phone: Asiakkaan puhelinnumero. Kenttä on pakollinen, 5-20 merkkiä.

Varaus suoritetaan "Book service" -painikkeesta. Kentät saa tyhjennettyä "Reset"-painikkeesta.

## Rekisteröitynyt asiakas

#### Palveluvaraus

![reg_booking](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/reg_booking.jpg)

Varauksen kentät ovat seuraavat:
* Päivä ja aika: Päivän voi valita painamalla päivämäärän painiketta tai (selaimesta riippuen) suoraan kentästä. Järjestelmä ei anna tehdä varausta menneille päiville.
* Service: Alasvetovalikosta valitaan palvelu, jonka asiakas haluaa varata.
* Notes: Viesti palveluntuottajalle. Kenttä ei ole pakollinen, max 150 merkkiä.

Varaus tehdään painamalla "Book service" -painiketta. Kenttien arvot nollataan "Reset" -painikkeesta.

#### Vahvistettujen varausten tarkastelu

Yläpalkin painiketta "My Bookings" painamalla, asiakas pääsee tarkastelemaan varauksiaan. Asiakkaalle näytetään varaukset, jotka ovat hänen tekemiään ja vahvistettuja pääkäyttäjän toimesta.

![cust_bookings](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/cust_bookings.jpg)

Asiakas ei voi poistaa varausta järjestelmästä.

_______

#### Omat tiedot

Yläpalkin painiketta "My Accout" painamalla pääsee katsomaan ja muokkaamaan omia käyttäjätietojaan.

Näkymä avautuu käyttäjätunnukseen liittyvien asiakastietojen listaan. Asiakas ei voi poistaa itseään järjestelmästä, vaan nämä oikeudet on annettu ainoastaan pääkäyttäjälle.

![cust_related_accout](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/cust_related_account.jpg)
___________
Painamalla nimessään olevaa linkkiä, asiakas pääsee tarkastelemaan hänestä talletettuja tietoja. 

![cust_information](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/cust_info.jpg)

Tietokenttien vaatimukset ovat samat kuin rekisteröidyttäessä järjestelmään. Salasana ei vaihdu, ellei kenttien arvoa muuteta. Mikäli henkilötiedot haluaa palauttaa ennalleen (ennen tallennusta), käyttäjä voi painaa "Reset" -painiketta. Henkilötiedot muutetaan pysyvästi "Modify" -painikkeella.

## Työntekijä

Työntekijän näkymässä keskeisimmät hallintanäkymät on koottu ohjelman alapalkkiin.

![Staff resources]()

#### Vahvistettujen varausten tarkastelu

Alapalkin painiketta "View bookings" (tai yläpalkin "My Bookings") painamalla, työntekijä pääsee tarkastelemaan hänelle tehtäväksi annettuja ja vahvistettuja varauksia. Työntekijä ei voi poistaa varauksia järjestelmästä.

![worker_bookings]()
_________
#### Asiakastietojen tarkastelu

Alapalkin painiketta "Customer information" (tai yläpalkin "My account") painamalla, työntekijä pääsee tarkastelemaan asiakastietoja. Työntekijä ei voi poistaa tai muokata järjestelmään tallennettuja asiakastietoja.

![worker_customers]()

## Pääkäyttäjä

