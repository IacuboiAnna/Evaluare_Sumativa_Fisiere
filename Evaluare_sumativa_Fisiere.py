with open('INPUT.txt', 'r') as f:
    input=f.read()
print('Nr', 'Numele', 'Prenumele', 'Nota1', 'Nota2', 'Nota3', sep='\t')
print(input)
with open('REZERVA.txt', 'w') as f:
    for linie_input in input:
        f.write(linie_input)
medie=0
for linie_output in input:
    i=linie_output.split()
    medie=str((float(i[3])+float(i[4])+float(i[5]))/3)
    output=i[0]+'  '+i[1]+'  '+i[2]+'  '+medie+'\n'
    with open('OUTPUT.txt', 'w') as f:
        f.write(output)
with open('OUTPUT.txt', 'r') as f:
    print('Nr', 'Numele', 'Prenumele', 'Media', sep='\t')
    print(f.read())