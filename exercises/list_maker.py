fr = open("list.txt")
fw = open("new.txt", "w")
for line in fr:
    fw.write(line)
