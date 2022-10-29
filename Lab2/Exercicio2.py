import os 
tamanhos={}
diretorio=os.getcwd()
print(diretorio)
print("Diretorio: ",diretorio)
print(os.listdir(diretorio))

print("\n")
for raiz, pastas, arquivos in os.walk(diretorio, topdown=False):
   for name in pastas:
      caminho=os.path.join(raiz, name)
      print("Diretorio: ",caminho)
      #for nome_arquivo in (caminho):
      files=(os.listdir(caminho))
      print(files)
      for i in files:
         #print(os.path.getsize(caminho))
         sub_caminho=os.path.join(caminho, i)
         tamanho=os.path.getsize(ok)
         ultima_att=os.path.getmtime(sub_caminho)
         #print(os.path.getmtime(filename))
         dt_criacao=os.path.getctime(sub_caminho)
         #print(os.path.getctime(filename))
         print(tamanho)
  
   
      #tamanhos[name]=(os.stat(os.path.join(raiz, name)).st_size)
   
     
#final=sorted(tamanhos.items(),reverse=True, key=lambda x:x[1])
#print(final)
