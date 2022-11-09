function order_category(id) {
    console.log("ID",id)
    url = `/order_category/`
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            id: id,
        }),
    }).then((response) => {
        response.json().then((data) => {
            console.log(data)
        })
    })
}