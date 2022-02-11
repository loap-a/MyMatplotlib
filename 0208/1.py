import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,50)
print('here',type(x))
y1=x**2
y2=x**2+1

plt.figure()
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
l1=plt.plot(x,y1,label='up')
l2=plt.plot(x,y2,color='red',linewidth=1.0,linestyle=':',label='down')
plt.legend(handles=[l1[0],l2[0]],labels=['aaa','bbb'],loc='best')


plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I m x')
plt.ylabel('I m y')

new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)

plt.yticks([-2,0,1],['$aa aa$',r'$bbbb \ \alpha$','c'])

ax=plt.gca()
ax.spines['right'].set_color('none')


ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',-1))
ax.spines['left'].set_position(('data',-1))



plt.show()