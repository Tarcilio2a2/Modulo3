import requests
import streamlit as st

# Definindo a chave da API e a cidade
API_KEY = 'sua_chave_api'  # Substitua pela sua chave da API OpenWeather
CITY = 'São Paulo'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# Realiza a requisição para a API
response = requests.get(URL)
data = response.json()

# Verifica se a resposta foi bem-sucedida
if data['cod'] == 200:
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    st.write(f'Clima em {CITY}: {weather} com {temperature}°C')
else:
    st.write("Erro ao obter os dados do clima.")

# Recebendo os valores de umidade e pH via sliders do Streamlit
humidity = st.slider("Nível de Umidade do Solo", 0, 100, 50)
ph = st.slider("Valor de pH", 0.0, 14.0, 7.0)

# Lógica de irrigação baseada na previsão de chuva e nas condições do solo
if 'rain' in weather.lower():
    st.write("Previsão de chuva detectada. Irrigação desativada.")
else:
    if humidity < 30 or ph < 5.5:
        st.write("Irrigação Ativada!")
    else:
        st.write("Irrigação Desativada!")
