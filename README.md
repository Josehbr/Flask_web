Aplicação Flask com SQLAlchemy e SQLite

Este é um exemplo de aplicação Flask que utiliza o ORM SQLAlchemy para se conectar a um banco de dados SQLite. A aplicação também possui um sistema de login e cadastro, onde os usuários autenticados são redirecionados para uma página de perfil que exibe seus dados.

Configuração do Ambiente
Antes de executar a aplicação, você precisa configurar o ambiente seguindo as etapas abaixo:

Certifique-se de ter o Python instalado (versão recomendada: Python 3.7 ou superior).

Instale as dependências do projeto executando o seguinte comando no terminal:

!pip install -r requirements.txt

Configuração das Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e defina as seguintes variáveis de ambiente:

Executando a Aplicação
Para executar a aplicação, execute o seguinte comando no terminal:

!flask run
Acesse a aplicação em seu navegador através do seguinte endereço: http://localhost:5000

Funcionalidades
Cadastro de Usuário
A aplicação permite o cadastro de novos usuários. Para se cadastrar, clique em cadastrar na página inicial e preencha o formulário de cadastro.

Login de Usuário
Após se cadastrar, você pode fazer o login usando as credenciais fornecidas durante o cadastro. Na página inicial clique em "Login" e preencha o formulário de login.

Página de Perfil
Após fazer o login com sucesso, você será redirecionado para a página de perfil, onde poderá visualizar seus dados.

Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:

app/: pasta principal do projeto.
templates/: diretório que contém os templates HTML para as páginas da aplicação.
static/: diretório que contém os arquivos estáticos (CSS, imagens.) da aplicação.
router.py: arquivo responsável pelas rotas e funcionalidades do cadastro e login.
db/: pasta que contém o arquivo de banco de dados.

manutencao/: pasta que contém códigos separados da aplicação principal para fazer manutenção no banco de dados.

Esta estrutura de pastas permite uma organização clara dos diferentes componentes da aplicação. Os arquivos do diretório app/ são responsáveis pelo funcionamento da aplicação web, incluindo a parte de design (templates) e lógica de roteamento (router.py). A pasta db/ armazena o arquivo do banco de dados SQLite utilizado pela aplicação. Já a pasta manutencao/ contém scripts que podem ser usados para realizar tarefas de manutenção no banco de dados, como operações de limpeza.


