# Regresja Liniowa

*Regresja liniowa i jej rozszerzenia — proste i wielokrotne MNK, estymacja nieliniowa, regresja logistyczna i kwantylowa (studia, PWr).*

![R](https://img.shields.io/badge/R-276DC3?logo=r&logoColor=white)

## 📖 Opis

Dziewięć raportów R/RMarkdown/Sweave z kolejnych zajęć: od estymacji i diagnostyki regresji prostej, przez regresję wielokrotną (VIF, selekcja krokowa), korelacje cząstkowe, estymację nieliniową metodą Gaussa-Newtona/Levenberga-Marquardta, po regresję logistyczną/probitową i regresję kwantylową. Tam, gdzie zachowały się wcześniejsze podejścia do tego samego zadania, dodano je obok wersji finalnej z sufiksem `_wersja_robocza`.

## 📂 Struktura

| Folder | Zawartość |
|---|---|
| `lista-01/` | Estymacja MNK regresji prostej: test istotności współczynnika, przedziały ufności, diagnostyka reszt (Q-Q, obserwacje wpływowe), symulacja przy różnym poziomie szumu |
| `lista-02/` | Regresja prosta z transformacją logarytmiczną, gdy reszty modelu liniowego wskazują na nieliniowość; skrypt pomocniczy z symulacją regresji prostej dla różnych σ |
| `lista-03/` | Regresja wielokrotna: macierz korelacji, iteracyjne usuwanie współliniowych zmiennych przez VIF, diagnostyka obserwacji wpływowych (Cook, leverage, rstudent) |
| `lista-04/` | Selekcja krokowa (backward, AIC) modelu regresji wielokrotnej, przedziały ufności współczynników, diagnostyka reszt względem każdej zmiennej |
| `lista-05/` | Korelacje zwykłe, cząstkowe i semicząstkowe oraz wizualizacja regresji wielorakiej (`avPlots`) |
| `lista-06/` | Estymacja nieliniowa metodą Gaussa-Newtona (funkcja wymierna, gradient, zbieżność dla różnych punktów startowych, macierz kowariancji estymatorów); warianty tłumione Levenberga-Marquardta na tym samym i na liniowym modelu |
| `lista-07/` | Regresja logistyczna na symulowanych danych binarnych: test ilorazu wiarygodności, interpretacja ilorazu szans, macierz pomyłek, krzywa ROC i AUC |
| `lista-08/` | Rozszerzenie lista-07: porównanie modeli logit i probit z selekcją zmiennych forward wg AIC i BIC |
| `lista-09/` | Regresja kwantylowa (`quantreg::rq`) na symulowanych danych z trzema rozkładami błędu, porównanie z regresją OLS |

## 🛠️ Technologie

| Technologia | Szczegóły |
|---|---|
| R | pakiety: car, ppcor, corrplot, MASS, quantreg, xtable, knitr |

## 👤 Autor

Michał Frąckowiak
