define([], function () {

	/**
	 * Represents one cast with dice
	 * @param {int} type
	 * @param {int} repetition
	 * @param {string} note
	 * @class
	 * @constructor
	 */
	var	Cast = function(type, repetition, note) {
		this.sum = 0;
		this.results = [];
		this.note = note || "";
		this.type = type;

		for (var i = 0; i < repetition; i++) {
			var r = Math.floor(Math.random() * this.type) + 1;
			this.sum += r;
			this.results.push(r);
		}
	}

	/**
	 * @returns {string}
	 */
	Cast.prototype.toString = function() {
		return "Type: " + this.type +
			", Sum: " + this.sum +
			", Casts: " + this.results.join() +
			", Note: " + this.note ;
	}

    return Cast;
});