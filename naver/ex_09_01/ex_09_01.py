di = {'kim': 2, 'park': 2, 'son': 1, 'lee': 4}

def func_get(dic_var, name, dft):
  if name in dic_var:
      return dic_var[name]
  else:      
      return dft

print('내장함수 get 결과', di.get('lee',10))
print('함수fuct_get 결과', func_get(di,'lee',10))
print('내장함수 get 결과', di.get('jung',10))
print('함수fuct_get 결과', func_get(di,'jung',10))