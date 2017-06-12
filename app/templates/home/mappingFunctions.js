//Holds a dictionary of: (peripheral person name, the peripheral's own Custom Canvas object)
var peripherals = new Map();

/*
 * Checks if we have a peripheral Canvas object associated with a peripheral name
 * passed in. Send true/false accordingly
 */
function isPeriNew(periName) {
  //Checks in the map with the key
  if (peripherals.get(periName) === undefined){
    return true;
  }
  return false;
}

/*
 * Makes a new Canvas object, draw a mark at (x, y)
 * in the Canvas and then add this new object to the map
 * and associate it with the peripheral name
 */
function addPeri(periName, periCanvasId, x, y) {
  var periCanvas = new Canvas(document.getElementById(periCanvasId));
  periCanvas.setName(periName);
  periCanvas.addMarkerXY(x, y);
  peripherals.set(periName, periCanvas);
}

/*
 * This simply gets a Canvas object from the dictionary
 * with the peripheral person name as the key then
 * remove the existing marker and create a new one
 * at (x, y)
 */
function updatePeri(periName, x, y) {
  var periCanvas = peripherals.get(periName);
  periCanvas.clearMarker();
  periCanvas.addMarkerXY(x, y);
}
