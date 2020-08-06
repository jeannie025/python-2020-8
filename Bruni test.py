score = 0

print('Welcome to the Bruni test!')
sel = input('Start?: ')
if sel == 'yes'or'Yes':
    print('')
    print('1. Spring')
    print('2. Summer')
    print('3. Fall')
    print('4. Winter')
    q1 = input('Q.1: What is your favourite season? (spring/summer/fall/winter): ')
    
if q1 == ('spring'):
    score+=0
    print('score +',score)
elif q1 == ('summer'):
    score+=1
    print('score +',score)
elif q1 == ('fall'):
    score+=2
    print('score +',score)
elif q1 == ('winter'):
    score+=3
    print('score: ',score)

if q1 == 'spring'or'summer'or'fall'or'winter':
    
    print('')
    print('1. Elsa')
    print('2. Anna')
    print('3. Olaf')
    print('4. Bruni')
    print('5. None') 
    q2 = input('Q.2: Who is your favorite character in Frozen?')
if q2 == ('elsa'or'Elsa'):
    score+=0
    print('score +',score)
elif q2 == ('anna'or'Anna'):
    score+=1
    print('score +',score)
elif q2 == ('olaf'or'Olaf'):
    score+=2
    print('score +',score)
elif q2 == ('bruni'or'Bruni'):
    score+=3
elif q2 == ('none'or'None'):
    score+=0
    print('score: ',score)
    


if q3 == ('Daytime'or'daytime'or'Nighttime'or'nighttime'):
    q4 = input('Q.4: Do you prefer fire or ice?')
    
if q4 == ('fire'or'Fire'):
    print('score +',score)
    score+=2
elif q4 == ('ice'or'Ice'):
    print('score +',score)
    score+=3
    print('score: ',score)
    
    
print('Key:')
print('12 points: Bruni Bruni!')
print('8-11: Happy Bruni')
print('4-7: Sad Bruni')
print('0-3: Angry Bruni')

While True:
if score == 12:
    from tkinter import       
        root = Tk()      
        canvas = Canvas(root, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(file="bruni_bruni.jpg")      
        canvas.create_image(20,20, anchor=NW, image=img)      
        mainloop()
if score == 8 to 11:
    from tkinter import       
        root = Tk()      
        canvas = Canvas(root, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(file="happy_bruni.jpg")      
        canvas.create_image(20,20, anchor=NW, image=img)      
        mainloop()
if score == 4 to 7:
    from tkinter import       
        root = Tk()      
        canvas = Canvas(root, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(file="sad_bruni.jpg")      
        canvas.create_image(20,20, anchor=NW, image=img)      
        mainloop()
if score == 0 to 3:
    from tkinter import       
        root = Tk()      
        canvas = Canvas(root, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(file="angry_bruni.jpg")      
        canvas.create_image(20,20, anchor=NW, image=img)      
        mainloop()
