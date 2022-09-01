window.onload = function ()
{
const paymentForm = document.querySelector("#paymentForm");
paymentForm.addEventListener("submit", payWithPaystack, false);

fetch("/public_key")
.then(res => res.json())
.then(data => public_key = data)

function payWithPaystack(e) {
  e.preventDefault();
  let handler = PaystackPop.setup({
    key: public_key, // Replace with your public key
    email: document.getElementById("email").value,
    amount: document.getElementById("amount").value * 100,
    ref: ''+Math.floor((Math.random() * 1000000000) + 1), // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you
    // label: "Optional string that replaces customer email"
    onClose: function(){
      alert('Window closed.');
    },
    callback: function(response){
      let message = 'Payment complete! Reference: ' + response.reference;
      alert(message);
      $.ajax({
        url: '/verify_transaction?reference='+ response.reference,
        method: 'get',
        success: function (response) {
            console.log(response)
          // the transaction status is in response.data.status
        }
      });
    }
  });

  handler.openIframe();
}}