var saveButton = document.getElementById('save');

saveButton.addEventListener('click', saveImage);

function saveImage()
{
    var data = canvas.toDataURL();

    var request = new XMLHttpRequest();

    // request.onreadystatechange = function(){
    //     if(request.readyState == 4 && request.status == 200){
    //         var response = request.responseText;
    //         //  console.log('img='+data);
    //         // window.open(response, '_blank', 'location=0, menubar=0')
    //         // window.open('download.php?file='+response, '_blank', 'location=0, menubar=0')
    //         document.getElementById('downloadframe').src = 'save.php?file='+response;
    //     }
    // }

    request.open('POST', 'save.php', true);
    request.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    request.send('img='+data);
    // window.open(data, '_blank', 'location=0, menubar=0')
}