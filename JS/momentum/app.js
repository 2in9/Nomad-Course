const player = {
    name: "LHS",
    age: 24,
    fat: true,
    habby: "game",
    hello(aaa, bbb){
        return aaa+bbb
    }
};
player.fat = false;
player.lastname = "hahaha"
player.age += 10;
console.log(player)
console.log(player.name)
console.log(player.hello(1, 2))