define(["knockout", "cast"], function (ko, Cast) {

	/**
	 * Knockout model of this app
	 * @see http://knockoutjs.com/
	 * @constructor
	 */
	var Model = function () {
		this.name = ko.observable(this.DEFAULT_NAME);
		this.history = ko.observableArray([]);
		this.selectType = this.types[this.DEFAULT_TYPE];
		this.repetition = 1;
		this.note = "";
	}

	/**
	 * @returns {cast}
	 */
	Model.prototype.cast = function() {
		var cast = new Cast(this.selectType, this.repetition, this.note);
		this.history.push(cast);
		return cast;
	}

	/**
	 * Loads history of casts from html5 local storage.
	 * Delete actual history.
	 */
	Model.prototype.load = function() {
		var data = localStorage.getItem(this.name());
		var object = ko.utils.parseJson(data);
		this.history.removeAll();
		for(var key in object) {
			var cast = new Cast();
			cast.sum = object[key].sum;
			cast.results = object[key].results;
			cast.note = object[key].note;
			cast.type = object[key].type;
			this.history.push(cast);
		}
	}

	/**
	 * Save to html5 local storage.
	 * Key is this.name()
	 */
	Model.prototype.save = function() {
		localStorage.setItem(this.name(), ko.toJSON(this.history()));
	}

	/**
	 * Constants
	 */
	Model.prototype.types = [4, 6, 12, 20];
	Model.prototype.DEFAULT_TYPE = 1;
	Model.prototype.DEFAULT_NAME = "Anonymous";

	return Model;
});