function changeColor(slotsNcolors)
{
    var i;
    for (i=0; i < slotsNcolors.length; i++)
    {
        let counter = i + 1;
        let squareName = 's' + counter;
        document.getElementById(squareName).style.backgroundColor = slotsNcolors[i];
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
}
