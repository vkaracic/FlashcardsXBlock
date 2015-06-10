/* Javascript for FlashcardsXBlock. */
function FlashcardsXBlock(runtime, element) {
    /* Show the answer of the question by cliking on the question */
    $('.fc-question').click(function() {
        $('.fc-answer').css('visibility', 'visible');
    });
yvxcvfsdg

    /* Initializing the variables for displaying the current question
       and total questions.
    */
    var current_number = parseInt($('.current-fc').text())+1;
    var total_number = parseInt($('.fc-total').text());

    /* Hide all elements for the first iteration */
    $('.flashcards_block li').hide();
    $('.next-btn').click(function() {

        /* Hide the answer again */
        $('.fc-answer').css('visibility', 'hidden');

        /* Removing the previous question. Have trouble figuring out how to
           make it work without removing the previous question.
           TO-DO: Figure this out!
        */
        $('.flashcards_block > ul > li:visible:first').remove();
        $('.flashcards_block > ul > li:hidden:first').show();
        $('.next-btn').html('NEXT');
        $('.current-fc').html(current_number++);

        /* If the student reaches the end say FINISHED and disable going further */
        if (current_number == total_number+1) {
            $('.button').html('FINISHED!');
            $('.button').addClass('finished-btn').removeClass('next-btn').off('click');
        }
    });
}
