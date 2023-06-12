
species Dog is mammal
species Sparrow is bird

function bark(){
    !("WOOF WOOF!")
}

if (Dog == "mammal") {
    !("Dog is a mammal")
    bark()
} else {
    !("Dog is not a mammal")
}

if (Dog == Sparrow) {
    !("Dog and Sparrow are the same species")
} else {
    !("Dog and Sparrow are not the same species")
    !(Dog)
    !(Sparrow)
}
