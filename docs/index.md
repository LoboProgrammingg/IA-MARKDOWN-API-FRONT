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