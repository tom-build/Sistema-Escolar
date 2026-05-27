# Sistema Escolar - Gerenciador Acadêmico

Sistema desktop desenvolvido em Python para gerenciamento acadêmico, permitindo o controle centralizado de alunos, professores, turmas, notas e registros escolares.

---

# Funcionalidades

- Cadastro de alunos
- Cadastro de professores
- Gerenciamento de turmas
- Controle de notas
- Registro de informações acadêmicas
- Operações CRUD completas
- Persistência de dados com banco relacional
- Interface gráfica desktop
- Organização centralizada das informações escolares

---

# Tecnologias Utilizadas

- Python
- SQLite
- Tkinter / CustomTkinter
- PyInstaller
- Git
- GitHub

---

# Estrutura do Projeto

```txt
sistema-escolar/
│
├── Schola.py
├── escola.db
├── requirements.txt
├── .gitignore
├── README.md
├── Macaco-School.spec
│
├── build/
├── dist/
└── venv/
```

---

# Objetivo do Projeto

O projeto foi desenvolvido com o objetivo de centralizar e organizar processos acadêmicos, permitindo gerenciamento eficiente de dados escolares através de uma aplicação desktop simples, funcional e escalável.

A aplicação foi estruturada utilizando princípios de:

- organização arquitetural
- separação de responsabilidades
- código limpo
- manutenção
- escalabilidade

---

# Banco de Dados

O sistema utiliza banco de dados relacional SQLite para armazenamento local das informações acadêmicas.

As operações implementadas incluem:

- criação de registros
- consulta de dados
- atualização de informações
- remoção de registros

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone SEU_LINK_DO_REPOSITORIO
```

---

## 2. Acessar a pasta do projeto

```bash
cd sistema-escolar
```

---

## 3. Criar ambiente virtual

```bash
python -m venv venv
```

---

## 4. Ativar ambiente virtual

### Windows

```powershell
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## 5. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 6. Executar o sistema

```bash
python Schola.py
```

---

# Gerar Executável

O projeto pode ser compilado utilizando PyInstaller.

```bash
pyinstaller Macaco-School.spec
```

O executável será gerado na pasta:

```txt
dist/
```

---

# Estrutura do Banco de Dados

Exemplo simplificado das entidades do sistema:

- Alunos
- Professores
- Turmas
- Notas
- Registros Acadêmicos

---

# Aprendizados Aplicados

Durante o desenvolvimento foram aplicados conhecimentos relacionados a:

- modelagem de dados
- banco de dados relacional
- operações CRUD
- manipulação de dados
- persistência de informações
- organização de projetos
- versionamento com Git
- estruturação de aplicações desktop

---

# Melhorias Futuras

- Sistema de autenticação
- Controle de permissões
- Exportação de relatórios
- Dashboard administrativo
- Integração com banco de dados remoto
- API REST
- Sistema web

---

# Versionamento

Projeto versionado utilizando Git e hospedado no GitHub.

---

# Autor

Tom  
Estudante de Análise e Desenvolvimento de Sistemas.

---

# Licença

Este projeto foi desenvolvido para fins educacionais e de aprendizado.