
  var i = 0;
  var txt = 'Ye is an American rapper, singer, songwriter, record producer, and fashion designer.Born in Atlanta and raised in Chicago, West gained recognition as a producer for Roc-A-Fella Records in the early 2000s, producing singles for several artists and developing the chipmunk soul sampling style.';
  var speed = 50;
  
  function typeWriter() {
    if (i < txt.length) {
      document.getElementById("info").innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
  };
  window.onload = function() {
    typeWriter();
    runZoom();
  };
  
function zoomin() {
    var pic = document.getElementById("pic");
    var width = pic.clientWidth;
    var height = pic.clientHeight;
    pic.style.width = width + 10 + "px";
    pic.style.height = height + 10 + "px";
  }
  
  function zoomout() {
    var pic = document.getElementById("pic");
    var width = pic.clientWidth;
    var height = pic.clientHeight;
    pic.style.width = width - 10 + "px";
    pic.style.height = height - 10 + "px";
  }
  
  function runZoom() {
    for (var i = 0; i < 10; i++) {
      setTimeout(zoomin, i * 1000);
    }
    for (var j = 0; j < 10; j++) {
      setTimeout(zoomout, 10000 + j * 1000);
    }
    setTimeout(runZoom, 20000);
  }
  const form = document.getElementById('review-form');
const tableBody = document.querySelector('#reviews-table tbody');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const name = event.target.elements.name.value;
  const rating = event.target.elements.rating.value;
  const review = event.target.elements.review.value;

  const row = document.createElement('tr');
  const nameCell = document.createElement('td');
  const ratingCell = document.createElement('td');
  const reviewCell = document.createElement('td');

  nameCell.textContent = name;
  ratingCell.textContent = rating;
  reviewCell.textContent = review;

  row.appendChild(nameCell);
  row.appendChild(ratingCell);
  row.appendChild(reviewCell);

  tableBody.appendChild(row);

  event.target.reset();
});

  
  
  runZoom();




 


  