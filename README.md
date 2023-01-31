# rpi-drumset
### Bubnjevi.ipynb
U Bubnjevi.ipynb sam napravila vise verzija koda koji bi mogao raditi. nije mi se dalo raditi u .py datotekama jer mi je
ovako bilo jednostavnije za ispobavat i usporedivat kod. Ako nemas Jupyter Notebook samo iskopiraj kod u .py datoteku iz
bilo koje celije i dodaj ono if \_\_name\_\_=='\_\_main\_\_'... ako treba.

### Aplikacija za mob
Znaci vidjela sam da mozes povezat RPi sa aplikacijama na mobu pa sam naravno odlucila da nam treba to haha.
Ugl ima aplikacija RaspController koja moze tamo gledat inpute od senzora i tako malo davat neke naredbe i to al nisam
bas nasla nacin na koji bi mogle napravi da nam bude korisna bas za ovo.
https://www.youtube.com/watch?v=lnHyVswZksM&t=315s
https://www.gallinaettore.com/android_apps/raspcontroller/user_widgets/
Evo slobodno si pogledaj malo pa mozda ti nades nacin kako da je iskoristimo.

Al ugl isto sam nasla da se flutter aplikacije mogu povezat s RPi
https://www.youtube.com/watch?v=6gFvmrpXols
pa sam pocela to radit logicno.

https://www.figma.com/file/NYcB36ZdfwNJnnaL689UX1/Cinema-Booking-App-(Community)-(Copy)?node-id=0%3A1&t=Q39R0smRbGMIfpZZ-0
Otprilike kako bi izgledala aplikacija. Znaci ideja je da na pocetnoj stranici mozes odabrat koje zvukove oces za bubnjeve
i onda kliknes start da se pokrene aplikacija na RPi da mozes svirat. Kad kasnije kliknes end logicno aplikacija se zaustavi.
Onda na home page imas izbor oces koristit vec postavljen set zvukova ili napravit custom. Logicno prvi put kad pokrenes
aplikaciju moras napravit custom set. Na stranici sa setovima biras datoteke koje ce bit za bubanj koji zelis. Mozes ih 
odabrati vise i pustit ih u aplikaciji da mozes ih mozes usporediti medusobno i odabrati koji zelis najvise. Samo onda
moras odabrati koji oces da ti se spremi i to sugerira siva popuna polja. I gore lijevo mozes odabrat koji set zelis za 
slucaj da nekom vec napravljenom setu zels promjenit neki zvuk. Isto jos mozes i pobrisat cijeli set. Set se sprema pod imenom
koji odaberes i onda ga kasnije mozes birat na home page u drop down izborniku.

I naravno trebat ce za prvi put kad koristis aplikaciju napravit stranicu na kojoj mozes postavit RPi i odabrat mapu iz koje biras
zvukove, i isto da mozes dodat vise RPi a pa birat koji oces ako ih imas vise od jedan. Al to tek kasnije napravim kako bi izgledalo
otprilike kad skuzim kako bi moglo funkcionirat.
