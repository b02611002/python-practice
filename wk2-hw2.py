AminoAcid={
	'UUC':'F', 
	
	'UUA':'L', 
	'UUG':'L',
	'CUU':'L',
	'CUC':'L',
	'CUA':'L',
	'CUG':'L',
	
	'AUU':'I',
	'AUC':'I',
	'AUA':'I',

	'AUG':'M',
	
	'GUU':'V',
	'GUC':'V',
	'GUA':'V',
	'GUG':'V',

	'UCU':'S',
	'UCC':'S',
	'UCA':'S',
	'UCG':'S',
	'AGU':'S',
	'AGC':'S',
	
	'CCU':'P',
	'CCC':'P',
	'CCA':'P',
	'CCG':'P',

	'ACT':'T',
	'ACC':'T',
	'ACA':'T',
	'ACG':'T',

	'GCU':'A',
	'GCC':'A',
	'GCA':'A',
	'GCG':'A',

	'UAU':'Y',
	'UAC':'Y',

	'CAU':'H',
	'CAC':'H',

	'CAA':'Q',
	'CAG':'Q',

	'AAU':'N',
	'AAC':'N',

	'AAA':'K',
	'AAG':'K',

	'GAU':'D',
	'GAC':'D',

	'GAA':'E',
	'GAG':'E',
	
	'UGU':'C',
	'UGC':'C',

	'UGG':'W',

	'CUG':'R',
	'CGC':'R',
	'CGA':'R',
	'CGG':'R',
	'AGA':'R',
	'AGG':'R',

	'GGU':'G',
	'GGC':'G',
	'GGA':'G',
	'GGG':'G',

	'UAA':'(Stop)',
	'UGA':'(Stop)',
	'UAG':'(Stop)'
}


def protein(s):

	if ((len(s)%3)!=0):
		return "Length should be multiple of 3."

	else:
		ans = ""
		for i in range(len(s)/3):
			# print(i*3, s[(i*3):(i*3+3)])
			ans += AminoAcid[s[(i*3):(i*3+3)]]

		return ans

print "Enter a string of RNA to translate into amino acid chains."
print "Example: Entering 'UGCGAUGAAUGGGCUCGCUCC' returns ", protein('UGCGAUGAAUGGGCUCGCUCC')
print(protein(input(":")))









