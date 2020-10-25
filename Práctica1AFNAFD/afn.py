
import os
import re 

class AFN:

  transicion = ''
  eliminartransicion = ''
  obtenerinicial = ''

  def __init__(self):
    pass

  def cargar_desde(self, fname):
    f = open(fname, "a")
    f.close()
  
  def guardar_en(self, gname):
    if os.path.isfile(gname):
      linea = self.verifica()
      if linea != '' and self.verifica_archivo(gname) != False:
        if self.transicion != '':
          print(linea)
          self.edita_archivo(gname, linea)
        elif self.eliminartransicion != '':
          print(linea)
          self.eliminar_transicion(gname, linea)
        else:
          pass  
        self.limpia()
      else:
        print('No hay acciones o no hay inicio y final')

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

  def obtenerin_icial(self):
    f = open(gname, "r")
    if bool(re.findall(r'^(inicial:1)$', f.readline())) != False:
      self.obtenerinicial = 'inicial:1'
    f.close()
    print(self.obtenerinicial)

  def edita_archivo(self, gname, linea):
    f = open(gname, "a")
    f.write(linea + '\n')
    f.close()
  
  def verifica_archivo(self,gname):
    verifica = False
    print('entro')
    f = open(gname, "r")
    if bool(re.findall(r'^(inicial:1)$', f.readline())) != False:
      if bool(re.findall(r'^(finales:)([2-9]+|[1-9][0-9]+)$', f.readline())) != False:
        print('ok')
        verifica = True
    f.close()
    return verifica

  def limpia (self):
    self.transicion = ''
    self.eliminartransicion = ''
  
  def verifica (self):
    if self.transicion != '':
      linea = self.transicion
    elif self.eliminartransicion != '':
      linea = self.eliminartransicion
    else:
      linea = ''
    return linea