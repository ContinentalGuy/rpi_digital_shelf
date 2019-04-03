function changeColor(slotsNcolors)
{
    for (i=0; i <= slotsNcolors.length; i++)
    {
        let square = document.getElementById('s'+i);
        square.style.backgroundColor = slotsNcolors[i];
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
                changeColor(data);
                return data;
            },
        error: function(data)
            {
                console.log('Error')
            } 
    })
    return data;
}