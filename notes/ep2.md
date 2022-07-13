# Python for beginners from zero
# ep.2

# Variable/str/int/float - 002600/003550
	- variable - 004900
	- .format - 005200
	- f-string - 005800
	- [Scratch](www.scratch.mit.edu) - 010000
# [Google Colab](www.colab.research.google.com) - 003855
# Anaconda introduction - 004600
# Operator [+ - * / ** // %] - 011040
# Loop [for/while] - 013720
```
for i in range(10):
	print(i)
```
```
i = 10
while i > 0 :
	print(i)
	i -= 1 # i = i -1
```
# Function - 021240
```
def Hello():
	print('Hello, World')

def Hello10():
	for i in range(10):
		print('Hello, World')

def Hello(name):
	print(f'Hello, {name}')

def Hello(name='World'):
	print(f'Hello, {name}')
```
# turtle - 022222
```
import turtle
tao = turtle.Pen()
tao.shape('turtle')
def Rectangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)
		
def Go(x=100, y=100):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()

```