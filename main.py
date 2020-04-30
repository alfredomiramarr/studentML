from student import student


def crea_estudiantes(count_estudiantes):
	count = 0
	list_students = []
	
	while count < int(count_estudiantes):

		student_code = input("dame la matricula: ")
		student_name = input("dame el nombre: ")
		student_age = input("dame la edad: ")
		student_gender = input("dame el genero (M-Mujer/H-Hombre): ")
		student_carreer = input("dame la carrera: ")
		
		list_students.append(student(student_code,student_name,student_age,student_gender,student_carreer))
		
		count = count + 1
	return list_students


def ordena_edades(list_students):
    c0 = 0
    list_orden = []
    list_orden = list_students
    list_orden.sort(key=lambda student: student.age, reverse=True)
    while c0 < len(list_orden):
        
        print(list_orden[c0].get_name() + " " + list_orden[c0].get_age())
        
        c0 = c0 + 1
    
    return 0
        
def separa_generos(list_students):
    c1 = 0
    cH = 0
    cM = 0
   
    list_H = []
    list_M = []
    while c1 < len(list_students):
       
        aux=list_students[c1].get_gender()
        if aux == "M":
            list_M[cM] = list_students[cM]
            cM = cM + 1
           
        if aux. == "H":
            list_H[cH] = list_students[cH]
            cH = cH + 1
           
        c1 = c1 + 1
   
    print("MUJERES: ")
    for i in list_M:
        print(list_M[i].get_name() + " " + list_M[i].get_gender())
       
    print("HOMBRES: ")
    for i in list_H:
        print(list_H[i].get_name() + " " + list_H[i].get_gender())
       
    return 0

def main():
    options = 1
    list_stud = []
    
    while options != "0":
        options = input("menu opciones 1. crea estudiantes - 2.ordena edades - 3.separa generos - 0. salir: ")
        if options == "1":
            print("crea estudiantes")
            count_x = input("cuantos estudiantes daremos de alta: ")
            list_stud = crea_estudiantes(count_x)
        
        if options == "2":
            print("ordena edades")
            li = list_stud
            ordena_edades(li)
            
            
        if options == "3":
            print("separa generos")
            li = list_stud
            separa_generos(li)

if __name__ == "__main__":
	main()
main()
=======
from student import student


def crea_estudiantes(count_estudiantes):
	count = 0
	list_students = []
	
	while count < int(count_estudiantes):

		student_code = input("dame la matricula: ")
		student_name = input("dame el nombre: ")
		student_age = input("dame la edad: ")
		student_gender = input("dame el genero (M-Mujer/H-Hombre): ")
		student_carreer = input("dame la carrera: ")
		
		list_students.append(student(student_code,student_name,student_age,student_gender,student_carreer))
		
		count = count + 1
	return list_students


def ordena_edades(list_students):
    c0 = 0
    list_orden = []
    list_orden = list_students
    list_orden.sort(key=lambda student: student.age, reverse=True)
    while c0 < len(list_orden):
        
        print(list_orden[c0].get_name() + " " + list_orden[c0].get_age())
        
        c0 = c0 + 1
    
    return 0
        
def separa_generos(list_students):
    c1 = 0
    cH = 0
    cM = 0
    
    list_H = []
    list_M = []
    while c1 < len(list_students):
        
        if list_students.gender == "M":
            list_M[cM] = list_students[cM]
            cM = cM + 1
            
        if list_students.gender == "H":
            list_H[cH] = list_students[cH]
            cH = cH + 1
            
        c1 = c1 + 1
    
    print("MUJERES: ")
    for i in list_M:
        print(list_M[i].get_name() + " " + list_M[i].get_gender())
        
    print("HOMBRES: ")
    for i in list_H:
        print(list_H[i].get_name() + " " + list_H[i].get_gender())
        
    return 0

def main():
    options = 1
    list_stud = []
    
    while options != "0":
        options = input("menu opciones 1. crea estudiantes - 2.ordena edades - 3.separa generos - 0. salir: ")
        if options == "1":
            print("crea estudiantes")
            count_x = input("cuantos estudiantes daremos de alta: ")
            list_stud = crea_estudiantes(count_x)
        
        if options == "2":
            print("ordena edades")
            li = list_stud
            ordena_edades(li)
            
            
        if options == "3":
            print("separa generos")
            li = list_stud
            separa_generos(li)

if __name__ == "__main__":
	main()
main()
>>>>>>> 183bf8522da3a4578f332623bd785a2a6ba6e0c8
=======
from student import student


def crea_estudiantes(count_estudiantes):
	count = 0
	list_students = []
	
	while count < int(count_estudiantes):

		student_code = input("dame la matricula: ")
		student_name = input("dame el nombre: ")
		student_age = input("dame la edad: ")
		student_gender = input("dame el genero (M-Mujer/H-Hombre): ")
		student_carreer = input("dame la carrera: ")
		
		list_students.append(student(student_code,student_name,student_age,student_gender,student_carreer))
		
		count = count + 1
	return list_students


def ordena_edades(list_students):
    c0 = 0
    list_orden = []
    list_orden = list_students
    list_orden.sort(key=lambda student: student.age, reverse=True)
    while c0 < len(list_orden):
        
        print(list_orden[c0].get_name() + " " + list_orden[c0].get_age())
        
        c0 = c0 + 1
    
    return 0
        
  def separa_generos(list_students):
    c1 = 0
    cH = 0
    cM = 0
   
    list_H = []
    list_M = []
    while c1 < len(list_students):
       
        aux=list_students[c1].get_gender()
        if aux == "M":
            list_M[cM] = list_students[cM]
            cM = cM + 1
           
        if aux. == "H":
            list_H[cH] = list_students[cH]
            cH = cH + 1
           
        c1 = c1 + 1
   
    print("MUJERES: ")
    for i in list_M:
        print(list_M[i].get_name() + " " + list_M[i].get_gender())
       
    print("HOMBRES: ")
    for i in list_H:
        print(list_H[i].get_name() + " " + list_H[i].get_gender())
       
    return 0

def main():
    options = 1
    list_stud = []
    
    while options != "0":
        options = input("menu opciones 1. crea estudiantes - 2.ordena edades - 3.separa generos - 0. salir: ")
        if options == "1":
            print("crea estudiantes")
            count_x = input("cuantos estudiantes daremos de alta: ")
            list_stud = crea_estudiantes(count_x)
        
        if options == "2":
            print("ordena edades")
            li = list_stud
            ordena_edades(li)
            
            
        if options == "3":
            print("separa generos")
            li = list_stud
            separa_generos(li)

if __name__ == "__main__":
	main()
main()
>>>>>>> 15d2766b37173a5fe24e404b7d3fcab2299e5115
