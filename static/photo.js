function readURL(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
          $('#blah').attr('src', e.target.result);
      };

      reader.readAsDataURL(input.files[0]);
      var inphoto = input.files[0];
      var x = document.getElementById("photodiv");
      x.style.display = "block";
      
      var fileReader = new FileReader();
      
      fileReader.onload = function(inphoto) {
      var srcData = input.files[0].target.result;
      var xhttp = new XMLHttpRequest();
      xhttp.open("POST", "http://127.0.0.1:5000/uploader/", true);
      xhttp.setRequestHeader("Content-type", "application/json");
      xhttp.send({image:srcData});
      // var xhr = new XMLHttpRequest();
//       xhr.open("POST", "http://127.0.0.1:5000/uploader/"+scrData, true);
//       xhr.setRequestHeader("Content-Type", "application/json");
//       xhr.send(JSON.stringify({image: srcData}));
      };
      
      // $.ajax({
//          url: 'http://127.0.0.1:5000/upload', 
//          type: 'POST',
//          data: '{"foo":"bar"}',
//          success: function(data){
//             alert(data);
//             //process the JSON data etc
//          },
//          error: function(){
//             alert("Cannot get data");
//          }
//       });
      
      
      
      console.log("Request complete!");
   }
}
    