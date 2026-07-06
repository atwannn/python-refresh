name=input('enter your name:')
with open ('students.txt',mode='r') as file:
    file_content=file.read()
if name in file_content :

    print('already in programm')


else :
    with open ('students.txt', mode='a') as file:
        file.write('\n'+name)