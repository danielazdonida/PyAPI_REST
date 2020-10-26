import requests
# pprint is used to format the JSON response
from pprint import pprint
import os

#ANALISE DE UM IDIOMA

#variáveis para a chave de assinatura e o endpoint do Azure
subscription_key = "03c84d95c648495fb4896fa245f88f28"
endpoint = "https://mycognitiveservicesresource12.cognitiveservices.azure.com/"

#acrescentar /text/analytics/v3.0/languages ao endpoint para formar a URL de detecção de idioma.
language_api_url = endpoint + "/text/analytics/v3.0/languages"

#dicionário que será analisado
documents = {"documents": [
    {"id": "1", "text": "Este é um documento escrito em uma linguagem desconhecida."},
    {"id": "2", "text": "Este es un document escrito en Español."},
    {"id": "3", "text": "这是一个用中文写的文件"}
]}

#adicionar a chave de assinatura ao cabeçalho Ocp-Apim-Subscription-Key
headers = {"Ocp-Apim-Subscription-Key": subscription_key}

#usar a biblioteca de solicitações para enviar os documentos à API.
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)
print("")
print("")


#ANALISE DE SENTIMENTO
#acrescentar /text/analytics/v3.0/sentiment ao endpoint para formar a URL de detecção de idioma.
sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"

documents = {"documents": [
    {"id": "1", "language": "pt",
        "text": "Eu gostei da nova TV da Samsung."},
    {"id": "2", "language": "es",
        "text": "Este ha sido un dia muy bueno, llegué tarde al trabajo debido a un accidente automobilistico."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)
print("")
print("")


#EXTRAIR FRASES CHAVE
#extrair as frases-chave de um conjunto de documentos
keyphrase_url = endpoint + "/text/analytics/v3.0/keyphrases"

documents = {"documents": [
    {"id": "1", "language": "en",
        "text": "Me and my boyfriend traveled to North Korea in the summer."},
    {"id": "2", "language": "pt",
        "text": "O novo Iphone possui novos recursos porém está com preço elevado."},
    {"id": "3", "language": "en",
        "text": "The Grand Hotel is a new hotel in the center of Seattle. It earned 5 stars in my review, and has the classiest decor I've ever seen."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(keyphrase_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)
