window.addEventListener("DOMContentLoaded", ()=>{
    const tiles = Array.from(document.querySelectorAll('.title'))
    const playerDisplay = document.querySelector('.display-player')
    const resetButton = document.querySelector('#reset')
    const announcer = document.querySelector('.announcer')

    let board = ['', '', '', '', '', '', '', '', '']
    let currentPlayer = 'X';
    let isGameActive = true;

    const PlayerX_WON = 'PlayerX_Won'
    const PlayerO_WON = 'PlayerO_Won'
    const TIE = 'TIE'

    const winningCondition = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    function handleResultValidation(){
        let roundWon = false
        for (let i = 0; i <= 7; i ++){
            const winCondition = winningCondition[i]
            const a = board[winCondition[0]]
            const b = board[winCondition[1]]
            const c = board[winCondition[2]]
            console.log(board)
            if (a === '' || b === '' || c == ''){
                continue;
            }
            if (a == b && b == c){
                roundWon = true
                console.log("Hi")
                break
            }
            // console.log(a)
            // console.log(b)
            // console.log(c)
        }
        if (roundWon){
            announce(currentPlayer === 'X' ? PlayerX_WON : PlayerO_WON)
            isGameActive = false
            return
        }
        if (!board.includes('')){
            announce(TIE)
        }
    }

    const announce = (type) => {
        switch (type) {
            case PlayerO_WON:
                announcer.innerHTML = 'Player <span class = "playerO">O</span> WON'
                break
            case PlayerX_WON:
                announcer.innerHTML = 'Player <span class = "playerX">X</span> WON'
                break;
            case TIE:
                announcer.innerText = 'TIE'
                break
        }
        announcer.classList.remove('hide')
    }

    const isValidAction = (tile) => {
        if (tile.innerText === 'X' || tile.innerText === 'O'){
            return false
        }
        return true
    }

    const updateBoard = (index) => {
        board[index] = currentPlayer;
    }
    
    const changePlayer = () => {
        playerDisplay.classList.remove(`player${currentPlayer}`)
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X'
        playerDisplay.innerText = currentPlayer
        playerDisplay.classList.add(`player${currentPlayer}`)
    }

    const userAction = (tile, index) => {
        if (isValidAction(tile) && isGameActive){
            tile.innerText = currentPlayer
            tile.classList.add(`player${currentPlayer}`)
            updateBoard(index)
            handleResultValidation()
            changePlayer()
        }
    }

    const resetBoard = () => {
        board = ['', '', '', '', '', '', '', '', '']
        isGameActive = true
        announcer.classList.add("hide")

        if (currentPlayer === 'O'){
            changePlayer()
        }
        tiles.forEach(tile => {
            tile.innerText = ''
            tile.classList.remove('playerX')
            tile.classList.remove('playerO')
        })
    }

    tiles.forEach((tile, index) => {
        tile.addEventListener('click', () => userAction(tile, index))
    })

    resetButton.addEventListener('click', resetBoard);
})