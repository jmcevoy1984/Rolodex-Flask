window.onload = function(){
    var name = document.getElementById('name');
    var role = document.getElementById('role');
    var detailsTable = document.getElementById('details-table');
    var detailsLen = detailsTable.innerHTML.length;
    var contactTable = document.getElementById('contact-table');
    var contactLen = contactTable.innerHTML.length;
    xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/staff/' + id);
    xhr.send();
    xhr.onload = function(){
        var dutiesString = '';
        var resp = JSON.parse(xhr.responseText);
        console.log(resp.profile_image_uri);
        //document.getElementById('profile_pic').innerHTML = "<img src='" + resp.profile_image_uri + "'>";
        name.innerHTML = resp.first_name + ' ' + resp.last_name;
        role.innerHTML = resp.role;
        document.getElementById('team').innerHTML = resp.team;
        document.getElementById('team-lead').innerHTML = resp.team_lead;
        document.getElementById('manager').innerHTML = resp.manager;
        document.getElementById('location').innerHTML = resp.location;
        document.getElementById('regions').innerHTML = resp.active_regions;
        document.getElementById('mobile').innerHTML = resp.phone_number;
        document.getElementById('extension').innerHTML = resp.extension;
        document.getElementById('office-hours').innerHTML = resp.office_hours;
        document.getElementById('duties-box').innerHTML = resp.duties;
        req = new XMLHttpRequest();
        req.open('GET', '/api/users/' + id);
        req.send();
        req.onload = function(){
            var response = JSON.parse(req.responseText);
            document.getElementById('email').innerHTML = response.email;
            document.getElementById('profile_pic').innerHTML = "<img src='" + response.profile_image_uri + "'>";
        }
        
    }
};

function editDetails(){
    window.location = '/update/' + id;
}