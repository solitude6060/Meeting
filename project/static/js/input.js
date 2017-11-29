$('.input-container input').blur(function(event) {
  var inputVal = this.value;
  
  if (inputVal) {
    this.classList.add('value-exists');
  } else {
    this.classList.remove('value-exists');
  }
});