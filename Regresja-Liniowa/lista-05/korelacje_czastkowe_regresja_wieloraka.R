library(ppcor)
library(readxl)
dane<-read_excel("C:/Users/micha/Downloads/lab7.xlsx")
temp1 <- cor(dane)
temp2 <-pcor(dane)
temp3 <- spcor(dane)
ext1 <- temp1$estimate
ext2 <- temp2$estimate
ext3 <- temp3$estimate

porownanie <- data.frame(
  Para           = c("Y~X1", "Y~X2", "Y~X3"),
  r_zwykle       = ext1[1, 2:4],
  r_czastkowe    = ext2[1, 2:4],
  r_semiczastkowe = ext3[1, 2:4]
)
print(round(porownanie, 4))

