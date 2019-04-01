function change_color(id)
{
    var square = document.getElementById(id);
    square.style.backgroundColor = rgb(255,0,0);
};

function update_color()
{
    $.ajax({
        url: '/upd/',
        method: 'GET',
        success: function (data)
            {
                debugger;
                console.log(data)
                //change_color(data)
            },
        error: function(data)
            {
                loadOff();
            } 
    })
}