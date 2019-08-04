# TesteD3
App Web de Anotações. Aplicativo exemplo para anotações pessoais com API REST.


# DEPLOY ADDRESS

https://yournotes4d3.herokuapp.com

user: tester

senha: bocchini1983


# API
ENDPOINT PARA OBTENÇÃO TOKEN DE ACESSO:

https://yournotes4d3.herokuapp.com/api-token-auth/

POST com USERNAME e PASSWORD como form-data (imagem exemplo "Token request - postman" neste mesmo repo)


# NOTES ENDPOINT:
https://yournotes4d3.herokuapp.com/api/v1/notes


GET e demais métodos obrigatóriamente com os seguintes HEADERS (imagem exemplo "acesso com Token postman" neste mesmo repo):

CONTENT-TYPE == application/json 

Authorization == Token seu-token
