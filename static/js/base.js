// // Delete item from cart and reload 
// $('.remove-item').click(function(e) {
//     var csrfToken = "{{ csrf_token }}";
//     var itemId = $(this).attr('id').split('remove_')[1];
//     var url = `/bag/remove/${itemId}/`;
//     var data = {'csrfmiddlewaretoken': csrfToken};

//     $.post(url, data).done(function() {
//         location.reload();
//     });
// })