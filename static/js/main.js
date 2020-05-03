var count=0
function countNav() {
	count+=1;
	if(count%2===0)
		closeNav();
	else
		openNav();
	return count;
}

function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}

