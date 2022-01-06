import rf

page = rf.page_get.find_all("a")
title = rf.table_get.find_all("a")
pval = []
tval = []

for a in page[0:-2]:
    pval.append(a.string)

print("Pages is ", 1, "~", pval[-2])

for b in title:
    tval.append(b.string)

print("##Security Title##")
for read in tval:
    print("-" + " " + read)
