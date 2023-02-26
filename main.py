# Format input:
# neterminali separati prin spatiu
# terminali separati prin spatiu
# simbol start
# productii - pe cate o linie - prin spatii

def generare( cuv, n ):
    if len( cuv ) > n:
        mari = [ x for x in cuv if x.upper() == x ]
        for lit in mari:
            if '#' in productii[lit]:
                generare( cuv.replace( lit, '' ), n )
        return
    if len( cuv ) == n and cuv.lower() == cuv:
        if cuv not in generate:
            print( cuv if cuv != "" else "#" )
        generate.append( cuv )
        return
    for lit in cuv:
        if lit == lit.upper():
            for var in productii[lit]:
                generare( cuv.replace( lit, var if var != '#' else '' ), n )

with open("input.txt", "r") as f:
    v = [ x.split() for x in f.readlines() ]
N = v[0]
T = v[1]
start = v[2][0]
aux = v[3::]
productii = {}
generate = []
for productie in aux:
    productii.update( { productie[0]: productie[1::] } )
n = int( input( 'n = ' ) )
generare( start, n )