const CACHE_NAME = 'biocazadores-cache-v2';
const urlsToCache = [
  '/',                        // Página principal 
  '/dashboard/',              // Ruta del dashboard
  '/register/',               // Ruta del registro
  '/static/css/styles.css',   // Estilos
  '/static/js/main.js',       // Script principal
  '/static/assets/logo.png',  // Imagen
  '/manifest.json',          // Manifest PWA
  'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap'
];

// Instalación
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log(' Archivos en caché:', urlsToCache);
        return cache.addAll(urlsToCache);
      })
  );
});

// Activación
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            console.log(' Eliminando caché vieja:', cache);
            return caches.delete(cache);
          }
        })
      );
    })
  );
  console.log(' Service Worker activado y actualizado');
});

// Interceptar requests
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});

