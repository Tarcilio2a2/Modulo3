# Projeto de Irrigação Automatizada - Fase 3

## Objetivo

Este projeto visa desenvolver um sistema de irrigação inteligente que monitora a umidade do solo, os níveis dos nutrientes (representados por botões para P e K), e o pH (simulado por um sensor LDR). O sistema de irrigação é automatizado e ajusta a irrigação com base nesses parâmetros. O projeto foi desenvolvido utilizando um microcontrolador ESP32, sensores simulados no Wokwi, e banco de dados SQL para armazenar e consultar os dados.

## Descrição do Sistema

O sistema funciona da seguinte maneira:
1. **Sensores**:
   - **Botões**: Para simular os sensores de nutrientes P e K.
   - **LDR**: Para simular o sensor de pH, com valores mapeados de 0 a 14.
   - **DHT22**: Para medir a umidade do solo.

2. **Controle de Irrigação**:
   - A irrigação é controlada por um relé que é ativado ou desativado com base nos valores lidos dos sensores.
   - Se a umidade do solo estiver abaixo de 30% ou o pH for inferior a 5.5, a irrigação é ativada.

3. **Banco de Dados**:
   - O sistema envia os dados coletados para um banco de dados SQL (MySQL) utilizando um script Python.
   - A operação CRUD (criar, ler, atualizar e deletar) é realizada no banco de dados para armazenar os dados históricos da irrigação.

## Circuito - Wokwi

O circuito foi desenvolvido na plataforma Wokwi, utilizando os seguintes componentes:
- **ESP32**
- **Botões para P e K**
- **LDR para pH**
- **DHT22 para umidade**
- **Relé para controle de irrigação**

![Imagem do circuito Wokwi](circuito_wokwi.png)

## Código

- **ESP32 (Código C/C++)**: O código para o ESP32 é responsável por ler os sensores e controlar a irrigação.
- **Python**: O código Python se conecta ao banco de dados MySQL e insere os dados coletados dos sensores.

### Código C/C++ para o ESP32
[Veja o código do ESP32](esp32_code.ino)

### Código Python para interação com o Banco de Dados
[Veja o código Python](python_code.py)

## Demonstração

Abaixo está o link para o vídeo demonstrando o funcionamento do projeto:

[Link para o vídeo de demonstração](https://youtu.be/seu_video_link)

## Como Rodar o Projeto

1. **Configuração do Hardware**:
   - Conecte os sensores conforme mostrado no circuito Wokwi.
   - Carregue o código no seu ESP32.

2. **Configuração do Banco de Dados**:
   - Crie um banco de dados MySQL e execute a tabela `sensor_data`.
   
3. **Executar o Código Python**:
   - Execute o código Python para consultar e inserir os dados no banco de dados.

4. **Visualizar no Dashboard**:
   - (Opcional) Se você desenvolveu um dashboard em Python, visualize os dados interativamente.
