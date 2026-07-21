# Eksploracja Danych

*Eksploracyjna analiza danych (EDA), redukcja wymiarów i analiza skupień — raporty z przedmiotu Eksploracja danych (studia, PWr).*

![R](https://img.shields.io/badge/R-276DC3?logo=r&logoColor=white)

## 📖 Opis

Pięć raportów R Markdown (jeden na listę zadań), z których każdy eksploruje inny zbiór danych i inną technikę: statystyki opisowe i porównania grup, skalowanie wielowymiarowe (MDS), klasyfikację przez regresję liniową oraz analizę skupień.

## 📂 Struktura

| Folder | Zawartość |
|---|---|
| `ED_lista_0.pdf/` | `eksploracja_danych_telco_churn.R`, `raport_eksploracja_klientow_telco.Rmd` — pełna eksploracja danych o rezygnacji klientów telekomu (Telco Customer Churn): statystyki opisowe, porównanie grup churn/no-churn, wykresy |
| `ED_lista_1.pdf/` | `raport_eksploracja_klientow_telco_szkic.Rmd`/`.pdf` — wcześniejszy, prostszy szkic tej samej analizy klientów Telco |
| `ED_lista_2.pdf/` | `raport_mds_redukcja_wymiarow_titanic.Rmd`/`.pdf` — skalowanie wielowymiarowe (MDS) na danych Titanic, ze szczególnym uwzględnieniem zmiennej `Survived` |
| `ED_lista_3.pdf/` | `raport_regresja_liniowa_klasyfikacja_iris.Rmd`/`.pdf` — regresja liniowa użyta jako klasyfikator na zbiorze iris |
| `ED_lista_4.pdf/` | `raport_analiza_skupien_vehicle.Rmd`/`.pdf` — hierarchiczna i podziałowa analiza skupień na zbiorze Vehicle, wizualizacja przez MDS |

## 🛠️ Technologie

| Technologia | Szczegóły |
|---|---|
| R | pakiety: MASS, cluster, dendextend, dplyr, e1071, ggplot2, gridExtra, knitr, mlbench, tidyr, titanic, xtable |

## ⚠️ Uwagi

Nazwy folderów (`ED_lista_0.pdf` … `ED_lista_4.pdf`) pochodzą z nazw plików PDF z treścią zadań rozdanych na zajęciach — stąd rozszerzenie `.pdf` w nazwie folderu, mimo że w środku są pliki `.R`/`.Rmd`/`.pdf` z rozwiązaniem.

## 👤 Autor

Michał Frąckowiak
