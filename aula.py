# class computador():
#     marca = ''
#     memoria = ''
#     placaV = ''

# Comp1 = computador()
# Comp1.marca = "Daten"
# Comp1.memoria = "R$2000"
# Comp1.placaV = "NVIDIA"

# print ("Detalhes do computador 1")
# print (Comp1.marca)



# class Computador(object):
#     def __init__(self):
#         self.marca = ''
#         self.preço = ''
#         self.placaV = ''
#         self.processador = ''
#     def set_computador(self):
#         self.marca = input("Digite a marca do computador: ")
#         self.preço = input("Digite o preço do computador: ")
#         self.placaV = input("Digite a placa de vídeo: ")
#         self.processador = input("Digite o processador: ")
#     def get_computador(self):
#         print("Marca do computador:", self.marca)
#         print("Preço do computador:", self.preço)
#         print("Placa de vídeo do computador:", self.placaV)
#         print("Processador do computador:", self.processador)
        
# A = Computador()
# print("set")
# A.set_computador()
# print("get")
# A.get_computador()

class Computador():
    def __init__(self, marca, memoria, placaVideo):
        self.marca = marca
        self.memoria = memoria
        self.placaV = placaVideo

    def get_computador(self):
        print("Marca do computador:", self.marca)
        print("Memória do computador:", self.memoria)
        print("Placa de vídeo do computador:", self.placaV)
        
A = Computador("Pichau", "16gB", "Nvidea")
A.get_computador()

