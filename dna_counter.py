dna= input("Enter DNA sequence:")
dna= dna.strip().upper()
print("DNA counter")
print("----------")
print("cleaned dna sequence:")
print(dna)
print("-----------")
print("Sequence Length:")
print(len(dna))
count=0
for nucleotide in dna:
  if nucleotide== "A":
    count=count+1
print("A count:")
print(count) 
count=0 
for nucleotide in dna:
  if nucleotide== "C":
    count=count+1 
print("C count:")     
print(count)
c_count= count
count=0
for nucleotide in dna:
  if nucleotide== "G":
    count=count+1
print("G count:")     
print(count)
g_count=count
count=0  
for nucleotide in dna:
  if nucleotide== "T":
    count=count+1
print("T count:")   
print(count)   
gc_content=((g_count+c_count)/len(dna))*100
print(gc_content)
rna=dna.replace("T","U")
print("RNA sequence:")
print(rna)
