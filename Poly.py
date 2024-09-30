class School:
    def __init__(self,Name,SchoolID):
        self.Name = Name
        self.SchoolID = SchoolID
    
    def AdressIdentity(self):
        print("School_Adress: 515/Amabani house Marg  ,Bandra Road,  Mustang Colony, Mumbai")

class Principal(School):

    def AdressIdentity(self):
      print("This is principal Class")
       
class Feculty(School):
    def AdressIdentity(self):
      print("This is Feculty Class")
       
class Student(School):
    def AdressIdentity(self):
      print("This is Student Class")
          
Principal1= Principal("Mukesh Ambani", "P_43234")
Feculty1 = Feculty("Ajay Malhotra", "F_34355")
Student1 = Student("Naina Sinde", "S_43254")

for x in (Principal1,Feculty1,Student1): 
    print(x.Name)
    print(x.SchoolID)
    x.AdressIdentity()
