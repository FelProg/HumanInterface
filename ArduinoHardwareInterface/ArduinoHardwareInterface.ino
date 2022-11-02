//Interfaz humano maquina programa V1.0
/*El programa recibe la interrupcion de las letras
  a,b,c,d Para activar los leds
  A,B,C,D Para desactivar los leds
  e,E     Para activar o desactivar en conjunto
*/
//Germán Félix

const int Led1 = 5;
const int Led2 = 4;
const int Led3 = 3;
const int Led4 = 2;
int opcion = 0;

int leds[] = {Led4,Led3,Led2,Led1};

void setup()
{
  Serial.begin(9600);
  for(int i=0; i < 4; i++)
    pinMode(leds[i],OUTPUT);
}

void loop()
{
  opcion = Serial.read();
  
  if(opcion!=-1){
  	Serial.println(opcion);
    switch(opcion){
      //Prendido minusculas
      case 97: digitalWrite(Led1,HIGH);
        break;
      case 98: digitalWrite(Led2,HIGH);
        break;
      case 99: digitalWrite(Led3,HIGH);
        break;
      case 100: digitalWrite(Led4,HIGH);
        break;
      case 101: 
        set(HIGH);
        break;
      //Apagado mayusculas
      case 65: digitalWrite(Led1,LOW);
        break;
      case 66: digitalWrite(Led2,LOW);
        break;
      case 67: digitalWrite(Led3,LOW);
        break;
      case 68: digitalWrite(Led4,LOW);
        break;
      case 69: 
        set(LOW);
        break;
      default:
        break;
    } 
  }
}

//funcion que recibe HIGH o LOW para prender o apagar
//todos los leds.
void set(uint8_t status){
  for(int i=0; i < 4; i++)
    digitalWrite(leds[i],status);          
}
