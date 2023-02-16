from PyPDF2 import PdfReader

reader = PdfReader("reva.pdf")
page = reader.pages[2]

import re

text = page.extract_text()

pattern = re.compile(r"QUESTÃO 3([\s\S]*)QUESTÃO 4")
matches = pattern.findall(text).__str__()

questao = {'Questao':[], 'A': [], 'B':[], 'C':[], 'D':[], 'E':[], 'Resposta':[]}

# Questão
pattern = re.compile(r"a.*\\nA ")
enunciado = pattern.findall(matches)[0]

questao['Questao'].append(enunciado)
 
# Alternativas

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
    rA = patternA.findall(matches)[0];
    questao[f'{padrao.findall(i)[0]}'].append(rA)

print(questao)