
#Vizcaíno Lopez Fernando

import re

class Afd:

  epsilon = 'E[0-9]*'
  simbolo = '[a-z]+'
  afd = {}
  destados = {} # A: *, B +, ...
  destados_estados = {} # A: {estados}, B: {estados}, ... 
  epsilon_inicial = []
  a = {} # simbolos: a,b,c,... del afn
  marca_T = '' # marcador temporal del estados: A,B,C...

  def __init__(self): # This is the constructor method.
    pass

  def set_afd(self, T, a, U):
    self.afd[T].update({a: U})
  
  def e_cerradura(self, transicion_inicial, afn, estado_a):
    e_cerradura = []
    for estado in transicion_inicial:
      if bool(re.findall('^'+self.epsilon+'$', estado)):
        e_cerradura.extend(self.e_cerradura(afn[transicion_inicial[estado]], afn, transicion_inicial[estado]))
    e_cerradura.append(estado_a)
    return e_cerradura

  def get_destados_estados(self):
    return self.destados_estados

  def set_destados(self, nuevo_estado, marca, estados):
    self.destados.setdefault(nuevo_estado, marca)
    self.destados_estados.setdefault(nuevo_estado, estados)

  def hay_estado_T_destados(self):
    for estado in self.destados:
      if self.destados[estado] == '+':
        self.marca_T = estado
        return True
    return False
  
  def marca_destados(self, estado, marca):
    self.destados.update({estado: marca})
  
  def get_estado(self, afn):
    for estado in afn:
      for simbolo in afn[estado]:
        if bool(re.findall('^'+self.simbolo+'$', simbolo)):
          self.a.update({
            simbolo: 1
          })
  
  def mover(self, T, a, afn):
    estado_nuevo = []
    for estado in T:
      if estado == max(afn[max(afn)].values()):
        return estado_nuevo
      for simbolo in afn[estado]:
        if simbolo == a:
          estado_nuevo.append(afn[estado][simbolo])
    return estado_nuevo
  
  def U_no_esta_e_cerradura(self, U):
    for estados in self.destados_estados:
      if U == self.destados_estados[estados]:
        return False
    return True
  
  def Dtran(self, T, a, U):
    for estado in self.destados_estados:
      if U == self.destados_estados[estado]:
        self.set_afd(T, a, estado)

  def subconjuntos(self, afn):
    T = []
    U = [] # estados: 1,2,3,4... del afn
    self.get_estado(afn)
    self.epsilon_inicial = sorted(self.e_cerradura(afn[min(afn)], afn, min(afn)))
    self.set_destados('A', '+', self.epsilon_inicial)
    while self.hay_estado_T_destados():
      self.afd.update({self.marca_T: {}})
      T = self.destados_estados[self.marca_T]
      self.marca_destados(self.marca_T, '*')
      for a in self.a: # a = a, a = b, ...
        U.clear()
        for estado in self.mover(T, a, afn): # mover(T, a), T = {estdos}, a = a
          if estado != max(afn[max(afn)].values()):
            U.extend(sorted(self.e_cerradura(afn[estado], afn, estado))) # U = e-cerradura()
          else:
            U.append(estado)
        tem_U = U.copy()
        if self.U_no_esta_e_cerradura(tem_U):
          self.set_destados(chr(ord(max(self.destados))+1), '+', tem_U)
          #self.set_destados(chr(ord(max(self.destados))+1), '+', U)
        self.Dtran(self.marca_T, a, tem_U)
