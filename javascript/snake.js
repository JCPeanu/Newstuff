export const SnakeSpeed = 1
const snakeBody = [{x : 11, y : 11}]


export function update(){
    console.log('update Snake')
}
export function draw(){
    snakeBody.forEach(segment =>{
        const snakeElement = document.createElement('div') 
        snakeElement.style.gridRowStart = segment.x
    })
}
