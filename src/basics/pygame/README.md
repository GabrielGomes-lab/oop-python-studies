# Pygame Examples

Este diretório contém exemplos e estudos sobre a biblioteca Pygame.

## Estrutura de Pastas

O diretório pygame está organizado da seguinte forma:

```
pygame/
├── chapter5.py              # Conceitos básicos do Pygame
├── PygameDemo1_OneImage/    # Demo 1: Exibindo imagens
│   ├── __init__.py
│   └── main.py
├── PygameDemo2_Animation/   # Demo 2: Animações simples
│   ├── __init__.py
│   └── main.py
├── PygameDemo3_UserInput/   # Demo 3: Entrada do usuário
│   ├── __init__.py
│   └── main.py
└── README.md                # Este arquivo
```

## Como Criar uma Nova Pasta Dentro do Diretório Pygame

Para criar uma nova pasta (diretório) dentro do diretório pygame, siga estes passos:

### Método 1: Usando o Terminal/Linha de Comando

1. Navegue até o diretório pygame:
   ```bash
   cd src/basics/pygame
   ```

2. Crie uma nova pasta usando o comando `mkdir`:
   ```bash
   mkdir NomeDaNovaPasta
   ```

   Por exemplo, para criar uma pasta chamada "PygameDemo4_Collision":
   ```bash
   mkdir PygameDemo4_Collision
   ```

3. (Opcional) Crie um arquivo `__init__.py` para torná-la um pacote Python:
   ```bash
   touch PygameDemo4_Collision/__init__.py
   ```

### Método 2: Usando Python

Você também pode criar pastas programaticamente usando Python:

```python
import os

# Caminho para o novo diretório
novo_diretorio = "src/basics/pygame/PygameDemo4_Collision"

# Criar o diretório
os.makedirs(novo_diretorio, exist_ok=True)

# Criar arquivo __init__.py
with open(os.path.join(novo_diretorio, "__init__.py"), "w") as f:
    f.write('"""Nova demo do Pygame"""\n')
```

### Método 3: Usando o Explorador de Arquivos (Windows/Mac/Linux)

1. Navegue até a pasta `src/basics/pygame` no explorador de arquivos
2. Clique com o botão direito e selecione "Nova Pasta" ou "New Folder"
3. Digite o nome da nova pasta e pressione Enter

## Convenções de Nomenclatura

- Use nomes descritivos que indiquem o propósito da pasta
- Para demos numeradas, use o formato: `PygameDemoX_Description`
- Use PascalCase ou snake_case de forma consistente
- Exemplos:
  - `PygameDemo1_OneImage`
  - `PygameDemo2_Animation`
  - `game_project_1`
  - `sprites_examples`

## Estrutura Recomendada para Cada Demo

Dentro de cada pasta de demo, recomenda-se a seguinte estrutura:

```
PygameDemoX_Description/
├── __init__.py          # Torna o diretório um pacote Python
├── main.py              # Arquivo principal do exemplo
├── README.md            # (Opcional) Documentação específica
└── assets/              # (Opcional) Imagens, sons, etc.
    ├── images/
    └── sounds/
```

## Executando os Exemplos

Para executar um exemplo específico, navegue até o diretório raiz do projeto e execute:

```bash
python -m src.basics.pygame.PygameDemo1_OneImage.main
```

Ou navegue até a pasta do exemplo e execute:

```bash
cd src/basics/pygame/PygameDemo1_OneImage
python main.py
```

## Recursos Adicionais

- [Documentação Oficial do Pygame](https://www.pygame.org/docs/)
- [Tutoriais do Pygame](https://www.pygame.org/wiki/tutorials)
