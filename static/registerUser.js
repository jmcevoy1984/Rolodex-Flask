function registerUser(){
    var error = null;
    var errorBox = document.getElementById('error-box');
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPass = document.getElementById('confirm-pass').value;
    console.log('button works!');
    console.log(email);
    console.log(password);
    console.log(confirmPass);
    if ((email !== '' && password !== '') && confirmPass !== ''){
        if (password === confirmPass){
            console.log('test')
            xhr = new XMLHttpRequest();
            xhr.open('POST', '/api/users');
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify({ 'email': email, 'password': password }));
            xhr.onload = function(){
                resp = JSON.parse(xhr.responseText);
                console.log(resp);
                if (resp.result === true){
                    console.log('true!');
                    window.location = '/login?result=True';
                }
            }

        }
        else{
            error = 'Passwords do not match.';
        }
    
    }
    else{
        error = 'Required fields missing.';
    }
    
    if (error !== null){
        errorBox.innerHTML = error;
        errorBox.style.visibility = "visible";
    }
}//end function