#hometask
a = [8,9,0,5,4,3,2,7,6,1,7]
k = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']
b = []
for _ in a:
  b.append(k[_])
print(*b)