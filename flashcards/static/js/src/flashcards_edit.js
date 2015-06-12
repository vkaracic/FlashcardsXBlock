function FlashcardsEditXBlock(runtime, element) {
    $(element).find('.save-button').bind('click', function() {
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');


        /* Every flashcard (fc-item) has two input fields, "front" and "back" */
        var flashcard_list = {};
        var items = document.getElementsByClassName('fc-item');

        for (var i = 0; i < items.length; i++) {
        /* Read every flashcard and save input values to a dictionary object */
            var inputs = items[i].getElementsByTagName('input');
            flashcard_list[inputs[0].value] = inputs[1].value;
        }

        var data = {
            title: $(element).find('input[name=title]').val(),
            flashcards: flashcard_list
        };

        var test = JSON.stringify(data);

        runtime.notify('save', {state: 'start'});
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            runtime.notify('save', {state:'end'});
        });
    });

    $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });
}
