let login = prompt(question = "Whos there?", "");

if(login == "Admin") {
    let password = prompt("Password?", "");

    if(password == "TheMaster") {
        alert("Welcome!");
    }
    else if (password == '' || password == null){
        alert('Canceled');
    }
    else {
        alert('Wrong password!');
    }
}
else if (login == null || login == ''){
    alert('Canceled');
} 
else {
    alert('I dont know you');
}