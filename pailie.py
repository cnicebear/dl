sum = []
def getPermutation(n):
        path = []
        a = []
        for i in range(n):
            a.append(i + 1)
        back(a,path)
def back(a, path):
      for j in range(len(a)):
          if a[j] not in path:
               path.append(a[j])
               if len(path) == len(a):
                   sum.append(1)
               back(a, path)
               path.remove(path[-1])
if __name__ == '__main__':
    getPermutation(5)
    print(len(sum))