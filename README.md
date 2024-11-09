# Desafio A - Ordenação de Números

## Descrição do Problema

Dado um conjunto de números inteiros não negativos, você precisa ordená-los de acordo com os seguintes critérios:

1. **Primeiro os números pares** em **ordem crescente**.
2. **Depois os números ímpares** em **ordem decrescente**.

## Entrada

- A primeira linha contém um único inteiro positivo **N** (1 < N ≤ 10^5), que representa o número de valores inteiros que serão fornecidos nas próximas **N** linhas.
- As próximas **N** linhas contêm, cada uma, um valor inteiro não negativo.

## Saída

- Todos os valores lidos devem ser impressos em linhas separadas, de acordo com a seguinte ordem:
  - **Pares em ordem crescente**.
  - **Ímpares em ordem decrescente**.

## Exemplo de Entrada
```
10
4
32
34
543
3456
654
567
87
6789
98
```

## Exemplo de Saída
```
4
32
34
98
654
3456
6789
543
567
87
```

## Explicação

- **Pares**: 4, 32, 34, 98, 654, 3456 (ordenados em ordem crescente).
- **Ímpares**: 6789, 543, 567, 87 (ordenados em ordem decrescente).

## Implementação em Python

Aqui está o código utilizado para resolver o problema:

```python
# Número de elementos
N = int(input())

# Listas para pares e ímpares
pares = []
impares = []

# Separando pares e ímpares
for _ in range(N):
    valor = int(input())
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# Ordenação conforme critérios
pares.sort()
impares.sort(reverse=True)

# Exibindo a saída conforme o esperado
for numero in pares:
    print(numero)
for numero in impares:
    print(numero)
```

## Como o Código Funciona

1. **Entrada de Dados**:
   - Lê o número de elementos `N`.
   - Lê `N` números inteiros e os classifica como **pares** ou **ímpares**.

2. **Ordenação**:
   - Os números **pares** são ordenados em ordem crescente usando `sort()`.
   - Os números **ímpares** são ordenados em ordem decrescente usando `sort(reverse=True)`.

3. **Saída**:
   - Imprime os números pares em ordem crescente.
   - Em seguida, imprime os números ímpares em ordem decrescente.

## Complexidade

- A complexidade do algoritmo é **O(N log N)** devido à utilização da função `sort()`, o que é eficiente para o limite de 10^5 elementos.
- A solução é otimizada para atender ao limite de tempo exigido no problema.

## Como Executar o Código

Certifique-se de ter **Python 3** instalado no seu sistema. Para rodar o programa, siga estas etapas:

1. Crie um arquivo `input.txt` com o conteúdo de entrada.
2. Execute o script da seguinte forma:
    ```
    python ordenacao_numeros.py < input.txt
    ```

3. A saída será exibida no terminal.
