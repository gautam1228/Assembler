if "\t" in line[0]:
    splited_list=line[0].split("\t")
    line[0]=splited_list[0]
    line.insert(splited_list[1],1)
