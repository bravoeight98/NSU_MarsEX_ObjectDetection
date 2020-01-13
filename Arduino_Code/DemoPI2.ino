String inString = "";    // string to hold input


//Motor2
const int Left2_M1 = 2;
const int Left2_M2 = 3;

//Motor3
const int Right1_M1 = 4;
const int Right1_M2 = 5;


void setup() {

  // Open serial communications and wait for port to open:

  Serial.begin(9600);


  pinMode(Left2_M1, OUTPUT);
  pinMode(Left2_M2, OUTPUT);

  pinMode(Right1_M1, OUTPUT);
  pinMode(Right1_M2, OUTPUT);

}




void loop() {

  // Read serial input:


  digitalWrite(Left2_M1, HIGH);
  digitalWrite(Left2_M2, HIGH);

  digitalWrite(Right1_M1, HIGH);
  digitalWrite(Right1_M2, HIGH);

  while (Serial.available() > 0) {
    String s1 = Serial.readStringUntil('\n');


    int locationofCom = s1.indexOf(',');

    String x_coord, y_coord;

    x_coord = s1.substring(0, locationofCom);
    y_coord = s1.substring(locationofCom+1);
    int x = x_coord.toInt();
    int y = y_coord.toInt();
    Serial.print("x: ");
    Serial.print(x_coord);
    Serial.print(" || ");
    Serial.print(x);
    Serial.print(" || ");
    Serial.print(" y: ");
    Serial.print(y);

    if (x > 80 && x < 320)
    {
      digitalWrite(Left2_M1, LOW);
      digitalWrite(Left2_M2, HIGH);

      digitalWrite(Right1_M1, HIGH);
      digitalWrite(Right1_M2, LOW);

      Serial.println("Object Right");
    }

    if (x < -80 && x > - 320)
    {


      digitalWrite(Left2_M1, HIGH);
      digitalWrite(Left2_M2, LOW);

      digitalWrite(Right1_M1, LOW);
      digitalWrite(Right1_M2, HIGH);



      Serial.println("Object Left");
    }

    else if (y > 0 && y < 160 && x<=80 && x>=-80)
    {

      digitalWrite(Left2_M1, HIGH);
      digitalWrite(Left2_M2, LOW);

      digitalWrite(Right1_M1, HIGH);
      digitalWrite(Right1_M2, LOW);

      Serial.println("Object UP");
    }

    else if (y < 0 && y > -160 && x<=80 && x>=-80)
    {
      digitalWrite(Left2_M1, LOW);
      digitalWrite(Left2_M2, HIGH);

      digitalWrite(Right1_M1, LOW);
      digitalWrite(Right1_M2, HIGH);




      Serial.println("Object Down");
    }

    else if (x == 0 && y == 0)
    {
      digitalWrite(Left2_M1, HIGH);
      digitalWrite(Left2_M2, HIGH);

      digitalWrite(Right1_M1, HIGH);
      digitalWrite(Right1_M2, HIGH);

      Serial.println("Object Center");

    }

  }
}













