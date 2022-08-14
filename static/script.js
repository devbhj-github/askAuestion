
function myfunction(){
    let idd = document.getElementById("idd").value;
    let myname = document.getElementById("name").value;
    let age = document.getElementById("age").value;
    let question  = document.getElementById("question").value;
    let extranotes = document.getElementById("extranotes").value;

    // Step4:- Create the HTML file that will capture input and process the data to Json  -->> Main part of this program is loading the HTML file , entering the data onto the page and then processing it with JavaScript and AJAX.

       // pass the javascript variables to a dictionary
    const dict_values = {
        "idd" : idd ,
        "name": myname,
        "age" : age,
        "question" : question,
        "extranotes" : extranotes
     };  
  

     // Stringify converts a javascript objector value to a JSON format
    const s = JSON.stringify(dict_values);

    window.alert(s)
    console.log("s",s );

    $.ajax({
        url:"/test",
        type:"POST",
        contentType:"application/json",
        data:JSON.stringify(s)
    });
}



