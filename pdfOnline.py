import urllib3
import urllib.parse
import urllib.request
from io import StringIO, BytesIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import urllib3
import json 
import sys, locale

# baixa o arquivo
http = urllib3.PoolManager()
r = http.request('GET', 'http://www.bcb.gov.br/pec/GCI/PORT/readout/R20180608.pdf')
print(r.status)
print(type(r.data))
print(r.data)
print("==========================================================")
arqbytes = r.data.decode('latin-1') # latin-1 / utf-8 ......
pdfManager = PDFResourceManager()
convertBytes = StringIO() # BytesIO 
codec = sys.getdefaultencoding() # tipo de codificação do sistema do usuario
parametros = LAParams()
Arquivo = TextConverter(pdfManager, convertBytes, codec=codec, laparams=parametros)
leitor = PDFPageInterpreter(pdfManager, Arquivo)
arq = r.data
arqLocal = "R20180608.pdf"
urllib.request.urlretrieve('http://www.bcb.gov.br/pec/GCI/PORT/readout/R20180608.pdf', arqLocal)
arqtexto = open(arqLocal, 'rb') # lê o arquivo em bytesdices.t ==================
for page in PDFPage.get_pages(arqtexto):
    leitor.process_page(page)
    text = convertBytes.getvalue()
    text = text.replace(chr(272)," ") 
    print(text)
    f = open("indices.txt",'w') # salva como indices.txt, para ler em formato plain text na proxima intrução
    f.write(text)
arqtexto.close()




indiceIPCA_Hoje = [] # IPCA (%) 
indiceIGPDI_Hoje = [] # IGP-DI (%) 
indiceIGPM_Hoje = [] # IGP-M (%) 
indiceIPCFipe_Hoje = [] # IPC-Fipe (%) 
open_file = open('indices.txt', 'r')  # lê o arquivo em modo plainText. 
lines = open_file.readlines()
cnt = 0

# ================================
# layout dos dados
# ================================
for line in lines:
    line.strip()
    print(line)
    print("")
    if cnt == 37:
        indiceIPCA_Hoje.append(line)
    if cnt == 38:
        indiceIGPDI_Hoje.append(line)
    if cnt == 39:
        indiceIGPM_Hoje.append(line)        
    if cnt == 40:
        indiceIPCFipe_Hoje.append(line)            
    cnt = cnt + 1
open_file.close()
# exibe dados 
print("Resultado ----------:")
print("")
print("indiceIPCA Hoje:")
print(indiceIPCA_Hoje[0])
print("")
print("indiceIGPDI Hoje:")
print(indiceIGPDI_Hoje[0])
print("")
print("indiceIGPM Hoje:")
print(indiceIGPM_Hoje[0])
print("")
print("indiceIPCFipe Hoje:")
print(indiceIPCFipe_Hoje[0])