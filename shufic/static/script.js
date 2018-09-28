
jQuery("document").ready(function(){

    jQuery("#like").on('click', function(){

            var href = document.getElementById('like').name;
            jQuery.ajax({
                type: "GET",

                url: "/Eminem/addlike/ajax/",

                data:{ "addlike" : href,},

                dataType: "text",

                catch: false,

                success: function(data){
                    jQuery("#count").html(data);
                }
            });
    });
});