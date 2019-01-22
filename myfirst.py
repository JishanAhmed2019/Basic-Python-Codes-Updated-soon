"""This is my first Python code
It Computes the gc contents of a DNA Sequence
"""
#Read DNA sequence from User
#dna='acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag'
dna=input("Enter a DNA sequence:")
print(dna)
#Count the numbrer of C's in DNA sequence
count_c=dna.count('c')
#Count the numbrer of G's in DNA sequence
count_g=dna.count('g')
print(count_c,count_g)
#Determine the length of DNA sequence
dna_length=len(dna)
#Compute the percentage of gc
gc_percent=(count_c+count_g)*100.0/dna_length
print("The GC percet is %5.3f %%"% gc_percent)

#Use of if statement
if 'c' in dna:
    nabases=dna.count('c')
    print("DNA sequence has %d undefined bases" % nabases)
