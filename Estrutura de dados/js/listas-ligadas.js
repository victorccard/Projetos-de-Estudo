function LinkedList() {
    var node = function(element) {
        this.element = element
        this.next = null
    }

    var lenght = 0
    var head = null
    
    this.append = function(element) {
        //adiciona um elemento no final da lista
        var node = new Node(element),
        current

        if(head === null) {
            head = node
        } else {
            current = head

            while(current.next) {
                current = current.next
            }

            current.next = node
        }
        lenght++
    }

    this.insert = function(position, element) {
        //insere um elemento em uma posição específica
    }

    this.removeAt = function(position) {
        //remove um elemento em uma posição específica
    }

    this.remove = function(element) {
        //remove o elemento 'element'
    }

    this.indexOf = function(element) {
        //retorna a posição do e
    }

    this.isEmpty = function() {
        //retorna se a lista está vazia
    }

    this.size = function() {
        //retorna o tamanho da lista
    }

    this.toString = function() {
        //converte em string
        var current = head,
        string = ''

        while(current) {
            string+= current.element + ' '
            current = current.next
        }

        return string
    }

    this.print = function() {
        //mostra no console
        console.log(this.toString)
    }
}

