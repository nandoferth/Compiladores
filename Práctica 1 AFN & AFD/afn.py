# Fernando Vizcaíno López
# 3CV6

import os
import re 

class AFN:

  transicion = ''
  eliminartransicion = ''
  obtenerinicial = ''
  obtenerfinales = ''
  establercer_inicial = ''
  establercer_final = ''
  error2 = 'FileNotFoundError: [Errno 2] No such file or directory:'
  error3 = 'No existe el archivo o el directorio'
  establecer = '([E|e]stablecer )((inicial )(inicial:([1-9]+|[1-9][0-9]+))|(final )(finales:([2-9]+|[1-9][0-9]+)))'

  def __init__(self):
    pass

  def cargar_desde(self, fname):
    f = open(fname, "a")
    f.close()

  def guardar_en(self, gname):
    if os.path.sifile(gname):
      linea = self.verificar
      if linea != '' and self.verifica_archivo(gname) != False:
        if self.transicion != '':
          self.edita_archivo(gname, linea)
        elif self.eliminartransicion != '':
          self.eliminar_transicion(gname, linea)
        elif self.establercer_inicial != '' or self.establercer_final != '':
          self.establercer_inicial_final(gname, linea)
        self.limpia()
      # else:
    else:
      print(self.error3)

  def agregar_transicion(self, tinicio, tfin, tsimbolo):
    self.transicion = tinicio + '->' + tfin + ',' + tsimbolo

  def eliminame_transicion(self, tinicio, tfin, tsimbolo):
    self.eliminartransicion = tinicio + '->' + tfin + ',' + tsimbolo
    print(self.eliminartransicion)

  def eliminar_transicion(self, gname, linea):
    f = open(gname, "r")
    lines = f.readlines()
    f.close()
    f = open(gname, "w")
    for x in lines:
      if x != linea + '\n':
        f.write(x)
    f.close()

  def obtener_inicial_final(self, intOend, oiname):
    if os.path.isfile(oiname):
      f = open(oiname, "r")
      inicialline = f.readline()
      if intOend != 'f':
        if bool(re.findall(r'^(inicial:([1-9]+|[1-9][0-9]+))$', inicialline)) != False:
          self.obtenerinicial = re.findall(r'^(inicial:([1-9]+|[1-9][0-9]+))$', inicialline)[0][0]
        else:
          self.obtenerinicial = '' 
      else:
        inicialline = f.readline()
        if bool(re.findall(r'^(finales:([2-9]+|[1-9][0-9]+))$', inicialline)) != False:
          self.obtenerfinales = re.findall(r'^(finales:([2-9]+|[1-9][0-9]+))$', inicialline)[0][0]
        else:
          self.obtenerfinales = ''
      f.close()
    else:
      print(self.error2, oiname)

  def setEstablercer_inicial_final(self, inicial, final):
    self.establercer_inicial = inicial
    self.establercer_final = final
 
  def establercer_inicial_final (self, gname, linea):
    if os.path.isfile(gname):
      f = open(gname, "r")
      lines = f.readlines()
      f.close
    else:
      print(self.error2, oiname)

  def edita_archivo(self, gname, linea):
    f = open(gname, "a")
    f.write(linea + '\n')
    f.close()

  def verifica_archivo(self,gname):
    verifica = False
    f = open(gname, "r")
    if bool(re.findall(r'^(inicial:)([1-9]+|[1-9][0-9]+)$', f.readline())) != False:
      if bool(re.findall(r'^(finales:)([2-9]+|[1-9][0-9]+)$', f.readline())) != False:
        verifica = True
      elif self.establercer_final !=  '':
        verifica = True
    elif self.establercer_inicial != '':
      verifica = True
    f.close()
    return verifica

  def limpia (self):
    self.transicion = ''
    self.eliminartransicion = ''
    self.establercer_inicial = ''
    self.establercer_final = ''

  def verifica (self):
    if self.transicion != '':
      linea = self.transicion
    elif self.eliminartransicion != '':
      linea = self.eliminartransicion
    elif self.establercer_inicial != '':
      linea = self.establercer_inicial
    elif self.establercer_final != '':
      linea = self.establercer_final
    else:
      linea = ''
    return linea
