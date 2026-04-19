# Projekt AI – Perceptron w rolnictwie

## Opis problemu

Celem projektu było stworzenie prostego modelu sztucznej inteligencji,
który na podstawie warunków środowiskowych określa, czy możliwa jest uprawa roślin.

Model analizuje dane takie jak:
- wilgotność
- temperatura
- opady
- pH gleby

Na tej podstawie zwraca decyzję:
- 1 – można uprawiać
- 0 – nie można uprawiać

---

## Dane

Dane znajdują się w pliku:

data/crop_data.csv

Zawierają przykładowe pomiary środowiska oraz decyzję.

Każdy rekord składa się z:
- wilgotność
- temperatura
- opady
- pH
- decyzja (0/1)

---

## Zastosowany algorytm

W projekcie zaimplementowano perceptron.

Jest to bardzo prosty model klasyfikacji, który:
- przypisuje wagę każdej cesze
- oblicza sumę ważoną
- na tej podstawie podejmuje decyzję 0 lub 1

Model uczy się na podstawie danych:
- jeśli się pomyli → poprawia wagi
- powtarza to wiele razy (epoki)

---

## Jak działa program (krok po kroku)

1. Program wczytuje dane z pliku CSV
2. Skaluje dane do zakresu 0–1
3. Dzieli dane na:
   - zbiór treningowy (80%)
   - zbiór testowy (20%)
4. Uczy perceptron na danych treningowych
5. Testuje model na danych testowych
6. Wyświetla wyniki

---

## Eksperymenty

Przeprowadzono kilka eksperymentów dla różnych parametrów:

- learning_rate = 0.1, epochs = 10
- learning_rate = 0.1, epochs = 50
- learning_rate = 0.1, epochs = 100
- learning_rate = 0.01, epochs = 50
- learning_rate = 0.5, epochs = 50

---

## Wyniki

Model osiągnął:

Accuracy = 1.00

Macierz pomyłek pokazuje brak błędów klasyfikacji.

---

## Wnioski

- perceptron dobrze działa dla prostych danych
- dane są liniowo separowalne
- zmiana parametrów nie miała dużego wpływu na wynik

---

## Struktura projektu

- app/data_loader.py – wczytywanie danych i przygotowanie
- app/perceptron.py – implementacja algorytmu
- app/metrics.py – obliczanie wyników
- app/run.py – uruchomienie eksperymentów
- data/crop_data.csv – dane

---
## Opis problemu

Celem projektu było stworzenie prostego modelu sztucznej inteligencji,
który na podstawie warunków środowiskowych określa, czy możliwa jest uprawa roślin.

Model analizuje dane takie jak:
- wilgotność
- temperatura
- opady
- pH gleby

Na tej podstawie zwraca decyzję:
- 1 – można uprawiać
- 0 – nie można uprawiać

---

## Dane

Dane znajdują się w pliku:

data/crop_data.csv

Zawierają przykładowe pomiary środowiska oraz decyzję.

Każdy rekord składa się z:
- wilgotność
- temperatura
- opady
- pH
- decyzja (0/1)

---

## Zastosowany algorytm

W projekcie zaimplementowano perceptron.

Jest to bardzo prosty model klasyfikacji, który:
- przypisuje wagę każdej cesze
- oblicza sumę ważoną
- na tej podstawie podejmuje decyzję 0 lub 1

Model uczy się na podstawie danych:
- jeśli się pomyli → poprawia wagi
- powtarza to wiele razy (epoki)

---

## Jak działa program (krok po kroku)

1. Program wczytuje dane z pliku CSV
2. Skaluje dane do zakresu 0–1
3. Dzieli dane na:
   - zbiór treningowy (80%)
   - zbiór testowy (20%)
4. Uczy perceptron na danych treningowych
5. Testuje model na danych testowych
6. Wyświetla wyniki

---

## Eksperymenty

Przeprowadzono kilka eksperymentów dla różnych parametrów:

- learning_rate = 0.1, epochs = 10
- learning_rate = 0.1, epochs = 50
- learning_rate = 0.1, epochs = 100
- learning_rate = 0.01, epochs = 50
- learning_rate = 0.5, epochs = 50

---

## Wyniki

Model osiągnął:

Accuracy = 1.00

Macierz pomyłek pokazuje brak błędów klasyfikacji.

---

## Wnioski

- perceptron dobrze działa dla prostych danych
- dane są liniowo separowalne
- zmiana parametrów nie miała dużego wpływu na wynik

---

## Struktura projektu

- app/data_loader.py – wczytywanie danych i przygotowanie
- app/perceptron.py – implementacja algorytmu
- app/metrics.py – obliczanie wyników
- app/run.py – uruchomienie eksperymentów
- data/crop_data.csv – dane

---

## Jak uruchomić

1. Otwórz terminal Git Bash

2. Wejdź do folderu projektu:
cd projekt-ai-rolnictwo


3. Zainstaluj wymagania:

pip install pandas


4. Uruchom program:

python -m app.run

---

## Autor Piotr Dziadosz
Zmiana do PR Final
