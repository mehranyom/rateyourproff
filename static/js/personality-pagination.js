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