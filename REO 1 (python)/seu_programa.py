# UTF-8
from scipy \
    import stats
import sys

arg = sys.argv[1]

X = []
Y = []

arq = open(arg, 'r')
try:
    for valor in arq.readlines():
        xis, ypis = map(float, valor.split(","))
        X.append(xis)
        Y.append(ypis)

    calcula = stats.pearsonr(X, Y)
    print(calcula[0])

except Exception as Erro:
    print(Erro.__cause__)
    print(Erro.__class__)
    print(Erro)