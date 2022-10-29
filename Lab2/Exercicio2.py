import os , time
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
         sub_caminho=os.path.join(caminho, i)
         tamanho=os.path.getsize(sub_caminho)
         ultima_att=time.ctime(os.path.getmtime(sub_caminho))
         dt_criacao=time.ctime(os.path.getctime(sub_caminho))
         author=os.stat(sub_caminho).st_uid
         print(tamanho,"bytes; \n Atualizado por último ",ultima_att,"; \n Criado ",dt_criacao,"\n\n","Autor:",author)
