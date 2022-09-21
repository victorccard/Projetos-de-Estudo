/* function Stack() {
    var items = []

    this.push = function(element) {
        items.push(element) //adiciona um novo item à pilha
    }

    this.pop = function() {
        return items.pop() //remove o item do topo da pilha
    }
    
    this.peek = function() {
        return items[items.length - 1] //devolve o elemento que está no topo da pilha
    }

    this.isEmpty = function() {
        return items.length === 0 //informa se a pilha está vazia ou não
    }

    this.clear = function() {
        items = [] //limpa a pilha
    }

    this.size = function() {
        return items.length //informa o tamanho da pilha
    }

    this.print = function() {
        console.log(items.toString()) //imprime a pilha no console
    }
}

var pilha = new Stack()

pilha.push(2) 
pilha.push(4) 
pilha.push(6) 
pilha.push(8) 
pilha.push(10)

pilha.print()

console.log(pilha.isEmpty())
 */

"Exemplo Conversor Decimal para binário"

function dec2Bin(decNumber) {
    var restStack = [],
    rest,
    binaryString = ''

    while(decNumber > 0) {
        rest = Math.floor(decNumber % 2)
        restStack.push(rest)
        decNumber = Math.floor(decNumber / 2)   
    }

    while(restStack.length > 0) {
        binaryString += restStack.pop().toString()
    }

    return binaryString
}

console.log(dec2Bin(3))


