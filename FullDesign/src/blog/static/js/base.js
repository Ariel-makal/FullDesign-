document.addEventListener("DOMContentLoaded", function() {
    const products = [
        {
            name: "Ensemble Chic",
            price: "59.90",
            image: "https://via.placeholder.com/300x180?text=Ensemble+Chic"
        },
        {
            name: "Ensemble Sport",
            price: "49.90",
            image: "https://via.placeholder.com/300x180?text=Ensemble+Sport"
        },
        {
            name: "Ensemble Été",
            price: "39.90",
            image: "https://via.placeholder.com/300x180?text=Ensemble+Été"
        },
        {
            name: "Ensemble Casual",
            price: "44.90",
            image: "https://via.placeholder.com/300x180?text=Ensemble+Casual"
        }
    ];

    const grid = document.getElementById('products');
    products.forEach(product => {
        grid.innerHTML += `
            <div class="card">
                <img src="${product.image}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.price} €</p>
                <button>Voir le produit</button>
            </div>
        `;
    });
});
//Menu burger toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const burger = document.getElementById('burger-menu');
    const nav = document.getElementById('main-nav');
    burger.addEventListener('click', function() {
        nav.classList.toggle('active');
    });
});