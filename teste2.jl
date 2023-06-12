species Human is mammal
species Shark is fish
species Dog is mammal
species Sparrow is bird
species Lion is mammal

function checkSpecies (anim1, anim2) {
    if (anim1 == anim2) {
        !("They are the same species")
    } else {
        !("They are not the same species")
    }
}

checkSpecies(Human, Shark)
checkSpecies(Human, Lion)
checkSpecies(Human, Dog)
checkSpecies(Human, Sparrow)
checkSpecies(Dog, Sparrow)
checkSpecies(Dog, Lion)
checkSpecies(Sparrow, Shark)
checkSpecies(Sparrow, Lion)
checkSpecies(Lion, Shark)
