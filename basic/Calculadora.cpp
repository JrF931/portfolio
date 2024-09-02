#include <stdio.h>
#include <math.h>
#include <stdlib.h>

float suma(float a, float b) {
    return a + b;
}

float resta(float a, float b) {
    return a - b;
}

float multiplicacion(float a, float b) {
    return a * b;
}

float division(float a, float b) {
    if (b == 0) {
        printf("Error: No se puede dividir por cero\n");
        return 0; 
    }
    return a / b;
}

float potencia(float a, float b) {
    return pow(a, b);
}

int main() {
    int operacion;
    float n1, n2;
    

    printf("Seleccione la operacion que desea ingresar:\n");
    printf("1. Sumar\n");
    printf("2. Restar\n");
    printf("3. Multiplicar\n");
    printf("4. Dividir\n");
    printf("5. Potencia\n");
    

    printf("Introduzca la operacion matematica que desea realizar: ");
    scanf("%d", &operacion);
    

    printf("Introduzca el valor del primer numero: ");
    scanf("%f", &n1);
    printf("Introduzca el valor del segundo numero: ");
    scanf("%f", &n2);
    
 
    switch (operacion) {
        case 1:
            printf("Resultado: %.2f\n", suma(n1, n2));
            break;
        case 2:
            printf("Resultado: %.2f\n", resta(n1, n2));
            break;
        case 3:
            printf("Resultado: %.2f\n", multiplicacion(n1, n2));
            break;
        case 4:
            printf("Resultado: %.2f\n", division(n1, n2));
            break;
        case 5:
            printf("Resultado: %.2f\n", potencia(n1, n2));
            break;
        default:
            printf("Opcion erronea\n");
            break;
    }
    
    system("pause");
    exit(0);
    
    return 0;
    
}

