
import re

class Thompson:
  simblos = '[a-z]+'
  ultima_operacion = ''
  ultima_operacion_union = []
  transiciones_der_or = {}
  transiciones_izq_or = {}

  def __init__(self, er):
    self.er = er

  def convertir(self, er, index):
    if len(er) == index + 1:
      return self.accion(er[index], er[index-1]) # retorna la transicion del estado
    else:
      transicione_der = self.convertir(er, index + 1) # retorna la transicio de lado derecho
      if er[index] == '|':
        self.transiciones_der_or.update(transicione_der)
        print(self.transiciones_der_or)
        return self.accion(er[index - 1], '0')
      elif self.accion(er[index], er[index-1]) != None and er[index + 1] != '|': # Hace la concatenacion
        transicione_izq = self.accion(er[index], er[index-1])
        max_valor_izq = max(transicione_izq[max(transicione_izq.keys())].values()) - 1
        return self.concatenacion(transicione_izq, transicione_der, max_valor_izq)
      else:
        self.ultima_operacion = '' 
        return transicione_der # retorna la transicion de la derecha para que no repita las misma operacion

  def modifica_er(self, er):
    idx = 0
    nueva_er = ''
    for e in er:
      if e != '+':
        nueva_er = nueva_er + e
      else:
        nueva_er = nueva_er + er[idx-1] + '*'
      idx = idx + 1
    return nueva_er

  def estado_base(self, simbolo):
    in_simbolo = simbolo
    init_estado = 1
    fin_estado = 2
    transicion = {
      init_estado: { in_simbolo: fin_estado }
    }
    return transicion

  def operador_estrella(self, simbolo, cambi_estado):
    estados = [1+cambi_estado,2+cambi_estado,3+cambi_estado,4+cambi_estado]
    init_estado = estados[0]
    fin_estado = estados[3]
    transicion = {
      init_estado: {'E1': estados[1], 'E2': fin_estado},
      estados[1]: {simbolo: estados[2]},
      estados[2]: {'E1': estados[1], 'E2': fin_estado}
    }
    return transicion
  def operador_positivo(self, simblo,):
    pass
  def operador_union(self, simbolo_izq, simbolo_der, cambi_estado):
    estados = [1,2,3,4,5,6]
    init_estado = estados[0]
    fin_estado = estados[5]
    

  def concatenacion(self, simbolo_izq, simbolo_der, cambi_estado):
    #print('izq', simbolo_izq)
    #print('der', simbolo_der)
    #print('c_e', cambi_estado)
    for key in simbolo_der:
      #print('key:',key)
      nuevo_afn_der = {
       (key + cambi_estado): {}
      }
      for keys in simbolo_der[key].keys():
        #print('keys:',keys)
        nuevo_afn_der[key + cambi_estado].update({keys : simbolo_der[key][keys] + cambi_estado})
        simbolo_izq.update(nuevo_afn_der)
        #print('nuevo',key,nuevo_afn_der)
    #print(simbolo_izq)
    return simbolo_izq

  def accion(self, e, e_siguiente):
    if e == '+':
      pass
    if len(self.ultima_operacion_union) != 0 and e != '*':
      return self.estado_base(e)
    elif bool(re.findall(self.simblos, e)) != False and self.ultima_operacion != '*':
      return self.estado_base(e)
    elif e == '*': # si la entra 'e' es un '*'
      self.ultima_operacion = e
      return self.operador_estrella(e_siguiente, 0) # retorna la transicion del 'e_siguiente*'
    elif e == '|':
      self.ultima_operacion_union.insert(len(self.ultima_operacion_union), e)
    else:
      return None
