# Simulador de Autômatos Finitos

Trabalho da disciplina de Linguagens Formais e Autômatos. Simula o funcionamento de Autômatos Finitos Determinísticos (AFD) e Não-Determinísticos (AFN, incluindo transições-épsilon), processando palavras a partir de definições carregadas de arquivos JSON.

**Um detalhe importante:** o projeto foi feito utilizando apenas bibliotecas nativas do Python (como `json` e `pathlib`). Ou seja, **não possui dependências externas e você não precisa baixar nada via pip**. É só clonar e rodar!

## Funcionalidades

- Carrega automaticamente todos os autômatos definidos em `data/*.json`
- Classifica cada autômato como AFD ou AFN, detectando transições-épsilon e não-determinismo automaticamente
- Simula o processamento de palavras, exibindo o caminho percorrido entre os estados
- Detecta e avisa sobre arquivos JSON malformados durante o carregamento
- Menu interativo com três modos: rodar os testes de um autômato, rodar os testes de todos de uma vez, ou testar uma palavra digitada manualmente

## Estrutura do projeto

```
simulador-automato/
├── main.py              # Script principal (menu interativo)
├── automato.py          # Classe Automato: lógica de simulação (AFD/AFN)
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    ├── AFD_maior.json
    ├── AFD_simples.json
    ├── AFN_epsilon.json
    ├── AFn_maior.json
    └── AFN_simples.json
```

## Formato dos arquivos JSON

Cada autômato é descrito em um arquivo separado dentro de `data/`:

```json
{
  "Sigma": ["a", "b"],
  "q0": "q0",
  "F": ["q3"],
  "delta": {
    "q0": {"a": [], "b": [], "": ["q1", "q4"]},
    "q1": {"a": ["q2"], "b": [], "": []}
  },
  "palavras_teste": ["ab", "ba", "aa"]
}
```

| Campo | Descrição |
|---|---|
| `Sigma` | Alfabeto do autômato |
| `q0` | Estado inicial |
| `F` | Lista de estados finais (de aceitação) |
| `delta` | Função de transição: estado → símbolo → lista de estados destino. Uma chave `""` representa transição-épsilon |
| `palavras_teste` | Palavras usadas nos testes automáticos |

## Como rodar

Requer Python 3.8 ou superior.

```bash
git clone https://github.com/demasiadopedro/simulador-automato.git
cd simulador-automato

python3 -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows


python3 main.py
```

## Uso

Ao rodar, o menu interativo é exibido:

```
1. Rodar automato
2. Testar todos os automatos
3. Testar uma palavra
4. Sair
```

- **1** — escolhe um autômato pelo número e roda as palavras de teste definidas no campo `palavras_teste` do próprio JSON
- **2** — roda os testes de todos os autômatos encontrados em `data/`, em sequência
- **3** — testa uma palavra digitada na hora contra um autômato escolhido, mostrando se foi aceita ou rejeitada
- **4** — encerra o programa

## Sobre

**Video de Apresentação:** __