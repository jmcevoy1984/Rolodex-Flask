function signIn(){
    var email = document.getElementById('email').value;
    var email = document.getElementById('email').value;
    var verify = false;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/users');
    xhr.send();
    xhr.onload = function(){
        var resp = JSON.parse(xhr.responseText);
        var users = resp.Users;
        for(var i = 0; i < users.length; i++){
            if(users[i].email === email){
                if(users[i].password === password){
                    verify = true;
                }
                else{
                    break;
                }
            }
        }
        console.log('Verified: ' + verify);
    }
}