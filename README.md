# 🧮 Calculadora PySide6

![image](https://github.com/user-attachments/assets/8f1f935d-bd9e-48f2-9fad-5c4a57e8f29a)

Uma calculadora desktop funcional e intuitiva, desenvolvida com Python e a biblioteca PySide6 para interface gráfica. Este projeto visa demonstrar habilidades em desenvolvimento de GUIs, lógica de programação e boas práticas de estruturação de código.

## ✨ Funcionalidades

* **Operações Básicas:** Realiza operações de adição, subtração, multiplicação e divisão.
* **Suporte a Números Negativos:** Permite a entrada e o cálculo com números negativos, ampliando a versatilidade.
* **BackSpace (Apagar):** Funcionalidade para apagar o último caractere digitado no visor, oferecendo maior controle ao usuário.
* **Controle de Entrada:** Manipula a entrada de números e operadores de forma eficiente.
* **Interface Clara:** Design limpo e responsivo para uma experiência de usuário agradável.

## 🚀 Tecnologias Utilizadas

* **Python 3:** Linguagem de programação principal.
* **PySide6:** Framework para criação de interfaces gráficas (GUI).
* **PyInstaller:** Ferramenta utilizada para empacotar o aplicativo em um executável (`.exe`), facilitando a distribuição.

## 📁 Estrutura do Projeto

O projeto é organizado em módulos para facilitar a manutenção e a escalabilidade:

## 🛠️ Como Executar o Projeto

Siga os passos abaixo para rodar a calculadora no seu ambiente local:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Joao-Lucas-Code/calculadora-pyside6.git](https://github.com/Joao-Lucas-Code/calculadora-pyside6.git)
    cd calculadora-pyside6
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install pyside6
    ```
    *(Se você usou outras libs, adicione aqui. Idealmente, você teria um `requirements.txt`.)*

4.  **Execute o aplicativo:**
    ```bash
    python main.py
    ```

## 📦 Como Gerar o Executável (Opcional)

Para gerar uma versão executável do aplicativo (para Windows, macOS ou Linux, dependendo do seu SO), você pode usar o PyInstaller:

1.  **Instale o PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Gere o executável:**
    ```bash
    pyinstaller Calculadora.spec
    ```
    O executável será encontrado na pasta `dist/`.

## 📌 Status do Projeto

Concluído (Versão Inicial)

## 🤝 Contribuições

Sinta-se à vontade para abrir issues ou pull requests se tiver sugestões ou melhorias!

## 📧 Contato

* **João Lucas**
* **LinkedIn:** 'https://www.linkedin.com/in/joaogomes6/'

---

### **Principais Mudanças:**

* **Seção de Funcionalidades:** Adicionei os itens "Suporte a Números Negativos" e "BackSpace (Apagar)" com suas descrições.
* **Estrutura do Projeto:** Adicionei a pasta `assets/images` na estrutura sugerida (se você subiu a imagem para lá) e mencionei que `buttons.py` e `utils.py` podem ter relação com essas novas funcionalidades.
* **Link da Imagem:** Mantive o placeholder com o caminho `assets/images/calculadora_screenshot.png` para você ajustar conforme o local real da sua imagem no GitHub.
