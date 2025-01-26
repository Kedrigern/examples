/**
 * Configuration
 * Libraries are loaded from CDN.
 * You can add local fallback.
 */
require.config({
	paths: {
		knockout: [
			"http://cdnjs.cloudflare.com/ajax/libs/knockout/3.1.0/knockout-min",
			//If the CDN location fails, load from this location
			"./lib/knockout-min"
		],
		jquery: [
			'http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min'
		],
		undersore: [
			"http://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.6.0/underscore-min"
		]
	},
	shim : {
		underscore : {
			exports : "_"
		}
	}
});

/**
 * Init point
 */
require(["knockout", "model"], function (ko, Model) {
	viewModel = new Model();

	ko.applyBindings(viewModel);

	knockout = ko;  // for direct access to the knockout
});