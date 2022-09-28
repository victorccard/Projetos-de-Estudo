/* function Queue() {
    var items = []

    this.enqueue = function(element) {
        items.push(element) //insere um elemento
    }

    this.dequeue = function() {
        return items.shift() // remove um elemento
    }

    this.front = function() {
        return items[0] //Returna o primeiro elemento
    }

    this.isEmpty = function() {
        return items.length === 0 //Esta vazio?
    } 
    
    this.size = function() {
        return items.length //tamanho da fila
    }

    this.print = function() {
        console.log(items.toString())//mostrar fila
    }
}

var fila = new Queue()

fila.enqueue('Carlos')
fila.enqueue('Ana')
fila.enqueue('Lucas')

fila.dequeue()
fila.front()

fila.print() */

function PriorityQueue() {
    var items = []

    function QueueElement(element, priority) {
        this.element = element
        this.priority = priority
    }

    this.enqueue = function(element, priority) {
        var queueElement = new QueueElement(element, priority)
        var added = false
        
        for(var i = 0; i < items.length; i++) {
            if(queueElement.priority < items[i].priority) {
                items.splice(i, 0, queueElement)
                added = true
                break
            }
        }
        if(!added) {
            items.push(queueElement)
        }
    }

    this.dequeue = function() {
        return items.shift()
    }

    this.print = function() {
        for(var i = 0; i < items.length; i++) {
            console.log(items[i].element + ' ' + items[i].priority)
        }
    }
}

var pqueue = new PriorityQueue()
pqueue.enqueue('Carlos', 2)
pqueue.enqueue('Ana', 1)
pqueue.enqueue('Lucas', 1)

pqueue.print()