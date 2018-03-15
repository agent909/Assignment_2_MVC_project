$(function(){
    $("#makeIncubator").click(function(){
        name = $("#incubatorName").val();
        rows = $("#rows").val();
        columns = $("#columns").val();

        if(name == ''){
            $("#incubatorName").attr("style","border-color:red;");
            $("#label1").text("This Field is Required");
        }

        if(rows == ''){
            $("#rows").attr("style","border-color:red;");
            $("#label2").text("This Field is Required");
        }

        if(columns == ''){
            $("#columns").attr("style","border-color:red;");
            $("#label3").text("This Field is Required");
        }

        if(name!='' && rows!='' && columns!=''){
            $("#IncubatorForm").submit();
            alert("what???");
        }

    });
});
