library(car)
library(readxl)

dane<-read_excel("regresja wielokrotna 2026.xlsx")
dane<-as.data.frame(dane)
sum(is.na(dane))

pairs(dane)

plot(dane$X6,dane$X9)

macierz.korelacji<-round(cor(dane),3)
View(macierz.korelacji)
library(corrplot)
corrplot(macierz.korelacji,method='color',
         addCoef.col='black',number.cex=0.6)

model<-lm(Y~.,dane)
model$coefficients

info<-summary(model)
info$r.squared
info$adj.r.squared

pf(info$fstatistic,info$df[1],info$df[2],lower.tail=F)[1]

vif.val<-vif(model)

while(any(vif.val>10)){
  zmienna.do.usunięcia<-names(which.max(vif.val))
  formuła<-formula(model)
  formuła.nowa<-update(formuła,paste(". ~ . -",zmienna.do.usunięcia))
  model<-lm(formuła.nowa,dane)
  vif.val<-vif(model)
  print(vif.val)
}

n<-nrow(dane)
p<-length(coef(model))
lev<-hatvalues(model)
cook<-cooks.distance(model)
rstud<-rstudent(model)

próg.lev<-2*p/n
próg.cook<-4/(n-p)
próg.rstud<-2

indeks.lev<-which(lev>próg.lev)
indeks.cook<-which(cook>próg.cook)
indeks.rstud<-which(abs(rstud)>próg.rstud)

indeksy.do.usunięcia<-sort(unique(c(indeks.cook,indeks.rstud,indeks.lev)))

dane.2<-dane[-indeksy.do.usunięcia,]

plot(cook,pch=19,col='blue',ylim=c(0,0.06),xlim=c(0,210))
abline(próg.cook,0)
text(x=indeks.cook,y=cook[indeks.cook]*1.1,labels=indeks.cook)

model<-lm(formuła.nowa,dane.2)
model$coefficients
info<-summary(model)
info$r.squared
info$adj.r.squared
pf(info$fstatistic,info$df[1],info$df[2],lower.tail=F)[1]

info
