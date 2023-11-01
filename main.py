import collections

with open('./books/frankenstein.txt') as f:
  contents = f.read()
  dict = {}
  for c in contents:
    if c.lower() in dict:
      dict[c.lower()] += 1
    else:
      dict[c.lower()] = 0

  # print (dict)
  sDict = collections.OrderedDict(sorted(dict.items()))
  for key, value in sDict.items():
    if key.isalpha():
      print(f'The {key} character was found {value} times')
