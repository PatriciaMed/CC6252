import os 
tamanhos={}
diretorio=os.getcwd()
print(diretorio)
for raiz, pastas, arquivos in os.walk(diretorio, topdown=False):
   for name in arquivos:
      print(os.path.join(raiz, name))
      tamanhos[name]=(os.stat(os.path.join(raiz, name)).st_size)
   for name in pastas:
      print(os.path.join(raiz, name))
     
final=sorted(tamanhos.items(),reverse=True, key=lambda x:x[1])
print(final)