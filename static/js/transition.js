$('#cleansersbtn').on('click', function(){
    $('#cleansers').show('fast')
    $('#creams').hide('slow')
    $('#serums').hide('slow')
    $('#vitamins').hide('slow')
    ;
});
$('#creamsbtn').on('click', function(){
    $('#cleansers').hide('slow')
    $('#creams').show('fast')
    $('#serums').hide('slow')
    $('#vitamins').hide('slow')
    ;
});
$('#serumsbtn').on('click', function(){
    $('#cleansers').hide('slow')
    $('#creams').hide('slow')
    $('#serums').show('fast')
    $('#vitamins').hide('slow')
    ;
});
$('#vitaminsbtn').on('click', function(){
    $('#cleansers').hide('slow')
    $('#creams').hide('slow')
    $('#serums').hide('slow')
    $('#vitamins').show('fast')

    ;
});



//dashboard
$('#add-item').on('click', function(){
      $("#item-form").show('slow')
      $("#user-form").hide('fast')
      $("#widget-1").hide('fast')
      $("#widget-2").hide('fast')
      ;
    });

$('#new-user').on('click', function(){
        $("#user-form").show('slow')
        $("#item-form").hide('fast')
        $("#widget-1").hide('fast')
        $("#widget-2").hide('fast')
        ;
      });
  
