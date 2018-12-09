var App = App || {};

App.products_all = function() {

    var init =  function() {
        console.log('init!!jahdb!')
        gallery();
       };

    var gallery =  function() {
    $('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:2,
            nav:false
        },
        1440:{
            items:3,
            nav:true,
            loop:false
        }
    }
})
    }

       return {
        init: init
       }

}();