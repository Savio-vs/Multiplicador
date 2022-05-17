from func import*

valor1 = lista()
valor2 = lista()
v1 = "12532"
v2 = "1337"
# retorna o tamanho da string (quantos caracteres)
tam1 = tam(v1)
tam2 = tam(v2)

# separando o numero v1 em blocos de 2 digitos e guardando em uma pilha cada bloco.
montagem(valor1, v1, tam1)
montagem(valor2, v2, tam2)

mult(valor1, valor2)