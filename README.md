📄 Gerador de Conteúdo com IA — Micro-SaaS para Negócios

Este projeto é um Gerador de Conteúdo com IA, desenvolvido em Python + Streamlit, utilizando a API da OpenAI.
A aplicação cria textos otimizados para SEO, redes sociais e blogs, adaptados ao nicho do cliente, ao público-alvo e ao tom desejado.

Ideal para:

Clínicas de saúde

Psicólogos

Dentistas

Empresas de ar-condicionado e refrigeração

Profissionais liberais

Agências de marketing

Criadores de conteúdo

🚀 Recursos Principais

Geração automatizada de posts otimizados para Instagram, Facebook, LinkedIn, Blogs, YouTube e E-mail.

Ajuste de tom, tamanho, público-alvo e plataforma.

Campo de nicho, permitindo textos ultra-específicos (ex.: “clínica de psicologia”, “empresa de ar-condicionado”).

Opção de incluir CTA e hashtags estratégicas.

Suporte para palavras-chave SEO.

Histórico de conteúdos gerados durante a sessão.

Botão Copiar conteúdo integrado nativamente via JavaScript.

Pronto para deploy no Railway, Vercel ou qualquer infraestrutura Python.

🧠 Tecnologias Utilizadas

* Python 3.x
* Streamlit
* LangChain
* OpenAI API
* streamlit-extras
* dotenv
* GitHub + Railway (deploy)

📦 Instalação e Configuração
1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

2. Crie o ambiente virtual
python -m venv venv


Ative:

Windows:

venv\Scripts\activate


Linux/macOS:

source venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt

4. Crie um arquivo .env
OPENAI_API_KEY="sua_chave_aqui"

5. Execute o projeto localmente
streamlit run app.py

☁️ Deploy no Railway
1. Arquivos necessários

Certifique-se de ter:

app.py

requirements.txt

Procfile

.gitignore

2. Configurar o Procfile
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

3. Subir o repositório para o GitHub
git add .
git commit -m "Initial commit"
git push origin main

4. No Railway:

Crie um novo projeto → Deploy from GitHub

Vá em Variables

Adicione: OPENAI_API_KEY

Deploy automaticamente

A URL ficará acessível ao público.

🧩 Estrutura do Projeto
/
├── app.py                # Código principal da aplicação
├── requirements.txt      # Dependências
├── Procfile              # Comando de inicialização no Railway
├── .env (local)          # Variáveis de ambiente
└── .gitignore            # Ignora venv, env, caches, etc.

🎯 Como Usar

Informe o nicho (ex.: “clínica de dermatologia”, “empresa de climatização”).

Digite o tema do post.

Escolha plataforma, tom, público e tamanho.

Opcional: inserir palavras-chave, CTA e hashtags.

Clique Gerar Conteúdo.

Use o botão copiar para colar no Instagram, blog ou site.

🛠️ Possíveis Extensões

Login + controle de assinantes

Créditos de uso (ex.: 50 textos/mês)

Exportação em PDF

Templates de posts

Dashboard admin

Integração com WhatsApp (bot)

API própria para revenda

Se quiser, posso ajudar a transformar isso em um produto SaaS completo.

🧑‍💻 Autor

Desenvolvido por Marcelo Levek — CoderTec
Soluções em IA, automação e SaaS para pequenos negócios.