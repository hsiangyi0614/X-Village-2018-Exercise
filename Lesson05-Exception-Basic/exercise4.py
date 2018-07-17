# RelationException
class relationship(Exception):
    def __init__(self, p1,p2):
        self.name = p1
        self.name2= p2
    def __str__(self):
        return "Are you sure that " + self.name + " and " + self.name2 +" are each other"

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    if pa not in relation:
        print("Not found")
        raise relationship(pa,pb)
    elif relation[pa] != pb:
        # TODO: raise exception
        # TIPS: 這個地方會需要 raise 兩種 exception
        raise relationship(pa,pb)
    
        

#main
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except relationship as e:
    print(e)