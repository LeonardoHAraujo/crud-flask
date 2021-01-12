Título: API-Flask

Autor: Leonardo Araújo

A API foi criada com Flask, para fins de estudo e conhecimento da micro-framework Flask.

A API funciona da seguinte maneira:

A API é composta pelas quatro funções CRUD (create, read, update e delete).
Foi feito deploy da aplicação no heroku, pode acessar os seguintes endereços para teste.

    Requisição GET : https://crud-flask-test.herokuapp.com/
    // Lista todos os usuários do banco

    Requisição POST : https://crud-flask-test.herokuapp.com/create
    // Cria novo registro no banco

    Requisição PUT : https://crud-flask-test.herokuapp.com/edit/1 (acessado quando clica no botão edit).
    // Atualiza registro existente

    Requisição DELETE : https://crud-flask-test.herokuapp.com/delete/1 (acessado quando clica no botão delete).
    // Exclusão de registro existente


Como testar em sua máquina:

1. Clone o repositório em sua máquina. (Baixando o ZIP ou pelo GIT);
2. Tendo Python3 e o pip3 em sua máquina, rode: "pip3 install -r requirements.txt";
3. Após isso rode: "python3 app.py";

OBS: Os arquivos requirements.txt e Procfile são essenciais para o deploy.
     Pois, na parte "app:app" do Procfile, é onde é interpretado pelo heroku
     que deve buscar dentro do arquivo app, a variavel app para executar o flask.
     
     E o requirements é para o heroku instalar as dependências que seu projeto
     precisa para rodar.
     
     
Como fazer deploy no heroku:

1. Rode o comando "heroku login" (Tendo heroku CLI instalado);
2. Rode o comando "heroku apps:create <nome-da-aplicação>";
3. Rode o comando "git init" (Tendo o Git CLI instalado);
4. Rode o comando "heroku git:remote -a <nome-da-aplicação>";
5. Com Procfile configurado e o requirements.txt configurado,
   Rode o comando "git add .";
6. Rode o comando "git commit -am <mensagem-de-commit>";
7. Rode o comando "git push heroku master";
8. Acesse "https://<nome-da-aplicação>.herokuapp.com/";

OBS: Caso algo dê errado, olhe os comandos em sua conta no 
     Heroku, que ai as coisas podem ficar mais claras para o
     debbug.
