class No:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None


class lista:
    def __init__(self):
        self.head = None
        self.next = None
        self.back = None
        self.sizeof = 0

    def tamanho(self):
        valor = int(self.sizeof)
        return valor

    def add(self, elem):
        if self.head:
            item = No(elem)
            anterior = self.head
            # anterior.next = item       ## não vai ser necessario pq a lista não será circular
            self.head = item
            item.next = anterior
            self.next = anterior
            anterior.back = item
            self.back = anterior.back
            self.sizeof += 1

        else:
            item = No(elem)
            self.head = item
            self.sizeof += 1
    def inicio_result(self,cont):
        item = self.head
        while (item.next!=None):
            item = item.next
        for i in range(cont):
            item = item.back
        return item
    
    def inicio(self):
        item = self.head
        while (item.next!=None):
            item = item.next
        return item

    # função para verificar se os numeros foram guardados na pilha corretamente.

    def print(self):
        item = self.head
        tam = self.tamanho()
        print("resultado da Multiplicação:")
        for i in range(tam):
            print(item.data, end="")
            item = item.next
        print("")


def mult(v1=lista(), v2=lista()):
    resultado = lista()     # nova lista para receber o resultado da multiplicação
    v1_head = v1             # fixando  a cabeça do lista
    result_inic = resultado   
     
    tam1 = v1.tamanho()     # pegando o tomanho da lista 1
    tam2 = v2.tamanho()
    print(tam1 ,tam2)
    up = 0
    valor = 0
    # vai até o inicio da pilha.
    v2 = v2.inicio()
    
    for i in range(tam2):
        cont = i
        v1 = v1_head.inicio()
        
        for j in range(tam1):
            if up != 0:     
                print ("numero v2 e numero v1")
                print(v2.data , v1.data)                # a variavel up simboliza 'sobe um'
                valor = v1.data * v2.data
                print (valor)
                print ("up")
                print(up)
                valor += up
                
                if valor > 99:
                    up = int(valor/100)
                    valor = valor - (up*100)
                else:
                    up = 0
            else:
                print ("numero v2 e numero v1")
                print(v2.data , v1.data) 
                valor = (v2.data * v1.data)
                if valor > 99:
                    up = int(valor/100)
                    valor = valor - (up*100)
                else:
                    up =0
                print(valor)


            v1 = v1.back
            if i >=1:
                resultado = result_inic.inicio_result(cont)
                if  resultado.back != None:
                    valor_anterior = resultado.data
                    print("segunda volta")
                    print(valor_anterior)
                    valor+=valor_anterior
                    print(valor)
                    
                    if valor > 99:
                        up2 = int(valor/100)
                        valor = valor - (up2*100) 
                        up+=up2
                   
                    resultado.data = valor
                    #resultado = resultado.back
                else:
                    valor_anterior = resultado.data
                    print("segunda volta")
                    print(valor_anterior)
                    valor+=valor_anterior
                    print(valor)
                    if valor > 99:
                        up2 = int(valor/100)
                        valor = valor - (up2*100) 
                        up+=up2

                    resultado.data = valor
                    if up>0:
                        result_inic.add(up)
                        up = 0
            else:
                result_inic.add(valor)
                valor = 0
                
            cont += 1
            #ultima execução do laço interno
        
        if up != 0 :
            print("aqui guardo o ultimo up")
            result_inic.add(up)
            up = 0
        
        
        result_inic.print()    
        v2 = v2.back
        #ultima execução do laço externo

       
    
def montagem(valor1, lista, tamanho) -> None:
    i = -1
    if tamanho %2 != 0:
        tamanho +=1
        while i >= tamanho:    
            valor = lista[i-1]
            valor = valor + lista[i]
            i = i-2
            valor = int(valor)
            valor1.add(valor)
        tamanho-=1
        valor = int(lista[tamanho])
        valor1.add(valor)
    else:
        while i >= tamanho:    
            valor = lista[i-1]
            valor = valor + lista[i]
            i = i-2
            valor = int(valor)
            valor1.add(valor)
        
def tam(lista):
    tamanho = len(lista)
    tamanho = tamanho * -1
    return tamanho