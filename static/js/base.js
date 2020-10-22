// // Delete item from cart and reload 
// $('.delete-item').click(function() {
//     var csrfToken = "{{ csrf_token }}";
//     var itemId = $(this).attr('id').split('remove_')[1];
//     var url = `/bag/remove/${itemId}/`;
//     var data = {'csrfmiddlewaretoken': csrfToken};
//     $(this).css("background-color", "red");
//     $.post(url, data).done(function() {
//         location.reload();
//     });
// })