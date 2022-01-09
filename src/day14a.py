input = '''BN -> C
OS -> K
BK -> C
KO -> V
HF -> K
PS -> B
OK -> C
OC -> B
FH -> K
NV -> F
HO -> H
KK -> H
CV -> P
SC -> C
FK -> N
VV -> F
FN -> F
KP -> O
SB -> O
KF -> B
CH -> K
VF -> K
BH -> H
KV -> F
CO -> N
PK -> N
NH -> P
NN -> C
PP -> H
SH -> N
VO -> O
NC -> F
BC -> B
HC -> H
FS -> C
PN -> F
CK -> K
CN -> V
HS -> S
CB -> N
OF -> B
OV -> K
SK -> S
HP -> C
SN -> P
SP -> B
BP -> C
VP -> C
BS -> K
FV -> F
PH -> P
FF -> P
VK -> F
BV -> S
VB -> S
BF -> O
BB -> H
OB -> B
VS -> P
KB -> P
SF -> N
PF -> S
HH -> P
KN -> K
PC -> B
NB -> O
VC -> P
PV -> H
KH -> O
OP -> O
NF -> K
HN -> P
FC -> H
PO -> B
OH -> C
ON -> N
VN -> B
VH -> F
FO -> B
FP -> B
BO -> H
CC -> P
CS -> K
NO -> V
CF -> N
PB -> H
KS -> P
HK -> S
HB -> K
HV -> O
SV -> H
CP -> S
NP -> N
FB -> B
KC -> V
NS -> P
OO -> V
SO -> O
NK -> K
SS -> H'''
template = 'KOKHCCHNKKFHBKVVHNPN'
current = template
mapping = dict([line.split(' -> ') for line in input.splitlines()])

for step in range(1, 11):
    result = current[0]
    for idx, char in enumerate(current[:-1]):
        next_char = current[idx + 1]
        mapped = mapping.get(char + next_char)

        if mapped:
            result = result + mapped + next_char
        else:
            print(f'?: {char}:{next_char}')
            result = result + next_char

    current = result
    print(f'After step {step}, length: {len(current)}: {current}')

occurrences = dict([(char, current.count(char)) for char in current])
high = max(occurrences, key=occurrences.get)
low = min(occurrences, key=occurrences.get)

print(f'Final result: {high} ({occurrences.get(high)}) - {low} ({occurrences.get(low)}) = {occurrences.get(high) - occurrences.get(low)}')
