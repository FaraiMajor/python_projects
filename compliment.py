def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])


s = "GTCAG"
print(reverse_complement(s))


def similar(a):
    s = ["xyz", "foo", "of", 'aaa']
    print(similar(s))


similar()
