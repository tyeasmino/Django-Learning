const loadCategory = () => {
    fetch('https://fakestoreapi.com/products/categories')
        .then(res=>res.json())
        .then(data=>displayCategory(data))
} 

const displayCategory = (data) => {
    const parent = document.getElementById("product-category")
    data.forEach(item => {
        const li = document.createElement("li")
        li.classList.add("capitalize")
        li.classList.add("mx-1")
        const button = document.createElement("button")
        button.textContent = item
        button.onclick = () => loadProducts(item)

        li.appendChild(button)
         
        parent.appendChild(li) 
    });
}

 

const loadProducts = (category = '') => {
    const productContainer = document.getElementById("product-container");
     
    productContainer.innerHTML = '';   
    document.getElementById("spinner").style.display = "block";   

    let url = 'https://fakestoreapi.com/products';  

    if (category) {        
        url = `https://fakestoreapi.com/products/category/${category}`;
    }

    fetch(url)
        .then(res => res.json())
        .then(data => {
            document.getElementById("spinner").style.display = "none";  // Hide spinner

            if (data.length > 0) {
                displayProducts(data);  // Call display function if products are found
            } 
        })
        .catch(error => {
            console.error("Error fetching products:", error);
            document.getElementById("spinner").style.display = "none";  // Hide spinner on error
        });
    
};






const displayProducts = (products) => {
    products?.forEach(product => {
        const parent = document.getElementById("product-container")
        const div = document.createElement("div")
        div.classList.add("card")
        div.classList.add("bg-base-100")
        div.classList.add("w-96")
        div.classList.add("shadow-xl")

        div.innerHTML = `
            <figure>
                <img class="h-40" src=" ${product.image} " />
            </figure>
            <div class="card-body">
                <h2 class="card-title"> ${product.title} </h2>
                <p> ${product.description.slice(0,50)} </p>
                <div class="card-actions justify-end">
                <button class="btn btn-primary"> 
                    <a href="productDetails.html?productId=${product.id}"> Details </a>
                </button>
                </div>
            </div>
        `

        parent.appendChild(div) 
    })
}



loadCategory() 
loadProducts() 