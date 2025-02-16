// async function fetchProducts() {
//     try {
//         const response = await fetch('http://127.0.0.1:8000/posts/postlist/');
//         const products = await response.json();
   
        
//         // productContainer.innerHTML = ''; // Clear previous content

//         products.forEach(product => {
//             // console.log(product)
//             const productContainer = document.getElementById('product-container');
//             const div = document.createElement("div")
//             // console.log(product.image)
//             div.innerHTML = `
//                 <div class="bg-white rounded-lg shadow-lg overflow-hidden">
//                     <img src="${product.image}" 
//                         alt="${product.name}" class="w-full h-48 object-cover">
//                     <div class="p-4">
//                         <h3 class="text-lg font-semibold text-gray-800">${product.name}</h3>
//                         <p class="text-gray-600 mt-2">${product.descirption}</p>
//                         <p class="mt-2 text-xl font-bold text-blue-500">$${product.price}</p>
//                     </div>
//                     <div class="p-4 flex justify-between">
//                         <a href="details.html?id=${product.id}" 
//                             class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700" target="_blank">
//                             Details
//                         </a>
//                         <button class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-700">
//                             Add to Cart
//                         </button>
//                     </div>
//                 </div>
//             `;
//             productContainer.appendChild(div);
//         });
//     } catch (error) {
//         console.error("Error fetching products:", error);
//         document.getElementById('product-container').innerHTML = "<p class='text-red-600 font-semibold'>Failed to load products</p>";
//     }
// }

// fetchProducts();



const baseURL = "https://sporting-server-pmrvwpqq4-rabiul-hosens-projects.vercel.app/posts/postlist/";
const user_id = localStorage.getItem("user_id");

// console.log(user_id); 
const productLoad = () => {
  fetch(baseURL)
    .then((res) => res.json())
    .then((data) => displayProduct(data))
    // .then((data) => console.log(data))
    .catch((error) => console.error("Error fetching data:", error));
};


const displayProduct = (products) => {
    // console.log(products);
  const parent = document.getElementById("slider-container");
  parent.innerHTML = ""; 

  products.forEach((product) => {
    // console.log(product.id);
    const li = document.createElement("li");
    // const imageUrl = product.image.startsWith("http") ? product.image : `${baseURL}${product.image}`;

    // const descriptionText = (product.description || "").trim();
    // const descriptionWords = descriptionText.split(/\s+/).slice(0, 5).join(" ") + "...";

    li.innerHTML = `

  <div class="card border-0 shadow-lg rounded-1 overflow-hidden bg-white">
  <div class="position-relative">
    <img src="$" class="card-img-top img-fluid" loading="lazy" alt="${product.name}">
    <span class="badge bg-success position-absolute top-0 end-0 m-2 px-3 py-2">Stock: ${product.stock}</span>
  </div>
  
  <div class="card-body d-flex flex-column p-4">
    <h5 class="card-title text-dark fw-bold">${product.name}</h5>
    <p class="card-text text-muted small flex-grow-1">${product.descirption}</p>
    <h6 class="text-primary fw-bold">Price: $${product.price}</h6>

    <div class="d-flex justify-content-between mt-3">

       <a href="details.html?id=${product.id}" class="btn btn-outline-primary me-2"><i class="fas fa-info-circle"></i> Details</a>
      
    <button class="btn btn-primary btn-sm w-50 add-to-cart" data-id="${product.id}" data-name="${product.name}" data-price="${product.price}">
    <i class="fas fa-shopping-cart"></i> Add To Cart
    </button>

  </div>
  </div>
</div>
    `;
    parent.appendChild(li);
  });
}
productLoad();