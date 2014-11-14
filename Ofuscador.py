tokens  = ('ID','NUM','LET', 'ALFNUM', 'ASG', 'IF', 'ELSE', 'SWITCH', 'CASE', 'WHILE', 'DEFAULT')
ids     = []
dic     = {}
t_NUM   = r'[0-9]+'
t_LET   = r'[A-Za-z]+'
t_ALFNUM= r'[A-Za-z0-9]+'
t_ASG   = r'='
#t_ID    = r'[a-z][a-zA-Z0-9]*'
t_IF    = r'if'

literals = ['+', '-', '*', '=', '<', '>', '=', '!', ':', ';', '(', ')', '{', '}', '&', '|']

def t_ID(t):
    r'[a-z][a-zA-Z0-9]*'
    return t

def ofuscarVar(id):
    new_id = id
    new_id +='X'
    return new_id

#t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Expresion mal definida '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex
lex.lex()

#parser
def p_var(p):
    'variable : ID ASG ID'
    if(p[1] in dic):
        n=ids[dic[p[1]]]
    else:
        ids.append(ofuscarVar(p[1]))
        dic[p[1]]=len(ids)-1
        n=ids[len(ids)-1]
    print (n)
    return n

def p_PLS(p):                       #PROGRAMA -> lista_sentencias
    'P : LS'
    p[0] = p[1]

def p_LSLSS(p):                     #lista_sentencias -> lista_sentencias sentencia
    'LS : LS S'
    p[0] = p[1]+p[2]

def p_LSS(p):                       #lista_sentencias -> sentencia
    'LS : S'
    p[0] = p[1]

def p_SE(p):                        #sentencia -> E;
    'S : E ;'
    p[0] = p[1]+p[2]

def p_SW(p):                        #sentencia -> WHILE
    'S : W'
    p[0] = p[1]

def p_SIFE(p):                      #sentencia -> IF_ELSE
    'S : IE'
    p[0] = p[1]

def p_SSWC(p):                      #sentencia -> SWITCH
    'S : SW'
    p[0] = p[1]

def p_WWS(p):                       #WHILE -> while (condicion) sentencia ;
    'W : while ( C ) S ;'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]

def p_WWLS(p):                      #WHILE -> while (condicion) { lista_sentencias }
    'W : while ( C ) { LS }'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]

def p_IEIES(p):                     #IF_ELSE -> IF else sentencia;
    'IE : I else S ;'
    p[0] = p[1]+p[2]+p[3]

def p_IEIELS(p):                     #IF_ELSE -> IF else { lista_sentencias }
    'IE : I else { LS }'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]

def p_IICS(p):                       #IF -> IF (condicion) sentencia
    'I : IF ( C ) S'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]

def p_ICLS(p):                      #IF-> IF (condicion) {lista_sentencias}
    'I : IF ( C ) { LS }'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]

def p_SWSWILC(p):                    #SWITCH -> SWITCH(ID) {lista_case}
    'SW : switch ( ID ) { LC }'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]

def p_SWSWILCD(p):                    #SWITCH -> SWITCH(ID) {lista_case DEFAULT}
    'SW : switch ( ID ) { LC } DF'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]

def p_LCC(p):                          #lista_case -> CASE
    'LC : CA'
    p[0] = p[1]

def p_LCLCC(p):                          #lista_case -> lista_case CASE
    'LC : LC CA'
    p[0] = p[1]+p[2]

def p_CACAIDSE(p):                      #CASE -> CASE ID : sentencia
    'CA : case ID : S'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]+p[6]

def p_CACAIDLS(P):                      #CASE -> CASE ID : { lista_sentencias }
    'CA : case ID : { LS }'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]

def p_DFDFS(p):                         #DEFAULT -> DEFAULT : sentencia
    'DF : default : S'
    p[0] = p[1]+p[2]+p[3]

def p_DFDFLS(p):                         #DEFAULT -> DEFAULT : { lista_sentencias }
    'DF : default : { LS }'
    p[0] = p[1]+p[2]+p[3]+p[4]+p[5]+p[6]

def p_CCL(p):                           #CONDICION -> CONDICION_LOGICA
    'C : CL'
    p[0] = p[1]

def p_CCA(p):                           #CONDICION -> AND
    'C : AND'
    p[0] = p[1]

def p_CCO(p):                           #CONDICION -> OR
    'C : OR'
    p[0] = p[1]

def p_AND(p):                           #AND -> CONDICION_LOGICA && CONDICION_LOGICA
    'AND : CL && CL'
    p[0] = p[1]+p[2]+p[3]

def p_OR(p):                           #OR -> CONDICION_LOGICA || CONDICION_LOGICA
    'OR : CL || CL'
    p[0] = p[1]+p[2]+p[3]

def p_CL0(p):                            #CONDICION_LOGICA -> E > E
    'CL : E > E'
    p[0] = p[1]+p[2]+p[3]

def p_CL1(p):                            #CONDICION_LOGICA -> E < E
    'CL : E < E'
    p[0] = p[1]+p[2]+p[3]

def p_CL2(p):                            #CONDICION_LOGICA -> E >= E
    'CL : E > = E'
    p[0] = p[1]+p[2]+p[3]+p[4]

def p_CL3(p):                            #CONDICION_LOGICA -> E <= E
    'CL : E < = E'
    p[0] = p[1]+p[2]+p[3]+p[4]

def p_CL4(p):                            #CONDICION_LOGICA -> E == E
    'CL : E == E'
    p[0] = p[1]+p[2]+p[3]+p[4]

def p_CL5(p):                            #CONDICION_LOGICA -> E != E
    'CL : E != E'
    p[0] = p[1]+p[2]+p[3]+p[4]

def p_EET(p):                           #E -> E+T
    'E : E + T'
    p[0] = p[1]+p[2]+p[3]

def p_EET2(p):                           #E -> E-T
    'E : E - T'
    p[0] = p[1]+p[2]+p[3]

def p_ET(p):                               #E -> T
    'E : T'
    p[0] = p[1]

def p_TTID(p):                               #T-> T*ID
    'T : T * ID'
    p[0] = p[1]+p[2]+p[3]

def p_TTID1(p):                               #T-> T/ID
    'T : T/ID'
    p[0] = p[1]+p[2]+p[3]

def p_TID(p):                                #T -> ID
    'T : ID'
    p[0] = p[1]

def p_error(p):
    if p:
        print("Error de sintaxis en '%s'" % p.value)
    else:
        print(">.>")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = input('Inserte expresion > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)