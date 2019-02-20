# Käyttöohje

## Yleistä

Ohjelman etusivu näyttää seuraavalta.

![frontpage](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/frontpage.jpg)

Etusivulta pääsee ilman rekisteröitymistä kolmeen näkymään:
* Booking (linkki yläpalkissa). Booking-näkymässä voi tehdä varauksen rekisteröitymättömänä asiakkaana.
* Register (linkki yläpalkissa oikealla). Register-sivulla on mahdollista luoda uusi asiakastili.
* Login (linkki yläpalkissa oikealla). Login näkymässä tapahtuu kirjautuminen kaikille käyttäjäryhmille.

![login](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/login.jpg)

## Rekisteröitymätön asiakas

Viemällä hiiren kursorin päivämäärän kohdalle, asiakas näkee tällä hetkellä järjestelmässä olevat, vahvistetut varaukset ko. päivälle.

![unreg_booking_res](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/unreg_booking_res.jpg)

Rekisteröitymätön asiakas voi tehdä palveluvarauksen Booking-näkymässä.

![unreg_booking](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/unreg_booking.jpg)

Varauksen kentät ovat seuraavat:
* Päivä ja aika: Päivän voi valita painamalla päivämäärän painiketta tai (selaimesta riippuen) suoraan kentästä. Järjestelmä ei anna tehdä varausta menneille päiville.
* Service: Alasvetovalikosta valitaan palvelu, jonka asiakas haluaa varata.
* Notes: Viesti palveluntuottajalle. Kenttä ei ole pakollinen.
* Name: Asiakkaan nimi. Kenttä on pakollinen.
* Email: Asikkaan sähköpostiosoite. Kenttä on pakollinen. Kenttä tarkastaa, että syöte on validin muotoinen sähköpostiosoite.
* Address: Asikkaan osoite. Kenttä on pakollinen.
* Phone: Asiakkaan puhelinnumero. Kenttä on pakollinen.

Varaus suoritetaan "Book service" -painikkeesta. Kentät saa tyhjennettyä "Reset"-painikkeesta.

## Rekisteröitynyt asiakas

#### Rekisteröityminen

![register](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/register.jpg)

#### Palveluvaraus

![reg_booking](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/reg_booking.jpg)

#### Vahvistettujen varausten tarkastelu

Yläpalkin painiketta "My Bookings" painamalla, asiakas pääsee tarkastelemaan varauksiaan. Asiakkaalle näytetään varaukset, jotka ovat hänen tekemiään ja vahvistettuja pääkäyttäjän toimesta.

![cust_bookings](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/cust_bookings.jpg)

#### Omat tiedot

Yläpalkin painiketta "My Accout" painamalla pääsee katsomaan ja muokkaamaan omia käyttäjätietojaan.

Näkymä avautuu käyttäjätunnukseen liittyvien asiakastietojen listaan. Asiakas ei voi poistaa itseään järjestelmästä, vaan nämä oikeudet on annettu ainoastaan pääkäyttäjälle.

![cust_related_accout](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/cust_related_account.jpg)

Painamalla nimessään olevaa linkkiä, asiakas pääsee tarkastelemaan hänestä talletettuja tietoja. 

![cust_information](https://github.com/sokkanen/TSOHA_OL_Booking/blob/master/documentation/Images/cust_info.jpg)

## Työntekijä

## Pääkäyttäjä

