let calculator = {
    read() {
        this.a = +prompt('Value of a?', '');
        this.b = +prompt('Value of b?', '');
    },

    sum() {
        return this.a + this.b;
    },

    mul() {
        return this.a * this.b;
    }
};

calculator.read();
alert( calculator.sum() );
alert( calculator.mul() );