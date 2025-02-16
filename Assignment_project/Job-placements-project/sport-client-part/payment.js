
        document.addEventListener("DOMContentLoaded", function() {
            document.getElementById("paymentButton").addEventListener("click", function() {

                fetch("http://127.0.0.1:8000/payment/pay/", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ amount: 100, currency: "BDT" }) // Add necessary data
                })
                .then(response => response.json())
                .then(data => {
                    console.log("Payment Response:", data); // Debugging
                
                    if (data.payment_url) { 
                        window.location.href = data.payment_url; // Redirect to SSL payment page
                    } else {
                        console.error("Payment Error: Invalid response", data);
                    }
                })
                .catch(error => {
                    console.error("Payment Error:", error);
                });
                


                // fetch("http://127.0.0.1:8000/payment/pay/", {
                //     method: "POST", 
                //     headers: { "Content-Type": "application/json" },
                //     body: JSON.stringify({ amount: 100, currency: "BDT" }) // Add necessary data
                // })
                // .then(response => response.json())
                // .then(data => {
                //     if (data.status === "success") {
                //         window.location.href = data.payment_url; // Redirect to SSL payment page
                //     } else {
                //         console.error("Payment Error:", data);
                //     }
                // })
                // .catch(error => {
                //     console.error("Payment Error:", error);
                // });
                 


                // fetch("http://127.0.0.1:8000/payment/pay/", {
                //     method: "GET",
                //     headers: {
                //         "Content-Type": "application/json"
                //     }
                // })
                // .then(response => {
                //     if (response.ok) {
                //         window.location.href = "http://127.0.0.1:8000/payment/pay/"; // Redirect to payment page
                //     } else {
                //         return response.json().then(
                //             err => { throw new Error(err.message); });
                //     }
                // })
                // .catch(error => {
                //     console.error("Payment Error:", error);
                //     alert("Failed to initiate payment. Please try again.");
                // });
            });
        });
  