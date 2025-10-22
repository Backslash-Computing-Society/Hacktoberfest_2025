pat=input("Enter pattern (stars/numbers/chars/pyramid/diamond/triangle/hollow): ").strip().lower()
n=int(input("Enter size: "))
if pat=='stars':
  [print('*'*i) for i in range(1,n+1)]
elif pat=='numbers':
  [print(''.join(str(x) for x in range(1,i+1))) for i in range(1,n+1)]
elif pat=='chars':
  [print(''.join(chr(64+x) for x in range(1,i+1))) for i in range(1,n+1)]
elif pat=='pyramid':
  [print(' '*(n-i)+'*'*(2*i-1)) for i in range(1,n+1)]
elif pat=='diamond':
  [print(' '*(n-i)+'*'*(2*i-1)) for i in list(range(1,n+1))+list(range(n-1,0,-1))]
elif pat=='triangle':
  [print('*'*i) for i in range(n,0,-1)]
elif pat=='hollow':
  [print('*'*i if i in (1,n) else '*'+ ' '*(i-2)+'*') for i in range(1,n+1)]
else: print('Invalid pattern')
