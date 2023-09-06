function play() {
  var wbutton = document.getElementById("wbutton");
  wbutton.play();
}
function play2() {
  var abutton = document.getElementById("abutton");
  abutton.play();
}
function play3() {
  var sbutton = document.getElementById("sbutton");
  sbutton.play();
}
function play4() {
  var dbutton = document.getElementById("dbutton");
  dbutton.play();
}
function play5() {
  var jbutton = document.getElementById("jbutton");
  jbutton.play();
}
function play6() {
  var kbutton = document.getElementById("kbutton");
  kbutton.play();
}
function play7() {
  var lbutton = document.getElementById("lbutton");
  lbutton.play();
}


function playSound(soundFile) {
  const audio = new Audio(soundFile);
  audio.play();
}