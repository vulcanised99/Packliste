// Service Worker: Offline-Betrieb. Zeigt sofort die gespeicherte Version und holt im Hintergrund die neue.
// Bei grösseren Änderungen an der App: VERSION erhöhen.
const VERSION = "packliste-v5";
const FILES = ["./", "index.html", "data.json", "manifest.webmanifest", "app-icon-192.png", "app-icon-512.png", "app-icon-180.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(caches.open(VERSION).then(async cache => {
    const cached = await cache.match(e.request, {ignoreSearch: true});
    const net = fetch(e.request).then(r => { if (r.ok) cache.put(e.request, r.clone()); return r; }).catch(() => cached);
    return cached || net;
  }));
});
