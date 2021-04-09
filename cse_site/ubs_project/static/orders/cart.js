document.addEventListener('DOMContentLoaded', () => {
    optionElts = document.querySelectorAll("option");
    optionElts.forEach(element => {
        if (element.value == element.parentNode.dataset.quantity) {
                element.selected = true;
        }
    });

    selectElts = document.querySelectorAll('select');
    selectElts.forEach(element => {
        element.addEventListener('change', async () => {
            await changeQuantityTo(element.dataset.id, element.options[element.selectedIndex].value)
        });
    });

    orderBtn = document.getElementById('order-btn');
    orderBtn.addEventListener('click', () => {
        const req = new XMLHttpRequest();
        const csrfToken = Cookies.get('csrftoken');
        req.open('GET', '/cart/order');
        req.setRequestHeader('X-CSRFToken', csrfToken);
        req.onload = () => {
            window.location.href = "/cart";
        }
        req.send(false);
    });
});

async function changeQuantityTo(line_id, quantity) {
    const req = new XMLHttpRequest();
    const csrfToken = Cookies.get('csrftoken');
    req.open('POST', '/cart/'+line_id);
    req.setRequestHeader('X-CSRFToken', csrfToken);
    req.onload = () => {
        window.location.href = "/cart";
    };

    data = new FormData();
    data.append("quantity", quantity);
    req.send(data);
}