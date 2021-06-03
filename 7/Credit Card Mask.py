def maskify(cc):
    cc_listed = list(cc)
    for i in range(0,len(cc_listed)-4):
        cc_listed[i] = "#"
    
    return "".join(cc_listed)

print(maskify("Bam"))