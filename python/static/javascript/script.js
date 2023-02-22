function removeItem(itemId) {
    fetch('/remove_item?id=' + itemId)
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Failed to remove item.');
            }
        })
        .catch(error => {
            console.error(error);
            alert('Failed to remove item.');
        });
}

