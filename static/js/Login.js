function CheckCredentials(e){
    console.log("working");
    // to cancel the event if the user misses an entry box
    e.preventDefault();

    //gets the username and password
    var userInput1 = document.getElementById("username").value;
    var userInput2 = document.getElementById("password").value;

    if(!userInput1 || !userInput2){
        alert("both fields are required!");
    }


}


/* thought process
basically in the program you need to check the credentials first and foremost and that's the first button thing we need to do and reduce repeated code
then we need to send the credentials over without an issue so we would need to send this info to main which then would reroute to argon2
then aes encryption then save boom, but first we need it to go back to main so the routeing is the first thing we need to handle
when this works we just need to rinse and repeat and make the ui look nice

i saw an example of fetch being used in someone code and i want to try to implement it myself into my own code.
 */