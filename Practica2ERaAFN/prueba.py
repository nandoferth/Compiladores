
in_er = '(vfd))'

def recuriva(er, index):
  if er[index] == '(':
    return False
  elif er[index] == ')':
    return True
  recuriva(er, index + 1)

print(recuriva(in_er, 0))