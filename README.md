# api para cadastro de usuarios

## Ressalva:

Meu primeiro projeto em django, para ser sincero nunca toquei nessa lib. Eu tive que fazer **muita** pesquisa na documentção e assistir a **muitos** tutoriais para poder criar a api. Isso foi tudo que eu consegui fazer nesse tempo sem conhecimento prévio da lib. 

A api ficou um tanto quanto simples, pois tive que aprender enquanto a criava, espero pelo menos ter demonstrado minha iniciativa e vontade de me desenvolver. com certeza com tempo e mais instrução teria entregado mais ainda.

## Sobre api:

### Para iniciar:

Primeiramente inicie a venv 
    win: venv\Scripts\activate.bat
    linux:soruce venv/bin/activate

Depois inicar o servidor: 
    win: py manage.py runserver
    lixux:python manage.py runserver

E por fim abrir a porta padrão do localhost: http://127.0.0.1:8000/

### Funcionalidades:

Basicamente é possível cadastrar usuários no banco de dados usando: login, data de nacsimento e senha (sendo esta opcional). Caso a senha não seja inserida, a api gerará uma senha personalizada única. Os logins também são únicos e tem tamanho máximo de 10 caracteres.A data de nascimentpo está em formato ano-mês-dia. 

Também é possiível cadastrar usando algúm programa que mande requisição de cadastro em json, desde que esteja de acordo com os requisitos de cadastro.

Usando o botão 'get' é possível ter uma lista de todos os usuários em formato json. Ao lado do get clicando na setinha para baixo tem a opção em json, nela será redirecionado para outra página que conterá somente os usuários em json. 

Para visualizar os usuários em csv basta ir para a página principal (http://127.0.0.1:8000/) e adicionar 'export_csv', e abrir o arquivo em algum leitor csv. 

Para ver em xslx funciona da mesma maneira que o csv somente mudando o caminho para 'export_xslx'.