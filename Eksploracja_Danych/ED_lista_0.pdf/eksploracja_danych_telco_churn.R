data <- read.csv("C:/Users/micha/OneDrive/Dokumenty/GitHub/EKSPLORACJA-DANYCH/lista1/WA_Fn-UseC_-Telco-Customer-Churn.csv", 
                 sep=",", header=TRUE, stringsAsFactors=FALSE)
```{r}
# Rozmiar danych (liczba wierszy i kolumn)
dim(data)
```

# Podgląd pierwszych wierszy
head(data)

# Typy zmiennych
str(data)

# Podsumowanie danych
summary(data)

