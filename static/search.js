function search(searchValue){
    var loadGif = document.getElementById('loading-gif');
    //loadGif.innerHTML = ajaxImg;
    var resultsArray = [];
    var usersArray = [];
    var req = new XMLHttpRequest();
    req.open('GET', '/api/staff');
    req.send();
    req.onload = function(){
    var resp = JSON.parse(req.responseText);
    resp = resp.Members;
    for(var i = 0; i < resp.length; i++){
        var keyArray = Object.keys(resp[i]);
        for(var j = 0; j < keyArray.length; j++){
            if(typeof(resp[i][keyArray[j]]) === 'string'){
                if (resp[i][keyArray[j]].toLowerCase().includes(searchValue.toLowerCase())){
                    resultsArray.push(resp[i]);
                    break;
                }
            
            }
        }
        
    }
        console.log(resultsArray.length);
        var request = new XMLHttpRequest();
        request.open('GET', '/api/users');
        request.send();
        request.onload = function(){
            var response = JSON.parse(request.responseText);
            response = response.Users;
            for (var i = 0; i < response.length; i++){
                for (j = 0; j < resultsArray.length; j++){
                    if (response[i].id === resultsArray[j].id){
                        usersArray.push(response[i]);
                        break;
                    }
                    
                }
            }
            if (resultsArray.length > 0){
            console.log(resultsArray);
            showResults(resultsArray, usersArray);
            }
            else{
                document.getElementById('main').innerHTML = "<div class='alert alert-danger'>No results found!</div>";

            }
        }
    }
    
}//End 'search' function.

function showResults(results, users){
    resultsHtml = 
        "<table class='table table-striped'>" + 
            "<tr>" +
            "<th>Image</th>" +
            "<th>Name</th>" +
            "<th>Role</th>" +
            "<th>Team</th>" +
            "<th>Email</th>" +
            "<th>Ext</th>" +
            "<th>Mobile</th>" +
            "</tr>";
    for(var i = 0; i < results.length; i++){
        resultsHtml +=
            "<tr class='hover' onclick='location.href ="+'"/member/'+users[i].id+'"'+"'"+";>" +
                "<td><img src=" + users[i].profile_thumb_uri + ">" +
                "<td>"+ "<a href='/member/" + results[i].id + "'>" + results[i].first_name + ' ' + results[i].last_name +"</a></td>" +
                "<td>"+ results[i].role +"</td>" +
                "<td>"+ results[i].team +"</td>" +
                "<td>"+ users[i].email +"</td>" +
                "<td>"+ results[i].extension +"</td>" +
                "<td>"+ results[i].phone_number +"</td>"
            "</tr>";
    }
    resultsHtml += "</table>";
    document.getElementById('main').innerHTML = resultsHtml;
}
