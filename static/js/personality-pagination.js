function change_ta_page_number(plus) {
    var temp_data = parseInt($('#ta-page_number').html());
    $('#ta-page_number').html(temp_data + plus);
  }

  function change_ta(plus) {
    if (question_slide_current_page + plus <= 18 && question_slide_current_page + plus >= 1) {
      $('.ta-slide[data-page=' + question_slide_current_page + ']').css('display', 'none');
      question_slide_current_page += plus;
      $('.ta-slide[data-page=' + question_slide_current_page + ']').css('display', 'block');
      change_ta_page_number(plus);
    }
    if (question_slide_current_page == 18) {
      saw_last_question = true;
    }
  }
  question_slide_current_page = 1;
  saw_last_question = false;
  $('a.ta-arrow-left:not(.disabled)').click(function() {
    change_ta(-1);
  });
  $('a.ta-arrow-right:not(.disabled)').click(function() {
    change_ta(1);
  });
  $('.ta-answer-skip').click(function(e) {
    e.preventDefault();
    change_ta(1);
  });
  $('.ta-answer-box > div').click(function(e) {
    e.preventDefault();
    var selected_radio_input = $(this).find('input');
    question_id = selected_radio_input.prop('name');
    var changing = false;
    if ($('.ta-answer-box').find('[name="' + question_id + '"]:checked').length > 0) changing = true;
    cancel_select = $(this).hasClass('selected');
    nme = $(this).hasClass('nme'); // Not Mutually Exclusive
    if (nme == false) {
      $('.ta-answer-box').find('[name="' + question_id + '"]:checked').parent().parent().removeClass('selected');
      $('.ta-answer-box').find('[name="' + question_id + '"]:checked').removeProp('checked')
      if (cancel_select == false) {
        selected_radio_input.prop('checked', 'true');
        $(this).toggleClass('selected');
      }
    } else {
      if (cancel_select == false) {
        selected_radio_input.prop('checked', 'true');
      } else {
        selected_radio_input.removeProp('checked');
      }
      $(this).toggleClass('selected');
    }
    if (saw_last_question == false && changing == false && nme == false) change_ta(1);
  });

  $('.more-coursegrade').click(function(e) {
    e.preventDefault();
    var baseCoursegrade = $('.coursegrade').clone().first().insertBefore('.more-coursegrade');
    baseCoursegrade.find('.select2').remove();
    baseCoursegrade.find('.visually-hidden').removeClass('visually-hidden');
    baseCoursegrade.find('[selected=selected]').removeAttr('selected');
    baseCoursegrade.attr('notsubmitted', 'true');
    $select2 = $(".select2-js").select2({
      width: '100%',
      escapeMarkup: function (m) {
          return m;
      },
      templateSelection: function (data) {
          return '<span class="select2-coursegrade-selection">' + data.text + '</span>';
      },
      templateResult: function (data) {
          return '<span class="select2-coursegrade-results">' + data.text + '</span>';
      }
    });
    
  });

  $(document).on('click', '.remove-coursegrade-row', function(e) {
    var $row = $(this).parent().parent().parent();
    if (!$row.attr('notsubmitted')) {
      if ($(".review-form").find('.coursegrade').length == 1) {
        $('.more-coursegrade').click();
        $row.remove();
        $('.coursegrade .remove-col').addClass('visually-hidden');
      } else {
        $row.remove();
      }
    } else {
      $row.remove();
    }
  });

  $select2 = $(".select2-js").select2({
    width: '100%',
    escapeMarkup: function (m) {
        return m;
    },
    templateSelection: function (data) {
        return '<span class="select2-coursegrade-selection">' + data.text + '</span>';
    },
    templateResult: function (data) {
        return '<span class="select2-coursegrade-results">' + data.text + '</span>';
    }
});

toastr.options = {
    "closeButton": false,
    "debug": false,
    "newestOnTop": false,
    "progressBar": false,
    "positionClass": "toast-top-center",
    "preventDuplicates": false,
    "onclick": null,
    "showDuration": "300",
    "hideDuration": "1000",
    "timeOut": "5000",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
}