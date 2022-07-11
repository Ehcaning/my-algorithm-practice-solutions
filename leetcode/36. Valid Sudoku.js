var isValidSudoku = function(board) {
    // check each column
    for(let i=0; i<9; i++){
        if(hasDuplicates([
            board[0][i], board[1][i], board[2][i],
            board[3][i], board[4][i], board[5][i],
            board[6][i], board[7][i], board[8][i]
        ])){
            return false;
        }
    }
    // check each row
    for(let i=0; i<9; i++){
        if(hasDuplicates(board[i])){
            return false;
        }
    }
    // check each 9
    for(let i=0; i<3; i++){
        for(let j=0; j<3; j++){
            let [ii,jj] = [i*3, j*3]
            if(hasDuplicates([
                board[0+ii][0+jj], board[1+ii][0+jj], board[2+ii][0+jj],
                board[0+ii][1+jj], board[1+ii][1+jj], board[2+ii][1+jj],
                board[0+ii][2+jj], board[1+ii][2+jj], board[2+ii][2+jj]
            ])){
                return false;
            }
        }
    }
    
    
    return true;
};

function hasDuplicates(array) {
    array = array.filter(el => el != '.')
    return (new Set(array)).size !== array.length;
}