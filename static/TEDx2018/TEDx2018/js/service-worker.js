var CACHE_NAME = 'static-cache';
var urlsToCache = [
	'../../../.',
	'../../../developmentTestbench/.',
	'../../../static/TEDx2018/css/animate.min.css',
	'../../../static/TEDx2018/css/fontello.css',
	'../../../static/TEDx2018/css/style.css',
	'../../../static/TEDx2018/font/fontello.woff2',
	'../../../static/TEDx2018/images/TEDxLogoBlack.svg',
	'../../../static/TEDx2018/js/service-worker.js',
	'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
	'https://code.jquery.com/jquery-3.2.1.slim.min.js',
	'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
	'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js',
	'https://fonts.googleapis.com/css?family=Open+Sans:300,400,700&amp;subset=greek'
];

self.addEventListener('install', function (event) {
	event.waitUntil(
		caches.open(CACHE_NAME)
			.then(function (cache) {
				return cache.addAll(urlsToCache);
			})
	);
});

self.addEventListener('fetch', function (event) {
	event.respondWith(
		caches.match(event.request)
			.then(function (response) {
				return response || fetchAndCache(event.request);
			})
	);
});

function fetchAndCache(url) {
	return fetch(url).then(
		function (response) {
			// Check if we received a valid response
			if (!response.ok) {
				throw Error(response.statusText);
			}
			return caches.open(CACHE_NAME).then(
				function (cache) {
					cache.put(url, response.clone());
					return response;
				}
			);
		}
	).catch(
		function (error) {
			console.log('Request failed:', error);
			// You could return a custom offline 404 page here
		}
	);
}