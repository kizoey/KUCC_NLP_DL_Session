#!/usr/bin/env python
# coding: utf-8

# ## [KUCC] NLP를 활용한 딥러닝
# ### Week 01. 파이썬 기초

# ### **1. 산술연산**

# In[ ]:


1 - 2


# In[ ]:


4 * 5


# In[ ]:


7 / 5


# In[ ]:


3 ** 2


# ### **2. 자료형**

# In[ ]:


type(10)


# In[ ]:


type(2.718)


# In[ ]:


type("hello")


# ### **3. 변수**

# In[ ]:


x = 10
print(x)


# In[ ]:


x = 100
print(x)


# In[ ]:


y = 3.14
x * y


# In[ ]:


type(x * y)


# ### **4. 리스트**

# In[ ]:


a = [1, 2, 3, 4, 5]
print(a)


# In[ ]:


len(a) #리스트 길이


# In[ ]:


a[0]


# In[ ]:


a[4]


# In[ ]:


a[4] = 99
print(a)


# In[ ]:


#1번 자리 ~ (3-1)번 자리의 숫자까지 표시
a[1:3]


# In[ ]:


a[1:]


# In[ ]:


a[:3]


# In[ ]:


a[:-1] #전체에서 하나 빼기


# In[ ]:


a[:-2] #전체에서 두개 빼기


# ### **5. 딕셔너리**

# In[ ]:


me = {'height':180} #딕셔너리 : 키 값
me['height']


# In[ ]:


me['weight'] = 70 #weight값 추가
print(me)


# ### 6. **Bool(True/False)**

# In[ ]:


hungry = True
sleepy = False
type(hungry)


# In[ ]:


not hungry


# In[ ]:


#True and False = False
hungry and sleepy


# In[ ]:


#True or False = True
hungry or sleepy


# ### 7. **if문**

# In[ ]:


hungry = True
if hungry:
  print("I'm hungry")


# In[ ]:


hungry = False
if hungry:
  print("I'm hungry")
else:
  print("I'm not hungry")

#elif: if ~ else 사이에 넣기


# ### 8. **For문**

# In[ ]:


for i in [1, 2, 3]:
  print(i)


# ### 9. **함수**

# In[ ]:


def hello():
  print("Hello World!")

hello()


# In[4]:


def hello(object):
  print("Hello" + " " + object + "!")

hello("cat")


# ### 10. **클래스**

# In[ ]:


class Man:
  def __init__(self, name):
    self.name = name #클래스에 이름 부여
    print("Initialized!")

  def hello(self):
    print("Hello " + self.name + "!")

  def goodbye(self):
    print("Good-bye " + self.name + "!")

m = Man("David") #클래스 생성
m.hello()
m.goodbye()


# ### **11. Numpy**

# In[ ]:


import numpy as np
#행렬: 2차원, 텐서: 2+차원의 데이터 다루기 위한 라이브러리


# In[ ]:


x = np.array([1.0, 2.0, 3.0])
print(x)
type(x)


# ### 12. **N차원 배열**

# In[ ]:


A = np.array([[1, 2], [3, 4]])
print(A)


# In[ ]:


print(A.shape) #행x열


# In[ ]:


print(A.dtype)


# ### **13. 산술 연산**

# In[ ]:


x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y) #원소별(elementwise) +
print(x - y) #원소별 -
print(x * y) #원소별 *
print(x / y) #원소별 /

#numpy 행렬의 배열이 똑같아야함
#np.matmul (행렬곱): 앞 행렬의 열, 뒤 행렬의 행이 같아야함


# In[ ]:


x = np.array([1.0, 2.0, 3.0])
x / 2.0


# ### **14. 원소 접근**

# In[ ]:


X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)


# In[ ]:


X[0] #1행


# In[ ]:


X[0][1] #1행,2열


# In[ ]:


for row in X:
  print(row)


# ### **15. 평탄화**.flatten()
# : numpy 배열에서 1차원적 배열 형태로 변환

# In[ ]:


X = X.flatten()
print(X)
X[np.array([0, 2, 4])]

