char serial;
#define KITCHEN 9
#define LOBBY 6
#define MASTER 10
#define GUEST 3
#define HALL 11
void setup(){    
  Serial.begin(9600);
  pinMode(KITCHEN,1);
  pinMode(LOBBY,1);
  pinMode(MASTER,1);
  pinMode(GUEST,1);
  pinMode(HALL,1);}
void loop(){
  if(Serial.available()>0){
      serial=Serial.read();
      Serial.println(serial);
      if(serial=='b'){
        lights(200);}
      else if(serial=='d'){
        lights(5);}}}
void lights(int intensity){
  analogWrite(KITCHEN,intensity);
  analogWrite(LOBBY,intensity);
  analogWrite(GUEST,intensity);
  analogWrite(HALL,intensity);
  analogWrite(MASTER,intensity);}
