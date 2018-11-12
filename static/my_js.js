// Validating Empty Field
function check_empty() {
if (document.getElementById('item').value == "" || document.getElementById('description').value == "" ||
    document.getElementById('cost').value == "" || document.getElementById('image').value == "") {
alert("Fill All Fields !");
} else {
document.getElementById('form').submit();

}
}

//Function To Display Popup
function div_show() {
document.getElementById('abc').style.display = "block";
}
//Function to Hide Popup
function div_hide(){
document.getElementById('abc').style.display = "none";
}
$(document).ready(function() {
    div_show();
});