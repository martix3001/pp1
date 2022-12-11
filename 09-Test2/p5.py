def f(first_letter,last_letter) :
    file = open('09-Test2\\test.txt','r',encoding="UTF-8")    
    sum = 0
    for line in file:     
        for word in line.split():       
            if (word[0] == first_letter) and (word[len(word)-1] == last_letter):
                sum += 1
            if (word[0] == first_letter) and ((word[len(word)-1] == ".")or(word[len(word)-1] == ",")):
                if(word[-2] == last_letter):
                    sum += 1    
    return sum  

print(f("w","d"))