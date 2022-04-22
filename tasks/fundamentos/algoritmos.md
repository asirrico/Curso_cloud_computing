## 1 Calcular y mostrar el cuadrado de los números del 1 a 30.

Propuesta algoritmo 1 Bucle for con array

 ```
    Inicio programa

     Declaración de vector  -> v = [1,2,3,4...30]
     Creamos e inicializamos variable para almacenar resultado cuadrado -> x = 0
     Creamos e inicializamos la variable con la que trabajaremos en el bucle-> i = 0

        Inicio bucle -> for i in v

            Calcula cuadrado -> x=i²
            Mostramos variable x -> print x
            Incrementamos valor i -> i++

        La máquina internamente verifica si i <= 30, si es así repite el bucle, si no finaliza el bucle
        Fin bucle for



    Fin programa

 ```


 Propuesta algoritmo 2 Bucle while sin array



 ```
    Inicio programa

     Creamos e inicializamos variable para almacenar resultado cuadrado -> x = 0
     Creamos e inicializamos la variable con la que trabajaremos en el bucle-> i = 0

        Inicio bucle -> while i <= 30 do:

            Calcula cuadrado -> x=i²
            Mostramos variable x -> print x
            Incrementamos valor i -> i++

        La máquina internamente verifica si i <= 30, si es así repite el bucle
        Fin bucle -> End While
     


    Fin programa

 ```


## 2 Números primos

Calcular los números primos que hay del 0 al número introducido por teclado




 ```

        Algoritmo NumerosPrimos
            Escribir "Ingrese un número: "
            Leer nro
            div <- 2
            band <- Verdadero 	         
                    Si nro=1 Entonces 		            
                    Escribir "Es primo" 	         
                        Sino 		             
                            Mientras band=Verdadero y nro>div Hacer
                        Si nro MOD div = 0 Entonces
                            band <- Falso
                        FinSi
                            div <- div +1
                        FinMientras
                        si band= Verdadero Entonces
                        Escribir "Es primo"
                        Sino
                        Escribir "No es primo"
                        FinSi
                    FinSi
        FinAlgoritmo
``` 

## 3 Construir un avión de papel


##  4 Realizar las cuatro operaciones básicas (Suma, Resta, Multiplicación, División)

Propuesta algoritmo con selección de operación (Recursivo)



```
            Inicio Programa

                Definición e inincialización variable número 1 -> x = 0
                Definición e inincialización variable número 2 -> y = 0
                Definición e inincialización variable resultado -> z = 0
                Definición e inincialización variable entrada -> e = 0

                Definición de función suma -> suma(x,y){ z = x + y ; print z}
                Definición de función resta -> resta(x,y){ z = x - y ; print z}
                Definición de función multiplicación -> multiplicación(x,y){ z = x * y ; print z}
                Definición de función división -> división(x,y){ z = x / y ; print z}

                Inicio bucle while -> while i = 0 do:

                    Preguntar por teclado operación -> Print ¿Que operación realizo 0.Suma, 1.Resta, 2.Multiplicación o 3.División? Introducir número!!!
                    Esperar entrada por teclado-> e = input()

                    Preguntar por teclado número 1 -> Print ¿Que valor asignamos a numéro 1? Introducir número!!!
                    Esperar entrada por teclado-> x = input()

                    Preguntar por teclado número 2 -> Print ¿Que valor asignamos a numéro 2? Introducir número!!!
                    Esperar entrada por teclado-> y = input()


                    Inicio SI   Si la entrada por teclado es = 0 entonces llamar a función suma -> if (e = 0) then suma (x,y) 
                                Si la entrada por teclado no es 0 y es 1 llamar a función resta -> else if (e = 1) then resta (x,y)
                                Si la entrada por teclado no es 1 y es 2 llamar a función multiplicación -> else if (e = 2) then multiplicación (x,y)
                                Si la entrada por teclado no es 2 y es 3 llamar a función división -> else if (e = 3) then división (x,y)
                    FIn SI      Si la entrada por teclado no es ninguno de los valores que esperábamos imprimir error -> else print" Número introducido no corresponde con ninguna operación"
                       
                         Asignamos a variable de entrada "e" un valor por encima de 3 -> e = 4
                         Inicio bucle while e != 0 || e != 1
                                            Imprimir por pantalla pregunta de seguir o acabar programa -> Print"¿Desea seguir realizando operaciones? 1.Si 0.No"
                                            Recibir respuesta por teclado; e = input()
                                            Si la entrada por teclado es 1 entonces i = 0; if (e = 1) then i = 0
                                            Si la entrada por teclado no es 1 y es 0 finalizamos programa -> if else (e = 0) then i = 1
                                            Si la entrada por teclado no es un valor esperado imprimir error y se repetirá el bucle -> else print "Valor introducido no esperado"
                        Fin bucle while

                Fin bucle while
                



            Fin Programa



 ```     

    
    
Propuesta algoritmo 2 con ejecución secuencial sin bucles



```

         Inicio Programa

                Definición e inincialización variable número 1 -> x = 0
                Definición e inincialización variable número 2 -> y = 0
                Definición e inincialización variable resultado -> z = 0
                Definición e inincialización variable entrada -> e = 0

                    Preguntar por teclado número 1 -> Print ¿Que valor asignamos a numéro 1? Introducir número!!!
                    Esperar entrada por teclado-> x = input()

                    Preguntar por teclado número 2 -> Print ¿Que valor asignamos a numéro 2? Introducir número!!!
                    Esperar entrada por teclado-> y = input()
                    
                    Sumamos x más y, asignamos resultado a z -> z = x + y
                    Escribimos resultado -> print "Resultado suma = " z
                   
                    Restamos x menos y, asignamos resultado a z -> z = x - y
                    Escribimos resultado -> print "Resultado resta = " z
                   
                    Multiplicamos x por y, asignamos resultado a z -> z = x * y
                    Escribimos resultado -> print "Resultado multiplicación = " z
                   
                    Dividimos x entre y, asignamos resultado a z -> z = x / y
                    Escribimos resultado -> print "Resultado división = " z


            Fin Programa
```




## Volumen y Area de un Cilindro


## Pedir un libro en una biblioteca


## Encontrar el mayor número de tres números


Propuesta algoritmo 1 con ejecución secuencial sin bucles



```

         Inicio Programa

                Definición e inincialización variable número 1 -> x = 0
                Definición e inincialización variable número 2 -> y = 0
                Definición e inincialización variable numero 3 -> z = 0

                             
                Inicio SI
                    Si numero 1 es mayor o igual que número 2 y ademas es mayor o igual que numero 3 entonces  imprimir numero 1 es el mayor -> if x >= y && x >= z then print x " es el mayor"

                    Si no, si numero 2 es mayor que numero 1 y además es mayor que numero 3 entonces imprimir numero 2 es el mayor -> else if y > x && y > z then print y " es el mayor"

                    Si no, imprimir numero 3 es el mayor -> else print z " es el mayor"
                FIN SI

                


            Fin Programa
```




## Factorial de cualquier número


## Encontrar si un numero es mayor o menor a un número dado.

Propuesta algoritmo 1 con ejecución secuencial sin bucles



```

         Inicio Programa

                Definición e inincialización variable número 1 -> x = 6
                Definición e inincialización variable número 2 -> y = 8
           

                             
                Inicio SI
                    Si numero 1 es mayor o igual  número 2 imprimir número 1 mayor -> if x > y then print x " es mayor"
                    Si no, imprimir numero 2 es mayor -> if y > x then print y " es mayor"
                    
                FIN SI

                


            Fin Programa
```

## Adivinar una palabra.

