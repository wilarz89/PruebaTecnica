from collections import OrderedDict


def mostCommon(string):

    if len(string) < 3 or len(string) <= 10000:
        sortedlist = sorted(string)
                # detect change , need a number
        sortedlist.append('1')

        #verify ocurrences
        count = 0
        current = sortedlist[0]
        dictionary = OrderedDict()

        for s in sortedlist:
            if current != s:
                dictionary[current] = count
                count = 1
                current = s
            else:
                count += 1
        maximum = max(dictionary, key=dictionary.get)
        common = OrderedDict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        res = []
        for s, n in common.items():
            res.append(s + ' ' + str(n))
            if len(res) == 3:
                break
        return res
s = input()

for data in mostCommon(s):
    print(data)
