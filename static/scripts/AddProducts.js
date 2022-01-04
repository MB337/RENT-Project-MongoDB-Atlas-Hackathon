var category,
  prodName,
  desc,
  price,
  isHomepage,
  isHomepageCarousel,
  image,
  isCategoryCarousel;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

window.onload = function () {
  var submit = document.getElementById("submit");
  submit.onclick = function () {
    category = document.getElementById("category").value;
    prodName = document.getElementById("prodName").value;
    desc = document.getElementById("desc").value;
    price = parseFloat(document.getElementById("price").value);
    isHomepage = document.getElementById("isHomepage").checked;
    isHomepageCarousel = document.getElementById("isHomepageCarousel").checked;
    isCategoryCarousel = document.getElementById("isCategoryCarousel").checked;
    image = document.getElementById("img-url").value;

    if (
      category != "" &&
      prodName != "" &&
      desc != "" &&
      price != "" &&
      image != ""
    ) {
      var prodDict = {
        category: category,
        prodName: prodName,
        desc: desc,
        price: price,
        isHomepage: isHomepage,
        isHomepageCarousel: isHomepageCarousel,
        isCategoryCarousel: isCategoryCarousel,
        image: image,
        watch: 0,
      };
      
      axios
        .post("/api/add-product", prodDict)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      
      async function sleep(){await sleep(2000);}
      sleep()
      
      }else {
      alert("You have to complete all fields!");
    }

    console.log(
      category,
      prodName,
      desc,
      price,
      isHomepage,
      isHomepageCarousel,
      isCategoryCarousel
    );
    window.location.href = "/"
  };
};

function validate(evt) {
  var theEvent = evt || window.event;

  // Handle paste
  if (theEvent.type === "paste") {
    key = event.clipboardData.getData("text/plain");
  } else {
    // Handle key press
    var key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode(key);
  }
  var regex = /[0-9]|\./;
  if (!regex.test(key)) {
    theEvent.returnValue = false;
    if (theEvent.preventDefault) theEvent.preventDefault();
  }
}

