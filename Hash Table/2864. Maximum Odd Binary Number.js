/**
 * @param {string} s
 * @return {string}
 */
var maximumOddBinaryNumber = function(s) {
    obj = { "0":0, "1":0 };

    for (let char of s) {
        if (char === "0") {
            obj["0"] += 1;
        } else {
            obj["1"] += 1
        }
    }

    let ones = obj["1"] - 1
    let zeros = obj["0"]

    res = ""

    for (let i = 0; i < ones; i++) {
        res += "1"
    }

    for (let i = 0; i < zeros; i++) {
        res += "0"
    }

    res += "1"

    return res

};
