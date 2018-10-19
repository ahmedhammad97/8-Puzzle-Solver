$('#btn').on('click', function(){
  grid = $('#in').val()
  if(validateGrid(grid)){
    sendToServer(grid, $('#sel').val())
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
            console.log(msg)
        });
}
