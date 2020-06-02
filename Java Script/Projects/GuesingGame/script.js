
var randomint = Math.floor(Math.random() * 21);
alert(randomint)
var lives = ( 5)
document.getElementById("life").innerHTML = ("You have "+ lives + " lives")
function checkguess(){
var hello = document.getElementById('hello').value
if (hello == randomint){
    alert("You Won!!!")
    
}
else if(hello === NaN ){
    alert("please type a number")

}
else if (hello<20 && hello!==randomint){
    lives-=1
    document.getElementById("life").innerHTML = "you have "+ lives + " lives"+ " left";
    alert("wrong, You have ", lives , "lives left")
}
else if(lives<0){
    location.reload(true)
}
else{
    alert("please type a smaller value")
    
}
}
