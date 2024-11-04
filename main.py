
import pandas as p

data=p.read_csv(r"C:\Users\linge\Desktop\python 100 days\projects\pr-26\nato_phonetic_alphabet.csv")
credic={r.letter:r.code for i,r in data.iterrows()}


#METHOD 1
t=True
while t:
    instr=input("Enter a Word: ").upper()
    try:
        
        codeword=[credic[l] for l in instr]
    except KeyError:
        print("Sorry only Letters in the alphabet please")
        # t=True      
    else:
        print(codeword)
        t=False
        

#METHOD 2
def genalpha():
    instr=input("Enter a Word: ").upper()
    try:
        
        codeword=[credic[l] for l in instr]
    except KeyError:
        print("Sorry only Letters in the alphabet please")
        genalpha()
    else:
        print(codeword)

genalpha()
