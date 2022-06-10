from ast import While
from pydoc import doc


text = "<html><body>Hello</body><h1>I am happy</h1></html>"
m=""
def getText(ind):
    ind+=1
    m=""
    while(ind < len(text)):
        if text[ind] == '<': break
        m = ''.join((m,text[ind]))
        #m = m + text[ind]
        ind += 1
    print(m)

#i = text.find('>')
#getText(i)

for i in range( len(text) ):
    #print(text[i])
    if text[i] == '>':
        getText(i)


#while i == -1:
    #m = m.join(i)
    #print(text[i])
    #i= i+1


 
#while(i < len(text)):
    #print(text[i], end = " ")
    #i += 1


