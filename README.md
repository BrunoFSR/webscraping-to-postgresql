Webscraping to PostgreSQL

Esse projeto tem por objeto fazer um webscraping do site http://books.toscrape.com, coletando as informações dos livros do site. As informações coletadas são:
-Nome
-Categoria
-Estrelas
-Preço
-Possui Estoque

As informações coletadas são armazenadas num DataFrame que posteriomente são inseridas numa tabela em um banco de dados PostgreSQL.

Para a execução foram utilizados containeres com PostgreSQL, PGAdmin, Selenium/hub e Selenium/node-chrome. Dessa forma, toda a execução do script fica melhor protegida de erros e problemas de compatibilidade, por exemplo. Durante a execução, também é criado um ambiente virtual Python e são baixadas todas as dependências necessárias para a execução.

Para executar, basta chamar o comando abaixo:

sh install.sh

O resultado pode ser visto na tabela bookinfo dentro da base criada no PostgreSQL em:
http://localhost:16543/browser/

Observação: alguns comandos do arquivo install.sh podem mudar, pois esse script foi criado para o macOs.