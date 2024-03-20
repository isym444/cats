// $(document).ready(function () {
//     alert('Hello, world!');
// });

// $(document).ready(function(){
//     $('#about-btn').click(function(){
//         alert("You clicked the button using JQuery!");
//     })
// })


$(document).ready(function(){
    $('p').hover(function(){
        $(this).css('color', 'red');
    }, function(){
        $(this).css('color', 'black');
    });
$("#about-btn").removeClass('btn-primary').addClass('btn-success');
    $('#about-btn').click(function () {
        msgStr = $('#msg').html();
        msgStr = msgStr + ' ooo, fancy!';
        $('#msg').html(msgStr);
    });
})


