function updateMember(){
    var firstName = document.getElementById('first-name').value;
    var lastName = document.getElementById('last-name').value;
    var role = document.getElementById('member-role').value;
    var team = document.getElementById('team').value;
    var teamLead = document.getElementById('team-lead').value;
    var manager = document.getElementById('manager').value;
    var mobile = document.getElementById('mobile').value;
    var extension = document.getElementById('extension').value;
    var officeHours = document.getElementById('office-hours').value;
    var regions = document.getElementById('regions').value;
    var location = document.getElementById('location').value;
    var duties = document.getElementById('duties').value;
    
    var data = {
        'first_name' : firstName,
        'last_name' : lastName,
        'role' : role,
        'team' : team,
        'team_lead' : teamLead,
        'manager' : manager,
        'phone_number' :  mobile,
        'extension' : extension,
        'office_hours' : officeHours,
        'active_regions' : regions,
        'location' : location,
        'duties' : duties
    };
    console.log(data);
    xhr = new XMLHttpRequest();
    xhr.open('PUT', '/api/staff/' + id);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(data));
    xhr.onload = function(){
        resp = JSON.parse(xhr.responseText);
        var main = document.getElementById('main');
        if(resp.result === true){
            main.innerHTML = "<div class='alert alert-success'>Details sucessfully updated!</div>";
        }
        else{
            main.innerHTML = "<div class='alert alert-danger'>Error: Details Not Updated!</div>";
        }
    }
}