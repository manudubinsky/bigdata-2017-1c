library(choroplethr)

data <- read.csv("C:\\Users\\victo\\Downloads\\practica4\\resultado5.csv")

country_choropleth(data,
                   "Relevancia sitios educativos",
                   num_colors=1,
                   zoom=c("argentina", "brazil", "bolivia", "chile", "paraguay", "uruguay"))
