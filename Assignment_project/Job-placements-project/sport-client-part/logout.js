const handleLogout = (event) => {
    event.preventDefault();
  
      console.log("Logging out...");
      const token = localStorage.getItem("token");
      console.log(token);
      fetch("https://sporting-server-xi.vercel.app/accounts/logout/", {
        method: "GET",
        headers: {
          Authorization: `Token ${token}`,
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("Logout successful", data);
          localStorage.removeItem("token");
          localStorage.removeItem("user_id");
  
  
          Swal.fire({
            title: 'Success!',
            text: 'Your account has been successfully logged out.',
            icon: 'success',
            confirmButtonText: 'OK'
          }).then(()=>{
             window.location.href="home.html";
          })
          
        })
      
    };
    