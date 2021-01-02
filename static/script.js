$(document).ready(function(){
    $("#addPlant").click(function(){
        var style = $("#plantForm").css("display");
        if(style == "none"){
            $("#plantForm").css("display", "block");
        }
        else{
            $("#plantForm").css("display", "none");
        }
    });
});