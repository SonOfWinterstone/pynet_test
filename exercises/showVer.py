
f = open("../../pynet-ons-jun17/day1/show_version.txt")

lines = f.read().splitlines()

for line in lines:
  if "Processor board ID" in line:
    lst = line.split("Processor board ID ")

print(lst[1])
