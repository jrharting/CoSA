import os, sys

input_cov = sys.argv[1] # input .cov file generated by bedtools genomecov -d

# 0-based positions with high entropy based on mbrown analysis
POSITIONS = [1237, 3215, 8978, 11283, 14608, 17947, 18058, 18260, 23616, 25777, 28358]

for line in open(input_cov):
    name, pos1, cov = line.strip().split()
    pos1, cov = int(pos1), int(cov)
    if pos1-1 in POSITIONS: print(pos1, cov)

