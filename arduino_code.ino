int trigPin=13; //Sensor Trig pin connected to Arduino pin 13
int echoPin=11;  //Sensor Echo pin connected to Arduino pin 11
float pingTime;  //time for ping to travel from sensor to target and return
float targetDistance; //Distance to Target in inches
float speedOfSound=776.5; //Speed of sound in miles per hour when temp is 77 degrees.
 
void setup() {
 
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
 
void loop() {
  
