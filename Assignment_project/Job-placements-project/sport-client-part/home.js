console.log("Yes")
const baseURL = "https://sporting-server-xi.vercel.app/posts/postlist/";
const user_id = localStorage.getItem("user_id");

console.log(user_id); 
const productLoad = () => {
  fetch(baseURL)
    .then((res) => res.json())
    .then((data) => displayProduct(data))
    .then((data) => console.log(data))
    .catch((error) => console.error("Error fetching data:", error));
};


const displayProduct = (products) => {
  console.log(products);
  const parent = document.getElementById("slider-container");
  parent.innerHTML = ""; 

  products.forEach((product) => {

    const parent = document.getElementById("slider-container");
    const li = document.createElement("div");
    li.className = "min-w-[220px] bg-white shadow-md rounded-lg overflow-hidden border border-gray-300 transition-transform transform hover:scale-105";
    
    li.innerHTML = `
      <div class="relative">
        <img src="${product.image.url}" class="w-full h-36 object-cover" loading="lazy" alt="${product.name}">
        <span class="absolute top-2 right-2 bg-green-600 text-white text-xs px-2 py-1 rounded-full">Stock: ${product.storkQuantity}</span>
      </div>
      <div class="p-3 flex flex-col">
        <h5 class="text-sm font-semibold text-gray-800">${product.name}</h5>
        <p class="text-xs text-gray-600 flex-grow mt-1">${product.description}</p>
        <h6 class="text-blue-600 font-bold mt-2 text-sm">Price: $${product.price}</h6>
        <div class="flex justify-between items-center mt-3">
          <a href="cart_details.html?product_id=${product.id}" class="text-blue-500 hover:text-blue-700 text-xs font-medium flex items-center">
            <i class="fas fa-info-circle mr-1"></i> Details
          </a>
          <button class="bg-blue-600 text-white text-xs px-3 py-1 rounded-md flex items-center hover:bg-blue-700 transition add-to-cart" data-id="${product.id}" data-name="${product.name}" data-price="${product.price}" data-stock="${product.stock}">
            <i class="fas fa-shopping-cart mr-1"></i> Add To Cart
          </button>
        </div>
      </div>
    `;
    parent.appendChild(li);
  });

//     const li = document.createElement("li");
//     const imageUrl = product.image.startsWith("http") ? product.image : `${baseURL}${product.image}`;

//     const descriptionText = (product.description || "").trim();
//     const descriptionWords = descriptionText.split(/\s+/).slice(0, 5).join(" ") + "...";

//     li.innerHTML = `

//   <div class="card border-0 shadow-lg rounded-1 overflow-hidden bg-white">
//   <div class="position-relative">
//     <img src="" class="card-img-top img-fluid" loading="lazy" alt="${product.name}">
//     <span class="badge bg-success position-absolute top-0 end-0 m-2 px-3 py-2">Stock: ${product.storkQuantity}</span>
//   </div>
  
//   <div class="card-body d-flex flex-column p-4">
//     <h5 class="card-title text-dark fw-bold">${product.name}</h5>
//     <p class="card-text text-muted small flex-grow-1">${product.descirption}</p>
//     <h6 class="text-primary fw-bold">Price: $${product.price}</h6>

//     <div class="d-flex justify-content-between mt-3">

//        <a href="cart_details.html?product_id=${product.id}" class="btn btn-outline-primary me-2"><i class="fas fa-info-circle"></i> Details</a>
      
//     <button class="btn btn-primary btn-sm w-50 add-to-cart" data-id="${product.id}" data-name="${product.name}" data-price="${product.price}" data-stock="${product.stock}">
//     <i class="fas fa-shopping-cart"></i> Add To Cart
//      </button>

//   </div>
//   </div>
// </div>
//     `;
//     parent.appendChild(li);
//   });

  // Attach event listeners to "Add to Cart" buttons
  document.querySelectorAll(".add-to-cart").forEach((button) => {
    console.log("Yes")
    button.addEventListener("click", (event) => {
      const product = {
        id: event.target.dataset.id,
        name: event.target.dataset.name,
        price: parseFloat(event.target.dataset.price),
        stock: parseInt(event.target.dataset.storkQuantity),
        quantity: 1, // Default quantity
      };
      addToCart(product);
    });
  });
};

// Add product to cart

const addToCart = (product) => {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const existingProduct = cart.find((item) => item.id === product.id);

  if (existingProduct) {
    if (existingProduct.quantity < product.storkQuantity) {
      existingProduct.quantity++;
    } else {
      alert("No more stock available!");
    }
  } else {
    cart.push(product);
  }

  localStorage.setItem("cart", JSON.stringify(cart));
  alert(`${product.name} added to cart!`);
};

productLoad();










