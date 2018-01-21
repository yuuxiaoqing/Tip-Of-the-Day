var subtotal = parseInt('{{subtotal}}');
console.log(subtotal)
var tax = parseInt('{{tax}}');
var taxpercent = parseInt('{{tax_percent}}');
var tip = 0;


function tipcalc() 
{ 
    var fn, ln, result; 
    fn = parseInt(subtotal, 10);
    ln = parseInt(document.getElementById("tip").value, 10);
    result =  (fn*(ln/100)+tax); 
    document.getElementById("tipresult").innerHTML = result; 
}


   