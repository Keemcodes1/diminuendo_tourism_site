// Assign all elements
const demoId = document.getElementById('demo');
const demoClass = document.getElementsByClassName('demo');
const demoTag = document.getElementsByTagName('article');
const demoQuery = document.querySelector('#demo-query');
const demoQueryAll = document.querySelectorAll('.demo-query-all');

// Change border of ID demo to purple
demoId.style.border = '1px solid purple';

// Change border of class demo to orange
for (i = 0; i < demoClass.length; i++) {
  demoClass[i].style.border = '1px solid orange';
}

// Change border of tag demo to blue
for (i = 0; i < demoTag.length; i++) {
  demoTag[i].style.border = '1px solid blue';
}

// Change border of ID demo-query to red
demoQuery.style.border = '1px solid red';

// Change border of class query-all to green
demoQueryAll.forEach(query => {
  query.style.border = '1px solid green';
});
document.getElementById("myForm").addEventListener("submit",function(event){
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var cpassword = document.getElementById("cpassword").value;
  var telephone = document.getElementById("telephone").value;
  //validation checks
  if(name ===""){
      alert("please enter your name.");
      event.preventDefault();//to prevent form submission to default
      return;
  }
  if(email ===""){
      alert("please enter your email.");
      event.preventDefault();//to prevent form submission to default
      return;
  }
  if(password ===""){
      alert("please enter your password.");
      event.preventDefault();//to prevent form submission to default
      return;
  }
  if(cpassword !=="password"){
      alert("please enter the correct password.");
      event.preventDefault();//to prevent form submission to default
      return;
  }
  if(telephone ===""){
      alert("please enter your telephone number.");
      event.preventDefault();//to prevent form submission to default
      return;
  }
})
