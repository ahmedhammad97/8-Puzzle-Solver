$('#btn').on('click', function(){
  grid = $('#in').val()
  if(validateGrid(grid)){
    $('#curtains').fadeIn(400,function(){
      $('#sec1').fadeOut("slow", function(){$('#sec2').fadeIn("slow", function(){
        $('#code').text(grid)
        sendToServer(grid, $('#sel').val())
      })})
    })
  }else{
    alert("Wrong format .. Please fix the input")
  }
})

function validateGrid(grid){
  grid = grid.split(',').sort()
  for(i=0;i<9;i++){
    if(+(grid[i]) != i){return false}
  }
  return true
}

function sendToServer(grid, type){
      $.ajax({
        method: "POST",
        url: "/solve",
        data: { grid : grid, type : type}
      })
        .done(function( msg ) {
            $('#curtains').fadeOut()
            if(msg=="Failed :("){
              alert("Something Wrong Happened!");
            }
            else{
              renderGrid(linearToSquare(grid.split(",")))
              console.log(grid.split(","));
              doTheJob(grid.split(","), msg.split(" "));
            }
        });
}


function linearToSquare(array){
  grid = [[0,1,2],[3,4,5],[6,7,8]]

  for(i=0; i<3; i++){
    for(j=0; j<3; j++){
      grid[i][j] = array[(i*3)+j]
      if(grid[i][j]=='0'){zeroPos = [i,j]}
    }
  }

  return grid
}

function doTheJob(code, actions){
  grid = linearToSquare(code)
  zeroPos = [1,2]

  for(i=0; i<3; i++){
    for(j=0; j<3; j++){
      if(grid[i][j]=='0'){zeroPos = [i,j]}
    }
  }

  $('tbody tr').eq(zeroPos[0]).find('td').eq(zeroPos[1]).css('background-color', 'lightyellow')

  var loops = 0
  var iterations = setInterval(function(){
    if(loops==actions.length){
      clearInterval(iterations);
      $('#again').fadeIn('slow')
    }
    else{
      console.log("Loop " + loops)
      setTimeout(function(){},300)
      action = actions[loops]
      if(action == "Up"){
        grid[zeroPos[0]][zeroPos[1]] = grid[zeroPos[0] - 1][zeroPos[1]]
        grid[zeroPos[0] - 1][zeroPos[1]] = 0
        zeroPos = [zeroPos[0] - 1, zeroPos[1]]
      }
      else if(action == "Left"){
        grid[zeroPos[0]][zeroPos[1]] = grid[zeroPos[0]][zeroPos[1] - 1]
        grid[zeroPos[0]][zeroPos[1] - 1] = 0
        zeroPos = [zeroPos[0], zeroPos[1] - 1]
      }
      else if(action == "Right"){
        grid[zeroPos[0]][zeroPos[1]] = grid[zeroPos[0]][zeroPos[1] + 1]
        grid[zeroPos[0]][zeroPos[1] + 1] = 0
        zeroPos = [zeroPos[0], zeroPos[1] + 1]
      }
      else if(action == "Down"){
        grid[zeroPos[0]][zeroPos[1]] = grid[zeroPos[0] + 1][zeroPos[1]]
        grid[zeroPos[0] + 1][zeroPos[1]] = 0
        zeroPos = [zeroPos[0] + 1, zeroPos[1]]
      }

      renderGrid(grid)
      loops++
      $('td').css('background-color', 'lightblue')
      $('tbody tr').eq(zeroPos[0]).find('td').eq(zeroPos[1]).css('background-color', 'lightyellow')
    }
  },1000)

}


function renderGrid(grid){
  let table = $('#table')[0]
  // rows
  for(var i = 0; i < table.rows.length; i++)
  {
    // cells
    for(var j = 0; j < table.rows[i].cells.length; j++)
    {
        table.rows[i].cells[j].innerHTML = grid[i][j]
    }
  }
}

$('#again').on('click', function(){
  location.reload();
})
