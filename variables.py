texto = "Juan Ruiz"
num = 88
decimal = 1.70
pregunta = True
resultado = int

print('hola !',texto , 'tu numero de estudiantes es: ' + str(num),'tu estatura es: ' + str(decimal), '¿Eres de colombia? ' + str(pregunta) , sep= "\n")

# Limites de los enteros y los flotnates en python

""" 
LIMITES DE ENTEROS:

CHAR_BIT	Número de bits de la variable menor que no es un campo de bits.	8
SCHAR_MIN	Valor mínimo de una variable de tipo signed char.	-128
SCHAR_MAX	Valor máximo de una variable de tipo signed char.	127
UCHAR_MAX	Valor máximo de una variable de tipo unsigned char.	255 (0xff)
CHAR_MIN	Valor mínimo de una variable de tipo char.	-128; 0 si se usa la opción /J
CHAR_MAX	Valor máximo de una variable de tipo char.	127; 255 si se usa la opción /J
MB_LEN_MAX	Número máximo de bytes de una constante de varios caracteres.	5
SHRT_MIN	Valor mínimo de una variable de tipo short.	-32768
SHRT_MAX	Valor máximo de una variable de tipo short.	32767
USHRT_MAX	Valor máximo de una variable de tipo unsigned short.	65535 (0xffff)
INT_MIN   	Valor mínimo de una variable de tipo int.	-2147483648
INT_MAX 	Valor máximo de una variable de tipo int.	2147483647
UINT_MAX	Valor máximo de una variable de tipo unsigned int.	4294967295 (0xffffffff)
LONG_MIN	Valor mínimo de una variable de tipo long.	-2147483648
LONG_MAX	Valor máximo de una variable de tipo long.	2147483647
ULONG_MAX	Valor máximo de una variable de tipo unsigned long.	4294967295 (0xffffffff)
LLONG_MIN	Valor mínimo de una variable de tipo long long	-9223372036854775808
LLONG_MAX	Valor máximo de una variable de tipo long long	9223372036854775807
ULLONG_MAX	Valor máximo de una variable de tipo unsigned long long	18446744073709551615 (0xffffffffffffffff)

LIMITES DE FLOTANTES:

FLT_DIG - DBL_DIG - LDBL_DIG   Número de dígitos, q, tal que un número de punto flotante con q dígitos decimales se puede redondear en una representación de punto flotante y restablecer sin pérdida de precisión.
FLT_EPSILON-DBL_EPSILON-LDBL_EPSILON   Número positivo menor x, tal que x + 1,0 no es igual a 1,0
FLT_GUARD   0 
FLT_MANT_DIG - DBL_MANT_DIG - LDBL_MANT_DIG    Número de dígitos en la base especificada por FLT_RADIX en el significado de punto flotante. La base es 2; por consiguiente, estos valores especifican los bits.
FLT_MAX - DBL_MAX - LDBL_MAX	Número de punto flotante máximo que se puede representar.	3.402823466e+38F
FLT_MAX_10_EXP - DBL_MAX_10_EXP - LDBL_MAX_10_EXP	Entero máximo tal que 10 elevado a dicho número es un número de punto flotante que se puede representar.	38
FLT_MAX_EXP - DBL_MAX_EXP - LDBL_MAX_EXP	Entero máximo tal que FLT_RADIX elevado a dicho número es un número de punto flotante que se puede representar.	128
FLT_MIN - DBL_MIN - LDBL_MIN	Valor positivo mínimo.	1.175494351e-38F
FLT_MIN_10_EXP - DBL_MIN_10_EXP - LDBL_MIN_10_EXP	Entero negativo mínimo tal que 10 elevado a dicho número es un número de punto flotante que se puede representar.	-37
FLT_MIN_EXP - DBL_MIN_EXP - LDBL_MIN_EXP	Entero negativo mínimo tal que FLT_RADIX elevado a dicho número es un número de punto flotante que se puede representar.	-125
FLT_NORMALIZE		0
FLT_RADIX - _DBL_RADIX - _LDBL_RADIX	Base de representación de exponente.	2
FLT_ROUNDS - _DBL_ROUNDS - _LDBL_ROUNDS	   Modo de redondeo para la adición de punto flotante.	

"""

n1 = int(input ("ingresa tu primer numero a sumar: "))
n2 = int(input ("ingresa tu segundo numero a sumar: "))

print (n1+n2)