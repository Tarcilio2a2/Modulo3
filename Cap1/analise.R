# Exemplo de análise estatística
library(ggplot2)

# Suponha que você tenha os dados de umidade do solo em um dataframe
data <- data.frame(
  timestamp = c('2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04'),
  humidity = c(30, 45, 20, 60)
)

# Visualização dos dados
ggplot(data, aes(x=timestamp, y=humidity)) +
  geom_line() +
  ggtitle("Análise de Umidade do Solo")
