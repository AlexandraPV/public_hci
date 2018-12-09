var App = {};

App.main = function() {

   var init =  function(){
        console.log('init!');
   };


    return {
        init : init
    }
}();


$(document).ready(function() {
    App.main.init();
})
