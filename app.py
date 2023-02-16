from PyPDF2 import PdfReader
import re

#seleciono o arquivo
reader = PdfReader("reva.pdf")
#seleciono a pagina
page = reader.pages[2]

#extraio todo texto do pdf para tratar ele separadamente
text = page.extract_text()
#extraio as questões (por enquanto, uma unica especifica)
pattern = re.compile(r"QUESTÃO 1([\s\S]*)QUESTÃO 2")
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

print(questao)