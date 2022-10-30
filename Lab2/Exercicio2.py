import os 
import time
from pwd import getpwuid
tamanhos={}
diretorio= input("Digite o diretório")

print(diretorio)
print("Diretorio: ",diretorio)
arquivos=(os.listdir(diretorio))
for indices in arquivos:
      print("Arquivo: ",indices)
print()    
for indices in arquivos:
      sub_caminho=os.path.join(diretorio, indices)
      tamanho=os.path.getsize(sub_caminho)
      ultima_att=time.ctime(os.path.getmtime(sub_caminho))
      dt_criacao=time.ctime(os.path.getctime(sub_caminho))
      author_id=os.stat(sub_caminho).st_uid
      author=getpwuid(author_id).pw_name
      print("Arquivo: ",indices,"Tamanho: ",tamanho,"bytes"," Atualizado por último: ",ultima_att," Criado: ",dt_criacao," Autor:",author)
      print("\n")

for raiz, pastas, arquivos in os.walk(diretorio, topdown=True):
   for name in pastas:
      caminho=os.path.join(raiz, name)
      print("Diretorio: ",caminho)
      files=(os.listdir(caminho))
      
      for j in files:
         print("Arquivo: ",j)
      print()
      
      for i in files:
         sub_caminho=os.path.join(caminho, i)
         tamanho=os.path.getsize(sub_caminho)
         ultima_att=time.ctime(os.path.getmtime(sub_caminho))
         dt_criacao=time.ctime(os.path.getctime(sub_caminho))
         author_id=os.stat(sub_caminho).st_uid
         author=getpwuid(author_id).pw_name
         print("Arquivo: ",i,"Tamanho: ",tamanho,"bytes"," Atualizado por último: ",ultima_att," Criado: ",dt_criacao," Autor:",author)
         print()
           
