//Custom Canvas Object to hold all we need and make it easy
function Canvas(tag) {
  this.drawable = tag.getContext("2d"); //holds the canvas
  this.name = "Default Name";
  this.setName = setName;
  this.init = init;
  this.addMarkerXY = addMarkerXY;
  this.addMarkerInner = addMarkerInner;
  this.clearMarkerXY = clearMarkerXY;
  this.clearMarker = clearMarker;
  this.drawMap = drawMap;
  this.addMarkerList = addMarkerList;
  this.addMarkerCoor = addMarkerCoor
  this.setColor = setColor;
  this.drawTriangle = drawTriangle;
  this.color = "#000000"; //holds the color to draw with
  this.x = 0; //holds the last X coordinate
  this.y = 0; //holds the last Y coordinate
}

function setName(name) {
  this.name = name;
}

/*
 * Takes in a list of coordinates like [[x1,y1], [x2,y2]]
 * and draw a polygon by iterating through the coordinates
 * drawing points and lines between the points
 */
function drawMap(map) {
  this.drawable.strokeStyle = '#000000';
  for( i = 0; i < map.length; i++) {
    var x = map[i][0];
    var y = map[i][1];

    if( i > 0)
      this.drawable.lineTo(x, y)

    //this.addMarkerXY(x, y);
    this.drawable.moveTo(x, y);
  }
  this.drawable.lineTo(map[0][0], map[0][1]);
  this.drawable.lineWidth = 2;
  this.drawable.stroke();
}

//atm this is unused.
function init(tag) {
  this.drawable = tag.getContext("2d");
}

/*
 * Adds a marker at position (x,y) and saves x and y
 * internally a.k.a in this.x and this.y
 */
function addMarkerXY(x, y) {
  console.log("x = " + x + " y = " + y + " color = " + this.color);
  this.x = x;
  this.y = y;

  this.drawable.strokeStyle = this.color;

  this.drawable.fillStyle = this.color;
  this.drawable.font = "12px Arial";
  this.drawable.fillText(this.name,x-20,y-10);

  this.drawable.beginPath();
  this.drawable.arc(x, y, 4, 0, 2*Math.PI);
  this.drawable.fill();
  this.drawable.stroke();
  //this.drawable.strokeRect(x,y,2,2);
}

/*
 * Adds a marker at position (this.x, this.y)
 */
function addMarkerInner( ) {
  this.addMarkerXY(this.x, this.y);
}

function drawTriangle(x, y, wi, he) {
  this.drawable.fillStyle = this.color;
  this.drawable.beginPath();
  this.drawable.rect(x, y, wi, he);
  this.drawable.fill();
}
/*
 * Adds a lot of markers from a list of coordinates
 * this is different from drawMap because it doesn't draw
 * any lines.
 */
function addMarkerList(coordinateList, NameList) {
  for( i = 0; i < coordinateList.length; i++) {
    this.name = NameList[i];
    this.addMarkerXY(coordinateList[i][0], coordinateList[i][1]);
  }
}

/*
 * This functions received a single list of 2 entries
 * and makes a marker off of the 0th and 1st where [0] is x
 * and [1] is y
 */
function addMarkerCoor(coordinates) {
  this.addMarkerXY(coordinates[0], coordinates[1]);
}

/*
 * removes a marker at position x, y
 */
function clearMarkerXY(x, y) {
  //causes no error if x or y is 0
  //THIS MUST BE C HANGED LATER
  this.drawable.clearRect(0,0,640,640);
}

/*
 * remove the marker at position (this.x, this.y)
 */
function clearMarker() {
  this.clearMarkerXY(this.x, this.y);
}

/*
 * sets the color to draw with
 */
function setColor(color) {
  this.color = color;
}
