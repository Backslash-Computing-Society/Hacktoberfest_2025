function printPattern() {
    const patternType = prompt("Which pattern do you want to print? Choose from: stars, numbers, characters, pyramid, diamond, triangle, hollow: ").toLowerCase();
    const rows = parseInt(prompt("Enter the number of rows for the pattern: "));

    if (isNaN(rows) || rows <= 0) {
        console.log("Invalid number of rows. Please enter a positive integer.");
        return;
    }

    switch (patternType) {
        case "stars":
            for (let i = 1; i <= rows; i++) {
                console.log("* ".repeat(i));
            }
            break;
        case "numbers":
            for (let i = 1; i <= rows; i++) {
                let row = "";
                for (let j = 1; j <= i; j++) {
                    row += j + " ";
                }
                console.log(row);
            }
            break;
        case "characters":
            for (let i = 0; i < rows; i++) {
                let row = "";
                for (let j = 0; j <= i; j++) {
                    row += String.fromCharCode(65 + j) + " "; 
                }
                console.log(row);
            }
            break;
        case "pyramid":
            for (let i = 1; i <= rows; i++) {
                let row = " ".repeat(rows - i);
                row += "* ".repeat(i);
                console.log(row);
            }
            break;
        case "diamond":
            // Upper part of the diamond
            for (let i = 1; i <= rows; i++) {
                let row = " ".repeat(rows - i);
                row += "* ".repeat(i);
                console.log(row);
            }
            // Lower part of the diamond
            for (let i = rows - 1; i >= 1; i--) {
                let row = " ".repeat(rows - i);
                row += "* ".repeat(i);
                console.log(row);
            }
            break;
        case "triangle": 
            for (let i = 1; i <= rows; i++) {
                console.log("* ".repeat(i));
            }
            break;
        case "hollow":
            for (let i = 1; i <= rows; i++) {
                let row = "";
                if (i === 1 || i === rows) {
                    row = "* ".repeat(rows);
                } else {
                    row = "* " + " ".repeat(2 * (rows - 2)) + "*";
                }
                console.log(row);
            }
            break;
        default:
            console.log("Invalid pattern type selected.");
    }
}

printPattern();
