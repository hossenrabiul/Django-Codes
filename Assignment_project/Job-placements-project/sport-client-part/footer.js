document.addEventListener("DOMContentLoaded", function () {
    const footer = document.querySelector("footer");
    footer.innerHTML = `
      <div class="bg-gray-900 text-white py-10">
        <div class="container mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6 px-6">
          <!-- First Column: Newsletter -->
          <div>
            <h3 class="text-lg font-semibold mb-2">Stay Updated</h3>
            <p class="text-gray-400 mb-3">Subscribe to get the latest updates.</p>
            <div class="flex items-center space-x-2">
              <input type="email" placeholder="Enter your email" class="p-2 rounded-lg text-black w-full" />
              <button class="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg">Subscribe</button>
            </div>
          </div>
  
          <!-- Second Column: Social -->
          <div>
            <h3 class="text-lg font-semibold mb-2">Social</h3>
            <ul class="text-gray-400 space-y-2">
              <li><a href="#" class="hover:text-white"><i class="fab fa-facebook-f"></i> Facebook</a></li>
              <li><a href="#" class="hover:text-white"><i class="fab fa-twitter"></i> Twitter</a></li>
              <li><a href="#" class="hover:text-white"><i class="fab fa-instagram"></i> Instagram</a></li>
              <li><a href="#" class="hover:text-white"><i class="fab fa-linkedin-in"></i> LinkedIn</a></li>
            </ul>
          </div>
  
          <!-- Third Column: Products -->
          <div>
            <h3 class="text-lg font-semibold mb-2">Products</h3>
            <ul class="text-gray-400 space-y-2">
              <li>Football</li>
              <li>Basketball</li>
              <li>Cricket Bat</li>
              <li>Running Shoes</li>
              <li>Gym Equipment</li>
            </ul>
          </div>
  
          <!-- Fourth Column: Contact -->
          <div>
            <h3 class="text-lg font-semibold mb-2">Contact</h3>
            <p class="text-gray-400">Your Name</p>
            <p class="text-gray-400">123 Street, City</p>
            <p class="text-gray-400">+123 456 7890</p>
            <p class="text-gray-400">your.email@example.com</p>
          </div>
        </div>
      </div>
    `;
  });
  