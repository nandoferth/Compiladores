# Fernando Vizcaíno López
# 3CV6

import re
from afn import AFN

cargardesde = '([c|C]argar desde )(((\/\w+){2,}|\w+)(\.\w+))'
guardaren = '([G|g]uardar en )(((\/\w+){2,}|\w+)(\.\w+))'
agregartransicion = '([A|a]gregar transicion )((\d+) (\d+) ([a-z]|E))'
eliminartransicion = '([E|e]liminar transicion )((\d+) (\d+) ([a-z]|E))'
obtener = '([o|O]btener [inicial |final ]+)(((\/\w+){2,}|\w+)(\.\w+))'
establecer = '([E|e]stablecer )((inicial )(inicial:([1-9]+|[1-9][0-9]+))|(final )(finales:([2-9]+|[1-9][0-9]+)))'

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
      tename = re.findall(r'^' + eliminartransicion + '$', expresion)
      af.eliminame_transicion(tename[0][2], tename[0][3], tename[0][4])
    elif bool(re.findall(r'^' + obtener + '$', expresion)) != False:
      i_f_obtener = re.findall(r'^' + obtener + '$', expresion)
      af.obtener_inicial_final(i_f_obtener[0][0][8], i_f_obtener[0][1])
    elif bool(re.findall(r'^' + establecer + '$', expresion)) != False:
      i_f_establecer = re.findall(r'^' + establecer + '$', expresion)
      print(i_f_establecer[0][3])
      print(i_f_establecer[0][6])
      # print(i_f_establecer = re.findall(r'^' + establecer + '$', expresion)[0][1])
      # print(i_f_establecer = re.findall(r'^' + establecer + '$', expresion)[0][2])
      # i_f_establecer = re.findall(r'^' + establecer + '$', expresion)
      # af.establecer_inicial_final(establecer[0][0][8], establecer[0][1])
    else:
      print(expresion, ': orden no encontrada')