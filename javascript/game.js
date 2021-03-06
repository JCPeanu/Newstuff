import { update as updateSnake, draw as drawSnake, SnakeSpeed } from './snake.js'
let lastRenderTime = 0

function main(currentTime){
    window.requestAnimationFrame(main)
    const secondsSinceLastRender = (currentTime - lastRenderTime) / 1000
    if (secondsSinceLastRender < 1 / SnakeSpeed) return

    console.log('Render')
    lastRenderTime = currentTime
    update()
    draw()
}
window.requestAnimationFrame(main)

function update(){
    updateSnake()
}
function draw(){
    drawSnake()
}