from PyPDF2 import PdfReader

reader = PdfReader("reva.pdf")
page = reader.pages[2]

import re

text = page.extract_text()

pattern = re.compile(r"QUESTÃO 3([\s\S]*)QUESTÃO 4")
matches = pattern.findall(text).__str__()
 
contagem = {
    '\\\\nA' : '\\\\nB',
    '\\\\nB' : '\\\\nC',
    '\\\\nC' : '\\\\nD',
    '\\\\nD' : '\\\\nE',
    '\\\\nE' : '.'
}

for i,v in contagem.items():
    patternA = re.compile(r"{} ([\s\S]*).{}".format(i,v))
    rA = patternA.findall(matches)
    print(rA)
