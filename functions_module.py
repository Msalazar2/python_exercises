def is_vowel(s):
    
    v = ['a','e', 'i', 'o', 'u', 'y']
    
    return s in v


def calculate_tip(p, b):
    
    return p * b


def get_letter_grade(grade): 
        
        if int(grade >= 88 and grade <= 100):
        
            grade = 'A'
    
        elif int(grade >= 80 and grade <= 87):
        
            grade = 'B'
    
        elif int(grade >= 67 and grade <= 79):
        
            grade = 'C'
    
        elif int(grade >= 60 and grade <= 66):
        
            grade = 'D'
    
        else:
        
            grade = 'F'
            
        return grade