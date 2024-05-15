def read_heading():
        
    sub_heading = []
    
    with open('Inner_Heading.txt','r') as file:
        for line in file:
            sub_heading.append(line.strip())
            
        return sub_heading
            
