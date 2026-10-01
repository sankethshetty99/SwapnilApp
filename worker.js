// swapnil.sankethshetty.me — Swapnil's T-Mobile share breakdown. Public page, no login.
// PAGE is injected at deploy time from page.html + data.json (see inject.py).
const PAGE = __PAGE_HTML__;

export default {
  async fetch(request) {
    const url = new URL(request.url);
    if (url.pathname === "/" || url.pathname === "/index.html") {
      return new Response(PAGE, {
        headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" },
      });
    }
    return new Response("not found", { status: 404 });
  },
};
