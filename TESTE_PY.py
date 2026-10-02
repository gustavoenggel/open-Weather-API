#UMA API É UM JEITO CONECTAR SISTEMAS, INTERFACE DE PROGRAMAÇÃO DE APLICAÇÕES;
#API É UM CONJUNTO DE REGRAS E PADRÕES QUE PERMITE QUE DIFERENTE SISTEMAS
#DE SOFTWARE SE COMUNIQUEM E TROQUEM DADOS ENTRE SI;

#NESTE, SERÁ UTILIZADA A WEATHERapi.com PARA CONSULTAR AS CONDIÇÕES 
#CLIMÁTICAS DE UMA LOCALIDADE;

#CONSUMIR API ->
#VAMOS PRECISAR DE UMA PROGRAMA QUE TENHA UMA CERTA CAPACIDADE DE PEGAR DADOS
#MEDIANTE A UMA URL PRÉ DEFINIDA

#VAMOS PRECISAR DA APIKEY
import requests #biblioteca para fazer requisições HTTP
from pprint import pprint #biblioteca para imprimir dados de forma legível
api_key = "5403842e2e284a99a44224514262909"

link_api = "http://api.weatherapi.com/v1/current.json"

cidade = input("Digite o nome da cidade: ")
parametros = {
    "key": api_key,
    "q": "cidade", #cidade para qual queremos obter os dados
    "aqi": "yes", #não queremos dados de qualidade do ar
    "days": "1", #queremos apenas os dados do dia atual
    "lang": "pt" #Linguagem
}

#Armazenando a resposta da requisição na variável resposta

resposta = requests.get(link_api, params = parametros)

print(resposta)
#status 200 certo 400 errado


if resposta.status_code == 200:
    print("Requisição bem sucedida!")
    dados = resposta.json() #transformando a resposta em um dicionário
    pprint(dados) #imprimindo os dados de forma legível
    temperatura = dados["current"]["temp_c"] #pegando a temperatura em Celsius
    descricao = dados["current"]["condition"]["text"] #pegando a descrição do clima
    qualidade_ar = dados["current"]["air_quality"] #pegando a qualidade do ar
    descricao_qualidade_ar = qualidade_ar["us-epa-index"] #pegando a descrição da qualidade do ar
    dia = dados["location"]["localtime"] #pegando a data e hora local
    print(f"A temperatura em {cidade} é de {temperatura}°C e o clima é {descricao}")
    print(f"A qualidade do ar é {descricao_qualidade_ar}")
    print(f"A data e hora local são {dia}")


else:
    print("Erro na requisição:", resposta.status_code)