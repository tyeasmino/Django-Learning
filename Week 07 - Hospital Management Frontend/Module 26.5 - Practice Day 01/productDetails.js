const getParams = () => {
    const param = new URLSearchParams(window.location.search).get("productId");
    console.log(param);

    fetch(`https://fakestoreapi.com/products/${param}`)
        .then(res => res.json())
        .then(data => displayDetails(data))
}

const displayDetails = (product) => {
    const parent = document.getElementById("product-details");


    parent.innerHTML = `         
        <div class="card card-side bg-base-100 shadow-xl p-5">
            <figure >
                <img class="p-5 max-h-96 object-cover"
                src= "${product.image}" />
            </figure>
            <div class="card-body">
                <h2 class="card-title">${product.title}</h2>
                <p><strong>Category:</strong> ${product.category}</p>
                <p>${product.description}</p>
           
                

                <div class="stats shadow">
                    <div class="stat">
                        <div class="stat-figure text-secondary">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            class="inline-block h-8 w-8 stroke-current">
                            <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                        </svg>
                        </div>
                        <div class="stat-title">Rating Rate</div>
                        <div class="stat-value">${product.rating.rate}</div>
                        <div class="stat-desc">Jan 1st - Feb 1st</div>
                    </div>

                    <div class="stat">
                        <div class="stat-figure text-secondary">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            class="inline-block h-8 w-8 stroke-current">
                            <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path>
                        </svg>
                        </div>
                        <div class="stat-title">Rating Count</div>
                        <div class="stat-value">${product.rating.count}</div>
                        <div class="stat-desc">↗︎ 400 (22%)</div>
                    </div>

                    <div class="stat">
                        <div class="stat-figure text-secondary">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            class="inline-block h-8 w-8 stroke-current">
                            <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"></path>
                        </svg>
                        </div>
                        <div class="stat-title">Price</div>
                        <div class="stat-value">${product.price}$</div>
                        <div class="stat-desc">↘︎ 90 (14%)</div>
                    </div>
                </div>
                
                
     
                <div class="card-actions justify-end">
                <button class="btn btn-primary">Add to Cart</button>
                </div>
            </div>
        </div>
    `    
}


getParams()