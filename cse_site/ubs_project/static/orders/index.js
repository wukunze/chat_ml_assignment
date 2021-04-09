document.addEventListener('DOMContentLoaded', () => {
    
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
    
    addBtns = document.querySelectorAll('.add-btn');
    addBtns.forEach(button => {
        button.addEventListener('click', async () => {
            await addToCart(button.dataset.id);
        })
    });

    
});

async function addToCart(pizza_id) {
    let success = false;
    const req = new XMLHttpRequest();
    const csrfToken = Cookies.get('csrftoken');
    req.open('POST', '/cart');
    req.setRequestHeader('X-CSRFToken', csrfToken);
    req.onload = () => {
        let message = "";
        let buttonText = "GO TO CART";
        let btnHref = "/cart";
        if (req.status == 200){
            let data = req.responseText;
            let state = JSON.parse(data)['message'];
            if (state == 'auth') {
                buttonText = "LOGIN"
                btnHref = "/login"
                message = "Please login to add pizzas to your cart"
            }
            else message = "Your pizza has been added to your cart successfully!";
        } 
        else {
            message = "There has been a problem while adding the pizza to your cart. Please try again.";
        }
        document.getElementById('add-result').innerText = message;
        actionBtn = document.getElementById('modal-action');
        actionBtn.innerText = buttonText;
        actionBtn.href = btnHref;

        let modal = document.getElementById("modal1");
        let instance = M.Modal.getInstance(modal);
        instance.open();
    };
    
    data = new FormData();
    data.append("pizza_id", pizza_id);
    req.send(data);
}