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

"""NO FUNCIONA BIEN PORQUE NO IMPRIME LAS LISTAS SEPARADAS"""        
def separa_generos(list_students):
    c1 = 0
    cH = 0
    cM = 0
    i = 0
    j = 0
    list_H = []
    list_M = []
    while c1 < len(list_students):
       
        aux = list_students[c1].get_gender()
        
        """print(aux)"""
        if aux == "genero: M":
            list_M.append(list_students[c1])
            """print (list_M[cM].get_name())"""
            cM = cM + 1
            """print (cM)"""
           
        if aux == "genero: H":
            list_H.append(list_students[c1])
            """print(list_H[cM].get_name())"""
            cH = cH + 1
            """print(cH)"""
           
        c1 = c1 + 1
        
    """print (len(list_H))"""
    """print (len(list_M))"""
   
    print("MUJERES: ")
    while i < len(list_M):
        print(list_M[i].get_name() + " " + list_M[i].get_gender())
        i = i + 1
          
    print("HOMBRES: ")
    while j < len(list_H):
        print(list_H[j].get_name() + " " + list_H[j].get_gender())
        j = j + 1
       
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

