class Photo {
    
    constructor () {   
        this._index = parseInt(localStorage.getItem(collection+'page') || 0)
        this._index = this._index >= images.length ? images.length -1 : this._index
        this.setPhoto().setCaption().setCounter()
        var p = this             
        $('#iv_previous').click(function () {
            p.previous.setPhoto().setCaption().setCounter()
        })
        $('#iv_next').click(function () {
            p.next.setPhoto().setCaption().setCounter()
        })
        

        document.addEventListener("keydown", function (e) {
            if (e.keyCode == 39 && p.index < images.length-1) {
                p.next.setPhoto().setCaption().setCounter()
            } else if (e.keyCode == 37 && p.index > 0) {
                p.previous.setPhoto().setCaption().setCounter()
            }
        })
    }
    
    get index() {
        return this._index
    }
            
    get photo() {
        return images[this._index]
    }
    
    get next() {
        this._index = ( this._index < images.length ? this._index + 1 : this._index-1 )
        return this
    }
    
    get previous() {
        this._index = ( this._index > 0 ? this._index - 1 : 0 )
        return this           
    }
    
    goPhoto(i) {
        var ni = parseInt(i)
        if (!isNaN(parseInt(ni))) {
            this._index = (ni < 0 ? 0 : ni)
            this._index = (ni >= images.length ? images.length - 1 : ni)
        }
        return this
    }
    
    setCaption() {
        var cap = captions[this._index]
        var html = ''
        if (cap.length > 0) {                
            for (var i=0;i<cap.length;i++) {
                var c = cap[i].startsWith('-') ? 'talk' : 'cap'
                var cp = this.format(cap[i])
                html += `<p id="${c}">${cp}</p>\n`
            }
        }
        $('#iv_caption').html(html)
        return this        
    }
    
    setCounter () {
        $('#iv_counter').html(`${this._index + 1} of ${images.length}`)
    }
    
    setPhoto() {
        localStorage.setItem(collection+'page', this._index)
        $('#iv_photo').attr('src', this.photo)
        return this
    }
    
    format (str) {
        var r = str.replace(/^-/,'')
            r = r.replace(/[^/]\(/g, ' "')
            r = r.replace(/([^/])\)/g, '$1"')
            r = r.replace(/\//g,'')
            r = r.replace(/_(.*)_/g, '<span id="emph">$1</span>')
            r = r.replace(/\*(.*)\*/, '<span id="shout">$1</span>')
        return r
    }
}


