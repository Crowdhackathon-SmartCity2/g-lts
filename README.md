# City Payment Gateway.
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![MariaDb](https://img.shields.io/badge/Database-MariaDB-red.svg)](https://mariadb.org/)
[![python3](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![django2.0](https://img.shields.io/badge/Django-2.0.6-green.svg)](https://docs.djangoproject.com/en/2.0/releases/2.0/)
[![djangoApp](https://img.shields.io/badge/DjangoApp-v1-orange.svg)](https://github.com/Crowdhackathon-SmartCity2/g-ltstree/master/)
[![PHP](https://img.shields.io/badge/PHP-v5.6-blue.svg)](https://secure.php.net/releases/5_6_0.php)
[![HTML5](https://img.shields.io/badge/HTML-5-red.svg)](https://www.w3.org/TR/html5/) [![CSS3](https://img.shields.io/badge/CSS-3-blue.svg)](https://www.w3.org/Style/CSS/Overview.en.html) [![JavaScript](https://img.shields.io/badge/Java-Script-yellow.svg)](https://www.javascript.com/) [![coverage-95%](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)](https://github.com/Crowdhackathon-SmartCity2/g-lts/tree/master/)


### Εισαγωγή.

Ηλεκτρονική
Πλατφόρμα που περιλαμβάνει :

* Εικονικό Κοινωνικό Παντοπωλείο

* Πληρωμές στον δήμο

* Παραγγελίες χωρίς μεσάζοντες

* Ανταποδοτικότητα – επιβράβευση
δωρητών, πολιτών και επιχειρήσεων


### Ανάγκη.
  * Εξεύρεση πόρων για ενίσχυση
  κοινωνικών δομών

  * Ενίσχυση τοπικών
  επιχειρήσεων/παραγωγών με καλές πρακτικές κυκλικής οικονομίας

  * Εκσυγχρονισμός μέσων πληρωμής του
  δήμου

  * Ενίσχυση συλλογικών δράσεων σε
  τοπικό επίπεδο

  * Μείωση κόστους με εκμετάλλευση
  ελεύθερου λογισμικού και ανοιχτών τεχνολογικών υποδομών (Open
  APIs)

  *  Μείωση γραφειοκρατίας


### Στιγμιότυπα.


| !["welcome"](/screenshots/user/1.welcomeactions.png) |
|:--:|
| Αρχική σελίδα. |


| !["Πληρωμές στο δήμο"](/screenshots/user/2.paymetsdimos.png) |
|:--:|
| Πληρωμές στο Δήμο. |


| !["ΔΕΗ"](/screenshots/user/3.payDEI.png) |
|:--:|
| ΔΕΗ : Ανάλυση λογαριασμού (ΔΤ, ΔΦ & ΤΑΠ) |

| !["ΔΕΗ"](/screenshots/user/4.justpay.png) |
|:--:|
| ΔΕΗ : Επιλογή πληρωμής |

| !["ΔΕΗ"](/screenshots/user/5.payments.png) |
|:--:|
| ΔΕΗ : Ιστορικό πληρωμών |

| !["Παραγγελίες"](/screenshots/user/6.orderswithoutmidleman.png) |
|:--:|
| Παραγγελίες χωρίς μεσάζοντες |

| !["Παραγγελίες"](/screenshots/user/7.orders.png) |
|:--:|
| Λίστα και ιστορικό παραγγελιών |

| !["Πληροφορίες"](/screenshots/user/now_state.png) |
|:--:|
| Πληροφορίες του Δήμου και του δημότη. |

| !["Πληρωμή"](/screenshots/user/9.ibankPaydonation.png) |
|:--:|
| Διαθέσιμοι τρόποι πληρωμής και διαθέσιμος τρόπος δωρεάς προς το κοινωνικό παντοπωλείο. |

| !["Πληροφορίες"](/screenshots/user/chenged_state.png) |
|:--:|
| Η απευθείας ανανέωση των πληροφοριών <br/> ( διαφάνεια & ενημέρωση δημοτών ). |


### Εργαλεία που βασιστήκαμε.
* [AdminLTE](https://adminlte.io/): Premium Admin control Panel.
* APIs :
  * [NBG open APIs](https://developer.nbg.gr) :
      * [Optical Character Recognition 1.0.0](https://developer.nbg.gr/product/optical-character-recognition)
      * [Digital Payments Wallet (1.1)](https://developer.nbg.gr/product/5b23820be4b04700451d7d28)
      * [Bill Payments (2.0.0)](https://developer.nbg.gr/product/5b3209b1e4b04700451dc478)
      * [Social Network Platform (1.0.0)](https://developer.nbg.gr/product/5adeeb09e4b0e25aa9c0e2fd)
  * [Mastercard APIs](https://developer.mastercard.com/)
  * [PayPal APIs](https://developer.paypal.com/docs/api/overview/).

Download
------------

Download from [Github](https://github.com/orgs/Crowdhackathon-SmartCity2/teams/34-g-lts).


Installation
------------
Υπάρχουν διάφοροι τρόποι να εγκαταστήσει κάποιος την πλατφόρμα μας. Όμως πρώτα από όλα θα πρέπει να έχει μερικά απαραίτητα πακεέτα εγκατεστημένα στο σύστημα του.

#### Απαραίτητα πακέτα συστήματος.
```bash
apt-get install libapache2-mod-php php php-cgi php-cli php-common php-curl php-gd php-json php-mysql php-readline python3-venv
```
ή
```bash
apt-get install libapache2-mod-php5 php5 php5-cgi php5-cli php5-common php5-curl php5-gd php5-json php5-mysql php5-readline python3-venv
```
##### Πακέτα python.
Για την εγκατάσταση των απαραίτητων πακέτων της python εκτελέστε απλώς την παρακάτω εντολή :
```bash
pip install -r requirements.txt
```


### Λειτουργίες.
1. Βασικές Δράσεις.
  * Παραγγελίες χωρίς μεσάζοντες.
  * Πληρωμές σε ότι αφορά τον δήμο:
	* [ΔΕΗ](https://www.dei.gr/el/oikiakoi-pelates/xrisimes-plirofories-gia-to-logariasmo-sas/logariasmos-kai-xrewseis/ti-aforoun-oi-xrewseis-uper-tritwn-efk-eidtelos-5/dimotika-teli-dt-dimotikoi-foroi-dt-telos-akinitis)
    	   * Δημοτικά Τέλη ( ΔΤ )
    	   * Δημοτικοί Φόροι ( ΔΦ )
    	   * Τέλος Ακίνητης Περιουσίας ( ΤΑΠ )
  	* Δ.Ε.Υ.Α.Ι.
  	* Πρόστιμα
  * Υλοποίηση ψηφιακού Κοινωνικού Παντοπωλείου.
	Για κάθε παραγγελία δίνεται δυνατότητα στον χρήστη, να κάνει δωρεά στο κοινωνικό παντοπωλείο. Αυτή γίνεται με στρογγυλοποίηση του πληρωτέου ποσού.
2. Κερασάκια
  * Ανάλυση Φορολογικής Δήλωσης:
         Θα δίνεται δυνατότητα στον χρήστη να σκανάρει την φορολογική του δήλωση και να μαθαίνω στην στιγμή αν δικαιούται οικονομική βοήθεια από το κοινωνικό παντοπωλείο.

### Μελλοντικές επεκτάσεις.


License
-------
City Payment Gateway is an open source project by [G-LTS Team](https://g-lts.info/) that is licensed under [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.txt).

![lines of code](https://img.shields.io/badge/Lines%20of%20code-646.493-green.svg)
[![Commits](https://img.shields.io/badge/Commits-214-blue.svg)](https://github.com/Crowdhackathon-SmartCity2/g-ltscommits?author=Tas-sos)
