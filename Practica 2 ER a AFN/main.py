from thompson import Thompson
er = 'fd*'
def main():
  th = Thompson(er)
  print(th.convertir_er_afn(th.modifica_er(er)))
  # estado = ''
  # const_der = (th.operador_estrella(estado, 0))
  # const_izq = (th.operador_estrella('b', 0))
  # th.concatenacion(const_der, max(const_izq[2].keys()))
  # for key in const:
    # for keys in const[key].keys():
      # nuevo_const = {
        # key + 1: { keys: const[key][keys] + 1 }
      # }
  # print(nuevo_const)
main()
