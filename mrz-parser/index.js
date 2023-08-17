const parse = require('mrz').parse;

let mrz = ['PAISLAEVARSDOTTIR<<THURIDUR<OESP<<<<<<<<<<<<', 'A3536444<7ISL1212123<3103108121212<1239<<<68'];

var result = parse(mrz);
console.log(result);