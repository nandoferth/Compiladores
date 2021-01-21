
import re
import pandas as pd

class ll1:
  terminsles = '[a-z]{1}'
  no_terminales = '[A-Z]{1}'
  T = ['A', 'C', 'D']
  N = ['a', 'b', 'c', '$']
  tablaLL1 = {
    'A': {'a': [], 'b': [], 'c':[], '$':[]},
    'C': {'a': [], 'b': [], 'c':[], '$':[]},
    'D': {'a': [], 'b': [], 'c':[], '$':[]}
  }
  producciones = [
    {'D': ['a','b','C']},
    {'D': ['b','A','C']},
    {'C': ['A','b']},
    {'A': ['a','D']},
    {'D': ['c','C','A']}
  ]

  def get_tablaLL1 (self):
    return self.tablaLL1

  def get_producciones (self):
    return self.producciones
  
  def get_no_terminales (self):
    return self.N

  def get_terminales (self):
    return self.T

  def check_alfa (self, expresion): # Compruebo que alfa sea un terminales o no terminales
    if bool(re.findall(r'^' + self.terminsles , expresion)): # Terminales
      return list(expresion[0])
    else:
      return self.Primero(expresion[0])

  def Primero (self, no_terminal):
    terminales = []
    alfa = ''
    for produccion in self.producciones:  # ( 'D': ['a','b','C'] in producciones )
      if max(produccion.keys()) == no_terminal: # uso max para que me regrese un solo valor y no un diccionario
        alfa = list(produccion.values())[0][0]  # alfa va ser igual al terminal o no_terminal
        if bool(re.findall(r'^' + self.no_terminales, alfa)): # Compruebo si es terminal o no terminal
          terminales.extend(self.Primero(alfa)) # extend() modifica la lista original
        else:
          terminales.append(alfa)
    return terminales

  def Siguiente (self, alfa):
    terminales = []
    ter_noTer = ''
    for produccion in self.producciones:
      for index, alfas in enumerate(list(produccion.values())[0]):
        if (alfas == alfa):
          #print(alfa, list(produccion.values())[0][index+1:], max(produccion.keys()))
          if list(produccion.values())[0][index+1:] == []:
            terminales.extend(self.Siguiente(max(produccion.keys())))
          else:
            return self.check_alfa(ter_noTer.join(list(produccion.values())[0][index+1:]))
    return terminales

  def recorre_producciones (self):  # Es el paso 2 para Recorre todas las producciones
    str1 = ''
    numero_produccion = 1
    for produccion in self.producciones:
      # Se empezara asignar los valores para la tabla LL1 
      self.tabla_LL1(max(produccion.keys()), numero_produccion, self.check_alfa(str1.join(list(produccion.values())[0])))
      numero_produccion += 1
  
  def tabla_LL1 (self, no_terminal, num_produccion, terminales):
    for terminal in terminales:
     self.tablaLL1[no_terminal][terminal].append(num_produccion)
