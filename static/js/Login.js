function CheckCredentials(e){
    console.log("working");
    // to cancel the event if the user misses an entry box
    e.preventDefault();

    //gets the username and password
    var userInput1 = document.getElementById("username").value;
    var userInput2 = document.getElementById("password").value;

    // error handling if the user only enters one entry box
    //this is to prevent future errors as we know that both entries have data inside
    if(!userInput1 || !userInput2){
        alert("both fields are required!");
    }

    //calls the Flask route (aka the url endpoint)
    fetch("/credentials/validate", {
        //tells fetch to send a post request
        method: "POST",
        //sets a content type so Flask knows to parse JSON
        headers: {
            "Content-Type": "credentials/json"
        },
        // converts the JS objects into strings before sending
        body: JSON.stringify(userInput1, userInput2)
    })
        //waits for the server response and convert it to JSON
        .then(response => response.json())
        //catch and log any network or server errors
        .catch(error => {
        console.error("ERROR:",error)
    })


}


/* thought process
basically in the program you need to check the credentials first and foremost and that's the first button thing we need to do and reduce repeated code
then we need to send the credentials over without an issue so we would need to send this info to main which then would reroute to argon2
then aes encryption then save boom, but first we need it to go back to main so the routeing is the first thing we need to handle
when this works we just need to rinse and repeat and make the ui look nice

i saw an example of fetch being used in someone code and i want to try to implement it myself into my own code.
 */