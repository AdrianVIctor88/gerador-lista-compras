# Gerador de Lista de Compras Inteligente 🛒

Um MVP (Mínimo Produto Viável) desenvolvido em Python e Flask para gerenciamento e otimização de listas de compras. O foco principal do projeto foi a aplicação prática de conceitos de **Arquitetura de Software**, **UX (Experiência do Usuário)** e o cumprimento estrito de **Requisitos Não Funcionais (RNFs)** de performance e portabilidade.

---

## 🚀 Funcionalidades & Diferenciais

* **Sanitização Automatizada de Dados:** O sistema trata strings removendo espaços extras (`.strip()`) e padronizando a capitalização (`.capitalize()`), evitando duplicidades por erro de digitação.
* **Agrupamento Inteligente (Regra de Negócio):** Se um item já existente for adicionado novamente, o backend detecta a duplicidade e soma a nova quantidade diretamente na linha correspondente, mantendo a consistência dos dados.
* **Checklist Dinâmico no Cliente:** Sistema de marcação (*checkbox* customizado com "X") que risca o item de forma instantânea via CSS, garantindo alta performance sem requisições desnecessárias ao servidor.
* **Layout Responsivo e Semântico:** HTML5 estruturado (`<main>`, `<header>`, `<footer>`) com acessibilidade básica e estilização moderna via Flexbox.

---

## 🛠️ Requisitos Não Funcionais (RNF) Implementados

### 1. RNF de Impressão (Otimização de Mídia)
Utilização de diretivas `@media print` no CSS para redefinir o layout no momento da impressão ou exportação para PDF. Elementos desnecessários (como campos de input e botões de ação) são ocultados automaticamente, gerando um formato limpo no estilo "cupom", ideal para uso físico no supermercado.

### 2. RNF de Desempenho e Economia de Banda
Toda a lógica visual de marcação de itens e checklist foi isolada no frontend utilizando seletores CSS avançados (`:checked ~`). Isso elimina o *overhead* de comunicação com o backend Flask apenas para fins estéticos.

---

## 📦 Tecnologias Utilizadas

* **Backend:** Python 3 + Flask (Microframework)
* **Frontend:** HTML5 Semântico + CSS3 (Flexbox & Media Queries)
* **Ícones:** Font Awesome (Integração via CDN)
* **Controle de Versão:** Git & GitHub

---

## 🔧 Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/AdrianVIctor88/gerador-lista-compras.git](https://github.com/AdrianVIctor88/gerador-lista-compras.git)
   cd gerador-lista-compras

2. **Crie e Ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   # No Windows (CMD):
   .\venv\Scripts\activate.bat

3. **Instale as dependências:**
   ```bash
   pip install flask

4. **Execute a aplicação:**
   ```bash
   python app.py

---
