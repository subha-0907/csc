n=[1,2,3,4,5,6,7,9,8]
for i in range(len(n)-1):
      for j in range (i+1):
          if n[j] > n[j+1]:
              n[j],n[j+1] = n[j+1],n[j]
print(n)
