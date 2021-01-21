# Vizcaíno López Fernando

import re

class Thompson:
  simblos = '[a-z]+'
  ultima_operacion = ''
  ultima_operacion_union = []
  transiciones_der_or = {}
  transiciones_izq_or = {}
  cont_transiciones_or = 0
  grupo_transiciones = {}
  orden_grupo = []
  afn = {}

  def __init__(self, er):
    self.er = er
  
  def set_grupo_transiciones(self, transicion, grupo_num):
    self.grupo_transiciones.update({ grupo_num: transicion })

  def get_grupo_transiciones(self):
    return self.grupo_transiciones
  
  def get_afn(self):
    return self.afn

  def convertir_er_afn(self, er):
    self.get_grupo(er, 0, 1)
    for grupo in range(len(self.grupo_transiciones) - 1, 0, -1):
      if len(self.afn) != 0:
        max_estado_transicion_izq = max(self.afn[max(self.afn)].values())
      else:
        grupo_num = max(self.grupo_transiciones)
        estado = max(self.grupo_transiciones[grupo])
        max_estado_transicion_izq = max(self.grupo_transiciones[grupo_num][estado].values())
      self.concatenar_grupo(max_estado_transicion_izq, self.grupo_transiciones[grupo])

  def get_grupo(self, er, idx, grupo_num):
    grupo = ''
    while idx < len(er): # 1er -> (0 < 10) |set_grupo_transiciones
      if er[idx] == '(':
        self.orden_grupo.append(grupo_num + 1)
        idx = self.get_grupo(er[(idx + 1):], 0, grupo_num + 1) + idx
      elif er[idx] == ')':
        if grupo != '':
          self.convierte_grupo_afn(grupo, grupo_num)
        return idx + 1
      else:
        grupo = grupo + er[idx]
        if idx == len(er) - 1:
          self.convierte_grupo_afn(grupo, grupo_num)  
      idx = idx + 1
    #return self.convertir_grupo_afn(er, 0)
  
  def convierte_grupo_afn(self, grupo_er, grupo_num):
    grupo_afn = self.convertir_grupo_afn(grupo_er, 0) # -- 1
    if self.cont_transiciones_or != 0: # -- 1
      grupo_afn = self.operador_union(grupo_afn) # -- 1
    self.set_grupo_transiciones(grupo_afn, grupo_num) # -- 1

  def convertir_grupo_afn(self, er, index):
    if len(er) == index + 1:
      return self.operaciones(er[index], er[index-1])
    else:
      transicione_der = self.convertir_grupo_afn(er, index + 1)
      if er[index] == '|':
        self.cont_transiciones_or += 1
        self.transiciones_der_or.update({self.cont_transiciones_or: {}})
        self.transiciones_der_or[self.cont_transiciones_or].update(transicione_der)
        return self.operaciones(er[index - 1], er[index - 2])
      elif self.operaciones(er[index], er[index-1]) != None and er[index + 1] != '|' and er[index + 1] != '*':
        transicione_izq = self.operaciones(er[index], er[index-1])
        max_valor_izq = max(transicione_izq[max(transicione_izq.keys())].values()) - 1
        return self.concatenacion(transicione_izq, transicione_der, max_valor_izq)
      else:
        self.ultima_operacion = '' 
        return transicione_der

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

  def operador_union(self, simbolo_izq):
    simbolo_izq_up = {}
    simbolo_izq_up = {
      1: {'E1': 2}
    }
    for grupo in range(len(self.transiciones_der_or), 0, -1):
      simbolo_izq_up.update(self.operador_union_up(simbolo_izq))
      max_transicion_izq = max(simbolo_izq_up[max(simbolo_izq_up)].values())
      simbolo_izq_up.update({1: {'E1':2 ,'E2': max_transicion_izq + 1}})
      for estado in self.transiciones_der_or[grupo].keys():
        simbolo_izq_up.update({
          max_transicion_izq: {},
          estado + max_transicion_izq: {}
        })
        for simbolo in self.transiciones_der_or[grupo][estado].keys():
          simbolo_izq_up[estado + max_transicion_izq].update({simbolo: self.transiciones_der_or[grupo][estado][simbolo] + max_transicion_izq})
      simbolo_izq_up.update({
        max_transicion_izq: {'E3': max(simbolo_izq_up[max(simbolo_izq_up)].values()) + 1},
        max(simbolo_izq_up[max(simbolo_izq_up)].values()): {'E4': max(simbolo_izq_up[max(simbolo_izq_up)].values()) + 1}
      })
      simbolo_izq.update(simbolo_izq_up)
    self.transiciones_der_or.clear()
    return simbolo_izq

  def operador_union_up(self,simbolo_izq):
    copy_simbolo_izq = {}
    for estado in simbolo_izq:
      nuevo_afn_up = {
        (estado + 1): {}
      }
      for transicion in simbolo_izq[estado].keys():
        nuevo_afn_up[(estado + 1)].update({transicion : simbolo_izq[estado][transicion] + 1})
        copy_simbolo_izq.update(nuevo_afn_up)
    return copy_simbolo_izq
 
  def concatenar_grupo(self, max_estado_transicion_izq, transicion_der):
    print(transicion_der)
    for estado in transicion_der:
      for simbolo in transicion_der[estado].keys():
        self.afn.update({
          (estado + max_estado_transicion_izq): { simbolo: transicion_der[estado][simbolo] + max_estado_transicion_izq}
        })
    self.afn.update(transicion_der)
  
  def concatenacion(self, simbolo_izq, simbolo_der, cambi_estado):
    for key in simbolo_der:
      nuevo_afn_der = {
       (key + cambi_estado): {}
      }
      for keys in simbolo_der[key].keys():
        nuevo_afn_der[key + cambi_estado].update({keys : simbolo_der[key][keys] + cambi_estado})
        simbolo_izq.update(nuevo_afn_der)
    return simbolo_izq

  def operaciones(self, e, e_siguiente):
    if e == '+':
      pass
    if len(self.ultima_operacion_union) != 0 and e != '*':
      return self.estado_base(e)
    elif bool(re.findall(self.simblos, e)) != False and self.ultima_operacion != '*':
      return self.estado_base(e)
    elif e == '*':
      self.ultima_operacion = e
      return self.operador_estrella(e_siguiente, 0)
    elif e == '|':
      self.ultima_operacion_union.insert(len(self.ultima_operacion_union), e)
    else:
      return None
