from lexer import Lexer

a = '''/*fasfasfas
dasdasda
dasdasdasd*/   
	int a = 0;
//hola mep
int b=a+3;
  /*



  */  // tres
  /* es */// dos
    long s =         2;
    double esta_es_una_variable;
    bool bandera=false;
    int aab = 0223;
    int bcc = 0x32ad34;
    float daa = 0.9887;
    double asd = 7.889;
    long zzz = 43242;'''
#Con archivo
with open('Test','r') as f:
  lex = Lexer(f.read())
  lex.scan()
  for i in lex.tokens:
    print(i)

#Con variable
'''lex = Lexer(a)
lex.scan()
for i in lex.tokens:
   print(i)'''