function map(){
    var tags = this.entities;

    for(var i=0; i<tags.length; i++) {
        emit(tags[i],{count:1, lower:tags[i].toLowerCase()})
    }

}