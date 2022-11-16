function get_category(id){
    console.log("ID",id)
    url = `/get_category/`
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
            var products = data.products
            html = ``
            if(products.length == 0){
                alert('no data')
                return
            }
            for(let i=0;i<products.length;i++){
            html += `
                    <div class="col-xl-3 col-lg-4 col-md-4 col-12">
                        <div class="single-product">
                            <div class="product-img">
                                <a href="product-details.html">
                                    <img  class="default-img" src="${products[i].image}" alt="#">
                                    <img  class="hover-img" src="${products[i].image}" alt="#">`
                                if((products[i].price-products[i].discount)/products[i].price*100>20){
                                    html+=`<span class="out-of-stock">Sale</span>`
                                }
                                html +=`</a>
                                <div class="button-head">
                                    <div class="product-action">
                                        <a data-toggle="modal" data-target="#exampleModal"
                                           title="Quick View" href="#"><i class=" ti-eye"></i><span>Quick Shop</span></a>
                                        <a title="Wishlist" href="#"><i class=" ti-heart "></i><span>Add to Wishlist</span></a>
                                        <a title="Compare" href="#"><i
                                                class="ti-bar-chart-alt"></i><span>Add to Compare</span></a>
                                    </div>
                                    <div class="product-action-2">
                                        <a title="Add to cart" onclick="add_product(${products[i].id})">Add to cart</a>
                                    </div>
                                </div>
                            </div>
                            <div class="product-content">
                                <h3><a href="product-details.html">${products[i].name}</a></h3>
                                <div class="product-price">`
                                    if(products[i].discount != products[i].price){
                                       html+=` <span class="old">$${products[i].price}</span>
                                        <span>$${products[i].discount}</span>`}
                                    else{
                                        html +=`<span>$${products[i].price}</span>`}
                                html+=`</div>
                            </div>
                        </div>
                    </div>`
            document.getElementById('category_prods').innerHTML = html
            }
        })
    })
}


function add_product(id){
    console.log("ID",id)
    url = `/add_product/`
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
            html = ``
            for(let i=0;i<data.data.length;i++){
                html += `
                    <li id="list_product${data.data[i].id}">
                        <a onclick="remove_product(${data.data[i].id})" class="remove" title="Remove this item"><i class="fa fa-remove"></i></a>
                        <a class="cart-img" href="#"><img src="${data.data[i].image}" alt="#"></a>
                        <h4><a href="#">${data.data[i].name}</a></h4>
                        <p class="quantity" ><span id="quantity${data.data[i].id}">${data.data[i].quantity}</span>x - <span class="amount">$${data.data[i].price}</span></p>
                    </li>
                `
            }
            item_count = document.getElementById('item_total_count')
            item_count.style.display = 'inline'
            item_count.innerHTML = data.count
            document.getElementById('item_total_count(2)').innerHTML = data.count
            document.getElementById('shopping_list').innerHTML = html
            document.getElementById('total_price').innerHTML ='$'+data.total_price
            })
        })
}

function remove_product(id){
    console.log("ID",id)
    url = `/remove_product/`
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
            console.log(data,typeof data.success)
            if(data.success == true){
                const list_product = document.getElementById('list_product'+id.toString())
                list_product.style.display = 'none'
            }

            item_count = document.getElementById('item_total_count')
            item_count.style.display = 'inline'
            item_count.innerHTML = data.count

            if(data.count === 0){
                item_count.style.display = 'none'
            }
            document.getElementById('item_total_count(2)').innerHTML = data.count
            document.getElementById('total_price').innerHTML ='$'+data.total_price
            })
        })
}