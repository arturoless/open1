print('Ingrese:')
cadena=input()
cadena=cadena.split(' ')

terminales=['void','int','float','a','{','}','(',')','return','instrucciones']
no_terminales=['S','TipoDato','Identificador','Letra','RestoLetra','Retorno','$']
tabla = {"S":{"void":["void","Identificador","(",")","{","instrucciones","}"],
            "int":["TipoDato","Identificador","(",")","{","instrucciones","Retorno","}"],
            "float":["TipoDato","Identificador","(",")","{","instrucciones","Retorno","}"]},
        "TipoDato":{"int":["int"],"float":["float"]},
        "Identificador":{"a":["Letra","RestoLetra"]},
        "Letra":{"a":["a"]},
        "RestoLetra":{"a":["Letra","RestoLetra"],"(":[]},
        "Retorno":{"return":["return"]}        
        }


reglas=['S','$']
while reglas[0]!='$': 
    regla=reglas[0]
    lexema=cadena[0]
    if regla in terminales:
        if lexema == regla:
            reglas.pop(0)
            cadena.pop(0)
        else:
            print('ERROR')
            break
    else:
        
        try:
            resultado_consulta=tabla[regla][lexema]
        except:
            resultado_consulta=None
        if resultado_consulta != None:
            reglas.pop(0)
            if len(resultado_consulta)>0:
                for rule in reversed(resultado_consulta):
                    reglas.insert(0,rule)
        else: 
            print('ERROR')
            break
    print(reglas)