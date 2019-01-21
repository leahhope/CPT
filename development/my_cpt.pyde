snake test;
food food1;
int highScore;

void setup(){
  size(500, 500);
  frameRate(10);
  test = new snake();
  food1 = new food();
  rectMode(CENTER);
  textAlign(CENTER, CENTER);
  
  highScore = 0;
}


void draw(){
  background(0);
  drawScoreboard();
  
  test.move();
  test.display();
  food1.display();
  
  
  if( dist(food1.xpos, food1.ypos, test.xpos.get(0), test.ypos.get(0)) < test.sidelen ){
    food1.reset();
    test.addLink();
  }
  
  if(test.len > highScore){
    highScore= test.len;
  }
}


void keyPressed(){
  if(key == CODED){
    if(keyCode == LEFT){
      test.dir = "left";
    }
    if(keyCode == RIGHT){
      test.dir = "right";
    }
    if(keyCode == UP){
      test.dir = "up";
    }
    if(keyCode == DOWN){
      test.dir = "down";
    }
  }
}


void drawScoreboard(){
  // All of the scode for code and title
  
  fill(255);
  textSize(20);
  text( "Snake Game", width/2, 80);
  fill(250, 0, 250);
  textSize(20);
  
  // draw scoreboard
  noStroke();
  fill( 0 );
  rect(90, 70, 160, 80);
  fill(255);
  textSize(17);
  text( "Score: " + test.len, 70, 50);
  
  fill(255);
  textSize(17);
  text( "High Score: " + highScore, 70, 70);
}

class food{
  
  // define varibles
  float xpos, ypos;
  
  
  
  //constructor
  food(){
    xpos = random(100, width - 100);
    ypos = random(100, height - 100);
  }
