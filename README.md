<<<<<<< HEAD
# IA MARKDOWN API FRONT

[![Django](https://img.shields.io/badge/Django-4.x-green.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-orange)](#)
[![Code Style: Blue](https://img.shields.io/badge/code%20style-blue-0000FF.svg)](https://github.com/grantjenks/blue)
[![License](https://img.shields.io/badge/license-Interno%20da%20Empresa-lightgrey)](#)

---

Bem-vindo ao **IA MARKDOWN API FRONT**, um sistema avançado desenvolvido em Django para centralizar, organizar e potencializar a gestão documental e estratégica de organizações modernas. Com uma interface intuitiva, integra uma poderosa IA para análise de documentos e geração de conteúdos, além de recursos de personalização por setor, gerenciamento de usuários e muito mais.

---

> ⚠️ **Atenção:**  
> O ChatBot (IA corporativa) **NÃO** funcionará neste ambiente, pois a API de IA está hospedada localmente e não é pública.  
> **Você poderá navegar pelo layout, visualizar as páginas e explorar os recursos de interface normalmente.**  
> Caso deseje integrar sua própria API, basta adaptar o endpoint no código-fonte.

---

## 🚀 Funcionalidades

- 📄 **Centralização de Documentos Estratégicos**  
  Upload, download e gerenciamento centralizado de documentos relevantes à gestão, com filtros avançados por unidade/setor e busca dinâmica.

- 🤖 **IA Corporativa Integrada**  
  Consome uma API de IA própria (restrita), capaz de analisar documentos, gerar insights estratégicos, responder perguntas e criar relatórios detalhados sob demanda.

- 🖼️ **Geração de Imagens para Conteúdos**  
  Assistente IA para criação de imagens otimizadas para postagens e artigos institucionais, diretamente integradas ao sistema.

- 👤 **Gestão de Usuários e Perfis**  
  Autenticação robusta, perfis personalizados por área (ex: gestão, RH, TI), upload e gerenciamento de fotos de perfil.

- 📊 **Dashboards e Interatividade**  
  Interface responsiva, dashboards dinâmicos e navegação segmentada exibindo apenas os conteúdos relevantes a cada usuário.

- 🔒 **Administração e Segurança Avançadas**  
  Painel de administração Django, controle de permissões, logs de acesso e uso de variáveis de ambiente para segurança extra.

- 🛠️ **Código Limpo, Modular e Escalável**  
  Padrão Blue, fácil manutenção e expansão, pronto para integração de novas APIs e módulos.

- 🌐 **100% Personalizável**  
  Templates HTML facilmente adaptáveis para sua identidade visual.

---

## 🎯 Experiência Interativa

- **Busque e filtre documentos** por unidade/setor, facilitando o acesso à informação certa, na hora certa.
- **Peça análises e relatórios à IA** (quando integrada), tornando a tomada de decisão mais ágil e fundamentada.
- **Crie imagens e conteúdos** para postagens internas com auxílio da IA.
- **Gerencie perfis** e personalize sua experiência de acordo com sua área de atuação.
- **Acompanhe novidades e artigos** pela dashboard inicial.

---

## 🖼️ Interface e Navegação

Explore o sistema:

- **Landing Page** moderna e institucional.
- **Dashboard** com visão geral e atalhos rápidos.
- **Lista de Documentos** com filtros e busca.
- **Detalhamento de Postagens** e artigos com geração de imagens.
- **Área do Usuário** para personalização de perfil e documentos.
- **Administração** (via painel Django) para gestão avançada.

---

## 🛠️ Estrutura do Projeto

```
frontend_ia_django/
├── core/
│   ├── templates/core/
│   │   ├── base.html
│   │   ├── dashboards.html
│   │   ├── document_list.html
│   │   ├── home.html
│   │   ├── landing_page.html
│   │   ├── login.html
│   │   ├── post_detail.html
│   │   └── profile.html
│   ├── static/img/
│   ├── __init__.py
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── media/
│   ├── avatars/
│   ├── dashboards/
│   ├── documents/
│   ├── posts/
│   └── profile_pics/
├── site_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── .gitignore
├── requirements.txt
├── .env
└── README.md
```

---

## 📦 Instalação e Execução

> **Pré-requisitos:**  
> - Python 3.10+  
> - Django 4.x  
> - [Blue](https://github.com/grantjenks/blue) (opcional, para linting)
> - Banco de dados SQLite (padrão) ou outro, se preferir  
> - API de IA da empresa (restrita, não incluída neste repositório)

### 1. Clone o repositório

```bash
git clone https://github.com/LoboProgrammingg/IA-MARKDOWN-API-FRONT.git
cd IA-MARKDOWN-API-FRONT/frontend_ia_django
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o ambiente

- Renomeie `.env.example` para `.env` e preencha as variáveis conforme necessário.
- Ajuste `settings.py` para apontar para sua API de IA, se necessário.

### 5. Execute as migrações e inicialize o servidor

```bash
python manage.py migrate
python manage.py runserver
```

### 6. Acesse via navegador

Abra [http://localhost:8000](http://localhost:8000) para acessar a aplicação.

---

## 🤖 Sobre a Integração com IA

- A IA utilizada neste projeto é proprietária e restrita à empresa, não sendo distribuída neste repositório.
- Todas as interações com a IA (análises, respostas, geração de imagens) são feitas via API segura, respeitando os padrões de confidencialidade e compliance da empresa.
- **Quer testar a IA?**  
  - Implemente sua própria API e aponte o endpoint no projeto.
  - Explore o layout e a experiência do usuário como referência para suas próprias soluções!

---

## 💡 Sugestões de Uso

- **Gestores:** Consultem documentos estratégicos, recebam análises e relatórios sob demanda, compartilhem insights com o time.
- **RH e Unidades:** Organizem documentos, acessem conteúdos específicos para sua área e otimizem a comunicação interna.
- **Comunicação/Marketing:** Gere imagens para postagens, baixe conteúdos otimizados e mantenha tudo centralizado.

---

## 🧑‍💻 Contribuição

Contribuições são bem-vindas!  
Sinta-se à vontade para sugerir melhorias, reportar bugs ou abrir Pull Requests para novas funcionalidades.

1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -am 'Add nova funcionalidade'`)
4. Push para sua branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto é restrito ao uso interno da empresa. Para outras informações, consulte o responsável pelo projeto.

---

> Desenvolvido por [LoboProgrammingg](https://github.com/LoboProgrammingg) com 💙, Python, Django e Inteligência Artificial.
=======
# IA MARKDOWN FRONT



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.mti.mt.gov.br/mti/ia-markdown-front.git
git branch -M master
git push -uf origin master
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.mti.mt.gov.br/mti/ia-markdown-front/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/user/project/merge_requests/auto_merge/)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
>>>>>>> d0646fef3aef13f701620792f5775b9ee8aca109
