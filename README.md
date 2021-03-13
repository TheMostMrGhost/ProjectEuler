Biblioteka ProjectEuler to zbiór funkcji użytecznych w rozwiązywaniu zadań z PE.
Aby pobrać należy wpisać w terminalu będąc w odpowednim katalogu "git clone https://github.com/Wesenheit/ProjectEuler.git".
Odpowiedni katalog znajdujemy importując w interpreterze pythona bibliotekę sys i wywołując sys.path. Komenda ta powinna zwrócić listę katalogów które interpreter
przeszukuje w poszukiwaniu bibliotek i to do jednego z tych katalogów należy przekopiować bibliotekę.
Opis:
NumberTheory/
	core.py
	modulo.py
GraphTheory/

core.py- zbiór podstawowych funkcji
	sito(x) - funkcja która inicjuje tablicę liczb która w i-tej komórce trzyma informację o najmniejszej liczbie pierwszej dzielącej i.
	primes(x,tab) - funkcja zwracająca wszystkie liczby pierwsze dzielące x (wymaga zinicjowanie tablicy tab funkcją sito)
	fact(x,tab) - funkcja faktoryzujaca liczbę (zwracająca tablicę tablic liczb pierwszych i ile razy występują w rozkłądzie,
        wymaga zainicjowania tablicy tab funkcją sito)
	tot(x,tab) -funkcja licząca tocjent
	nwd(a,b) - funkcja licząca nwd liczb a i b algorytmem euklidesa
modulo.py
	leg_sym(a,n)- funkcja licząca symbol legandra elementu a modulo n
	modular_sqrt(a,n) - funkcja znajdująca taki element x, że x^2=a mod n algorytmem Tonelliego–Shanksa
	inverse(x,p) - funkcja znajdująca element odwrotny do x w grupie multiplikatywnej mod p


funkcje importujemy np w ten sposób:
from ProjectEuler import NumberTheory as nt
nt.inverse(3,5)
