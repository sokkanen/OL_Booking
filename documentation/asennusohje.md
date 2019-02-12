# Ohjelmiston asennusohje

### Esitoimet

Ohjelmaa käyttävällä tietokoneella tulee olla asennettuna Python 3.
Ubuntussa Python 3:n asentaminen onnistuu pääkäyttäjäoikeuksilla komennolla "sudo apt-get install python3" 

### Paikallisesti toimivan ohjelmiston asennus

* Lataa ohjelman viimeisin versio zip-tiedostona Githubista [Klik](http://linkkiohjemanzippiin.com) ja pura zip-tiedosto haluamaasi kansioon.
* Mene komentorivillä ohjelman kansioon, ja luo ohjelmalle virtuaaliympäristö komennolla "python3 -m venv venv"
* Aktivoi virtuaaliympäristö komennolla "source venv/bin/activate" 
* Lataa ohjelman tarvitsemat riippuvuudet komennolla "pip install -r requirements.txt"
* Suorita ohjelma komennolla "python3 run.py"

Ohjelma toimii localhostin portissa 5000. (Selaimella: http://localhost:5000)

### Herokussa toimiva ohjelmisto
