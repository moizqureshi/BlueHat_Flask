function socketio(data) {
  //Parse the JSON object
  var parsed_data = JSON.parse(data);

  //Go through each peripheral within the JSON
  for( i = 0; i < parsed_json.peripherals.length; i++) {
    //check if the peripheral is new
    if(isPeriNew(parsed_json.peripherals[i].personName)) {
      //if it is, add a new canvas tag for it and save the name id of that.
      var canvas_name = canvasAdder(parsed_json.peripherals[i].personName);
      //then add the canvas JS and draw a point at x and y
      addPeri(parsed_json.peripherals[i].personName, canvas_name, parsed_json.peripherals[i].x_coord, parsed_json.peripherals[i].y_coord);
    }

    else //if the peripheral is not new then update it no matter what.
      updatePeri(parsed_json.peripherals[i].personName, parsed_json.peripherals[i].x_coord, parsed_json.peripherals[i].y_coord);
  } //updating no matter what saves us time by not iterating through a list to check who has moved or not and isntead just do a O(n) and update everyone.
}
