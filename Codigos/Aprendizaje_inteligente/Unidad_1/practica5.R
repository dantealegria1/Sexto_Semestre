# Utilizando barras invertidas dobles
library(readr)

# Lee el archivo CSV en un marco de datos en R
datos <- read.csv("D:\\Sexto_Semestre\\Codigos\\Aprendizaje_inteligente\\iris.csv", sep = ";", dec = ".")

# Muestra las primeras filas del marco de datos
print(head(datos))

muestra = sample(1:150,50)
muestra

ttesting = datos[muestra,]
ttesting

dim(ttesting)

tasa_aprendizaje <- datos[muestra,]
tasa_aprendizaje
dim(tasa_aprendizaje)

modelo <- naiveBayes(tipo-.,data-tasa_aprendizaje)
modelo

prediccion <- predict(modelo,tasa_aprendizaje[,-5])
prediccion

MC <- table(tasa_aprendizaje[,5],prediccion)
MC

aciertos <- (sum(diag(MC))/sum(MC))
aciertos

