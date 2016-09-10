var form = document.getElementById('file-form');
var fileSelect = document.getElementById('file-select');

form.onsubmit = function(event) {
  event.preventDefault();

    // Get the selected files from the input.
    var files = fileSelect.files;
    
    // Create a new FormData object.
    var formData = new FormData();
    
    // Files
    formData.append('photo', files[0], files[0].name);
    console.log(formData);
    // Set up the request.
    var xhr = new XMLHttpRequest();
    // Open the connection.
    xhr.open('POST', '/upload', true);
    xhr.send(formData)
    xhr.onload = function () {
      if (xhr.status === 200) {
        // File(s) uploaded.
        //uploadButton.innerHTML = 'Upload';
        alert('File uploaded');
      } else {
        alert('An error occurred!');
      }
    };
}