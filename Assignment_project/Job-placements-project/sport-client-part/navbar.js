const navbarLoad = () => {
    const navbar = document.getElementById("navbarElement");
    const user_id = localStorage.getItem("user_id");

    navbar.innerHTML = `
        <div class="container mx-auto flex justify-between items-center">
            <!-- Left Side - Logo -->
            <div class="flex items-center space-x-3">
                <img src="./images/product-img/football.png" alt="Sport Club Logo" class="h-12 w-12 rounded-full">
                <span class="text-2xl font-bold tracking-wide">Sport Club</span>
            </div>

            <!-- Middle - Navigation Links -->
            <div class="hidden md:flex space-x-6">
                <a href="home.html" class="nav-link">Home</a>
                <a href="products.html" class="nav-link">Products</a>
                <a href="contact_us.html" class="nav-link">Contact</a>
                <a href="about_us.html" class="nav-link">About Us</a>
            </div>

            <!-- Right Side - User Profile & Cart -->
            <div class="flex items-center space-x-6">
                <a href="cart.html" class="relative">
                    <i class="fas fa-shopping-cart text-white text-xl"></i>
                    <span class="absolute top-0 right-0 bg-red-600 text-white text-xs px-1 rounded-full">3</span>
                </a>

                ${user_id ? `
                <div class="relative">
                    <button onclick="toggleDropdown()" class="profile-btn">
                        <i class="fas fa-user text-lg"></i>
                        <i class="fas fa-caret-down text-sm"></i>
                    </button>

                    <div id="dropdown-menu" class="hidden absolute right-0 mt-2 w-44 bg-white text-black rounded-lg shadow-lg overflow-hidden">
                        <a href="profile.html" class="dropdown-item">Profile</a>
                        <form id="logout" onsubmit="handleLogout(event)">
                            <button type="submit" class="dropdown-item w-full text-left">Logout</button>
                        </form>
                    </div>
                </div>` : `
                <a href="login.html" class="btn-outline">Login</a>
                <a href="registration.html" class="btn-primary">Register</a>`}
            </div>
        </div>
    `;
};

// Call function to load navbar
navbarLoad();
