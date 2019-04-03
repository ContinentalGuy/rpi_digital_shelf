function changeColor(slotsNcolors)
{
    for (i=0; i <= slotsNcolors.length; i++)
    {
        var square = document.getElementById(slotsNcolors[]);
        square.style.backgroundColor = 'rgb(255,0,0)';
    }
    
};

function updateColor()
{
    $.ajax({
        url: '/upd/',
        method: 'GET',
        success: function (data)
            {
                debugger;
                console.log(data);
                //changeColor(data);
                return data;
            },
        error: function(data)
            {
                console.log('Error')
            } 
    })
    return data;
}