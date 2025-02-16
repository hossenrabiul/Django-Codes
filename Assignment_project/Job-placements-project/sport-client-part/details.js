async function fetchPostDetails() {
    // Get the post ID from the URL
    const urlParams = new URLSearchParams(window.location.search);
    const postId = urlParams.get('id');

    if (!postId) {
        document.getElementById('post-details').innerHTML = "<p class='text-red-600 font-semibold'>Invalid Post ID</p>";
        return;
    }

    try {
        const response = await fetch(`https://sporting-server-pmrvwpqq4-rabiul-hosens-projects.vercel.app/posts/postdetail/${postId}/`);
        const post = await response.json();
        const div = document.createElement("div")
        const parent = document.getElementById("post-details")
        // console.log(post)
        div.innerHTML = `
            <img id="post-image" src="${post.image}" alt="Post Image" class="w-full h-64 object-cover rounded-lg shadow-md mb-4">
            <h2 id="post-title" class="text-3xl font-bold text-gray-800 mb-4">${post.name}</h2>
            <p id="post-content" class="text-gray-700 leading-relaxed">$${post.price}</p>
            <p id="post-content" class="text-gray-700 leading-relaxed">${post.rating}</p>
            <div class="p-4">
                <button class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-700">
                Add to Cart
                </button>
            </div>
        `;
        
        parent.appendChild(div)
        console.log(parent)
        // document.getElementById('post-image').src = post.image;
        // document.getElementById('post-title').textContent = post.title;
        // document.getElementById('post-content').textContent = post.content;
    } catch (error) {
        document.getElementById('post-details').innerHTML = "<p class='text-red-600 font-semibold'>Error loading post details</p>";
    }
}

function goBack() {
    window.history.back();
}

fetchPostDetails();