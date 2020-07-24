function opennavprod() {
	document.getElementById("mySidenavprod").style.width = "300px";
}
function closenavprod() {
	document.getElementById("mySidenavprod").style.width = "0";
}

function opensearch() {
	document.getElementById("sidephone").style.width = "250px";
}
function closesearch() {
	document.getElementById("sidephone").style.width = "0";
}

function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}
// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}



function myFunctionphone() {
  document.getElementById("myDropdownphone").classList.toggle("show");
}
// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtnphone')) {
    var dropdowns = document.getElementsByClassName("dropdown-content-phone");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}