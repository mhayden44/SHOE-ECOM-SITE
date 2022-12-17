// Each shoe has an add to cart button that allows for it to be added to the user's cart.
let btns = document.getElementsByClassName('addtocart')
for(let i = 0; i < btns.length; i++){
    btns[i].addEventListener('click', function(){
        let shoeId = this.dataset.shoe
        let action = this.dataset.action
        location.reload()    
        if (user === "AnonymousUser"){
            console.log("User is not logged in")
        }
        else{ // Changes text on "Add to Cart" button to "Adding to cart..." when it is pressed for a brief time
            this.textContent = "Adding to cart...";
            updateCart(shoeId, action)
            .then(() => {
                // Reset the text on the button after the item has been added to the cart
                this.textContent = "Add to Cart";
              });
        }
    })
}

// Updates the user's cart when they add a shoe to it.
function updateCart(id, action){
    let url = "/updatecart"
    fetch(url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({"shoeId": id, "action": action})
    })
    .then(response => response.json())
    .then(data => console.log(data))
}

// Allows for the quantity of each shoe within the user's cart to be changed.
let quantityField = document.getElementsByClassName('quantity')
for(let i = 0; i <quantityField.length; i++){
    quantityField[i].addEventListener('change',function(){
        let quantityFieldValue = quantityField[i].value
        let quantityFieldShoe = quantityField[i].parentElement.parentElement.children[1].children[0].innerText
        location.reload()
        let url = "/updatequantity"
        fetch(url, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body : JSON.stringify({ "qfv":quantityFieldValue, "qfp": quantityFieldShoe,})
        })
        .then(response => response.json())
        .then(data => console.log(data))
    })
}