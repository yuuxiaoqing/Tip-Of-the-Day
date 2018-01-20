var x = document.getElementById("photodiv");
   x.style.display = "none";
function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#blah')
                    .attr('src', e.target.result)
            };

            reader.readAsDataURL(input.files[0]);
            var x = document.getElementById("photodiv");
            x.style.display = "block";
        }
    }
    
var $form = $('#contactForm'),
    $summands = $('.num1'),
    $sumDisplay = $('#itmttl');

$('.num1').on("input",function(){
    var sum = 0;
    $.each($summands, function(){
        var n = $(this).val();
        sum = isNaN(n) || n == '' ? sum : sum+parseFloat(n); 
    });
    $('#sum').val(sum);
});