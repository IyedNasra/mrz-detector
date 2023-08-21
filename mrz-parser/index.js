
const parse = require('mrz').parse;

let mrz = ['P<GBRTHATCHER<<ROSS<<<<<<<<<<<<<<<<<<<<<<<<<', '2841464979TUN4904265M1601013<<<<<<<<<<<<<<04'];

var result = parse(mrz);
console.log(result);
