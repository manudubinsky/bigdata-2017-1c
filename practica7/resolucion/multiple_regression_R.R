library(readr)

housing_data <- read_csv("C:/Users/victo/Downloads/properati-AR-2016-08-01-properties-sell.csv")
#El objetivo será determinar si el precio del inmueble esta "descrito por" (~) ciertas variables

#Planteo de los modelos

results_reduced <- lm(price ~ rooms +place_name, data = housing_data)
summary(results_reduced)
anova(results_reduced)
#el output muestra que F= 637.7 por lo que la cantidad de ambientes y la zona influyen en el precio
#Pero R^2 es muy cercano a cero, el modelo menos no se ajustaría la realidad

results_full <- lm(price ~ expenses + rooms +property_type +place_name+surface_total_in_m2+floor, data = housing_data)
summary(results_full)
anova(results_full)
#el output muestra que las variables mas significativas son la cantidad de habitaciones, las expensas y la superficie
#siendo para estas p-value<0.05
#R^2 es más cercano a 1, explicando el 22% de la variabilidad del modelo

results_full_v1 <- lm(price ~ rooms+expenses, data = housing_data)
summary(results_full_v1)
anova(results_full_v1)

results_full_v2 <- lm(price ~ rooms +expenses +surface_total_in_m2, data = housing_data)
summary(results_full_v2)
anova(results_full_v2)

#modelo significativo p-value<=0.05, estamos dentro del 95%
#se tomaron las variables significativas del modelo anterior
#R^2 es igual al anterior, estas son las variables más relacionadas con el precio

#Comparo el primer y el último modelo
anova(results_reduced,results_full_v1)
