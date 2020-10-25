
import re
from afn import AFN

cargardesde = '([c|C]argar desde )(((\/\w+){2,}|\w+)(\.\w+))'
guardaren = '([G|g]uardar en )(((\/\w+){2,}|\w+)(\.\w+))'
agregartransicion = '([A|a]gregar transicion )((\d+) (\d+) ([a-z]|E))'
eliminartransicion = '([E|e]liminar transicion )((\d+) (\d+) ([a-z]|E))'
obtenerinicial = '([o|O]btener_inicial)'

if __name__ == "__main__":
  af = AFN()
  while 1:
    expresion = input()
    if bool(re.findall(r'^' + cargardesde + '$', expresion)) != False:
      fname = re.findall(r'^' + cargardesde + '$', expresion)
      af.cargar_desde(fname[0][1])
      # print( str(bool(re.search('^([c|C]argar desde )()$', expresion))).lower() )
    elif bool(re.findall(r'^' + guardaren + '$', expresion)) != False:
      gname = re.findall(r'^' + guardaren + '$', expresion)
      af.guardar_en(gname[0][1])
    elif bool(re.findall(r'^' + agregartransicion + '$', expresion)) != False:
      tname = re.findall(r'^' + agregartransicion + '$', expresion)
      af.agregar_transicion(tname[0][2], tname[0][3], tname[0][4])
    elif bool(re.findall(r'^' + eliminartransicion + '$', expresion)) != False:
      tname = re.findall(r'^' + eliminartransicion + '$', expresion)
      af.eliminame_transicion(tname[0][2], tname[0][3], tname[0][4])
    elif bool(re.findall(r'^' + obtenerinicial + '$', expresion)) != False:
      tname = re.findall(r'^' + obtenerinicial + '$', expresion)
      af.obtenerin_icial()
