var App = App || {};

App.ajax = function() {

    var init  = function() {
        send_ajax();
    };

    var send_ajax = function() {
        $('.js-add-backet').click(function(e){
            e.preventDefault();
            var id_product = $(this).data('id');
            console.log(id_product);
            $.ajax({
                method: "GET",
                url: $(this).prop('href'),
                data: {
                    id: $(this).data('id'),
                    category: $(this).data('category')
                },
                success: function(data){
                    console.log(data);
                }
            });

            console.log($(this).prop('href'));
        });

    };


    return {
        init : init
    }
}();