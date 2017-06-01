# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
global mode
mode = "normal"


def SetDir(Key, Dir):
    if (Dir == 0):
        Key += 1
    else:
        Key -= 1
        
    return Key


def key_switch():
    global mode
    row1 = ['1','2','3','4','5','6','7','8','9','0']
    row2 = ['q','w','e','r','t','y','u','i','o','p']
    row3 = ['a','s','d','f','g','h','j','k','l']
    row4 = ['z','x','c','v','b','n','m']
    
    row5 = ['!','@','#','$','%','^','&','*','(',')']
    row6 = ['Q','W','E','R','T','Y','U','I','O','P']
    row7 = ['A','S','D','F','G','H','J','K','L']
    row8 = ['Z','X','C','V','B','N','M']
        
    if (mode == "normal"):
        return [row1,row2,row3,row4]
        mode = "special"
    else:
        return [row5,row6,row7,row8]
        mode = "normal"
    
    
def MainLoop():
    key_list = key_switch()    
    pass_length = 16
    
    row_start = random.randrange(10)
    row_dir   = random.randrange(2)
    row_amount = random.randrange(6) + 2
    row_ind = row_start
    
    col_start = random.randrange(3)
    col_dir   = random.randrange(2)
    col_amount = random.randrange(2) + 2
    col_ind = col_start
    print(col_amount)
    
    phrase = ''
    col_iter  = 0
    key_count = 0
    while (key_count <= pass_length):
        row_iter  = 0
        row_ind = row_start
    
        '''while we dont have X number of row keys
        keep appending 'til we do'''
        while (row_iter < row_amount):
    
            '''try finding next row key but if we 
            get index out of range, reset row index'''
            try:
                phrase += key_list[col_ind][row_ind]
                key_count += 1
                row_ind = SetDir(row_ind, row_dir)
                if (row_ind == -1):
                    row_ind = row_start                    
            except:
                row_ind = row_start
    
            ''''we have added a row key so row
            iteration and row index + 1'''
            row_iter += 1
    
        '''now we have a full row of keys so
        switch columns'''
        col_ind = SetDir(col_ind, col_dir)
        col_iter += 1
        
        '''if column iteration reached the limit
        reset it and the index'''
        if (col_iter >= col_amount):
            col_ind = col_start
            col_iter = 0
            
        '''we have no 5th column so when it
        gets to that point loop around'''
        if (col_ind == 4):
            col_ind = 0
                      
        key_list = key_switch()    
    sys.stdout.write('{}\n'.format(phrase))

if (__name__ == "__main__"):
    import random, sys
    MainLoop()
