let canvas=document.getElementById("my_canvas");
let context=canvas.getcontext("2d");

const speed=4;
let position=0;
let moveSpeed=speed;
let radius=40;

function moveBall(){
    if(position+radius>640){
        movespeed=-speed;

    }else if(position-radius<0){
        moveSpeed=speed;
    }
    position+=moveSpeed;
}
function drawBall(){
    context.clearReact(0,0,640,480);
    context.fillStyle="#62687f";
    context.arc(position,50,radius,0,2*Math.PI);
}
function animate(){
    moveBall();
    drawBall();
    window.requestAnimationFrame(animate);
}
window.requestAnimationFrame(animate);