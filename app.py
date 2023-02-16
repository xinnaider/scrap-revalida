from PyPDF2 import PdfReader
import re
import os

clear = lambda: os.system('cls')
clear()

#seleciono o arquivo
reader = PdfReader("reva.pdf")
#seleciono a pagina
page = reader.pages[2]

#extraio todo texto do pdf para tratar ele separadamente
text = page.extract_text()
#extraio as questões (por enquanto, uma unica especifica)
pattern = re.compile(r"QUESTÃO 3([\s\S]*)QUESTÃO 4")
matches = pattern.findall(text).__str__()

#set array que vai armazenar as informações 
questao = {'Questao':[], 'A': [], 'B':[], 'C':[], 'D':[], 'E':[], 'Resposta':[]}

# get Questão e sanitize

pattern = re.compile(r"a.*\\nA ")
enunciado = pattern.findall(matches)[0]
enunciado = enunciado.replace("\\n","")
questao['Questao'].append(enunciado)
 
# get Alternativas

contagem = {
    '\\\\nA' : '\\\\nB',
    '\\\\nB' : '\\\\nC',
    '\\\\nC' : '\\\\nD',
    '\\\\nD' : '\\\\nE',
    '\\\\nE' : '.'
}

padrao = re.compile(r'(A|B|C|D|E)')
for i,v in contagem.items():
    patternA = re.compile(r"{} ([\s\S]*).{}".format(i,v))
    rA = patternA.findall(matches)[0]
    rA = rA.replace("\\n","")
    questao[f'{padrao.findall(i)[0]}'].append(rA)

clear()
print("\nQuestão:\n\n " + questao['Questao'][0])
print(" ")
print("A) " + questao['A'][0])
print("B) " + questao['B'][0])
print("C) " + questao['C'][0])
print("D) " + questao['D'][0])
print("E) " + questao['E'][0])