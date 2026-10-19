from __future__ import annotations

from pathlib import Path
import re

root = Path(".")

NEW_BUTTON = (
    '                <button type="button" id="mobileMenuButton" '
    'class="lg:hidden flex h-10 w-10 shrink-0 items-center justify-center rounded-full text-gray-800 '
    'transition-colors hover:bg-gray-100/90" aria-expanded="false" aria-controls="mobileMenuPanel" '
    'aria-label="Abrir menú de navegación">\n'
    '                    <i id="mobileMenuButtonIcon" class="ti ti-menu-2 text-2xl" aria-hidden="true"></i>\n'
    "                </button>"
)

NEW_PANEL = """    <!-- Mobile Menu fuera del nav: fixed debe anclar al viewport -->
    <div id="mobileMenuPanel" class="fixed bottom-0 left-0 right-0 z-[100] hidden overflow-hidden px-3 pb-[max(0.75rem,env(safe-area-inset-bottom,0px))] lg:hidden" style="top: var(--mobile-nav-top, 5.5rem);" aria-hidden="true">
        <div class="mobile-menu-sheet flex min-h-0 flex-col overflow-hidden rounded-2xl border border-gray-200/90 bg-white shadow-[0_12px_48px_rgba(0,0,0,0.12)] ring-1 ring-black/5">
            <nav class="mobile-menu-scroll overscroll-y-contain pt-1 [scrollbar-gutter:stable]">
                <a href="el_instituto.html" class="block border-b border-gray-200 px-4 py-4 text-base font-semibold text-gray-900 active:bg-gray-50">La Academia</a>
                <details class="mobile-nav-details border-b border-gray-200">
                    <summary class="flex cursor-pointer list-none items-center justify-between px-4 py-4 text-base font-semibold text-gray-900 [&::-webkit-details-marker]:hidden">
                        <span>Negocios y Finanzas</span>
                        <i class="ti ti-chevron-down mobile-nav-chevron text-xl text-gray-500 transition-transform duration-200" aria-hidden="true"></i>
                    </summary>
                    <div class="border-t border-gray-100 bg-gray-50/70">
                        <a href="economia_digital.html" class="block border-b border-gray-100 px-4 py-3.5 pl-5 text-[0.9375rem] font-medium text-gray-800 active:bg-white">Economía Digital</a>
                        <a href="digital_empower.html" class="block border-b border-gray-100 px-4 py-3.5 pl-5 text-[0.9375rem] font-medium text-gray-800 active:bg-white">Digital Empower</a>
                        <a href="edufintech.html" class="block border-b border-gray-100 px-4 py-3.5 pl-5 text-[0.9375rem] font-medium text-gray-800 active:bg-white">Edufintech</a>
                        <a href="economia_digital.html" class="block px-4 py-3.5 pl-5 text-[0.9375rem] font-medium text-gray-800 active:bg-white">Mercados Financieros</a>
                    </div>
                </details>
                <a href="blog_t.html" class="block border-b border-gray-200 px-4 py-4 text-base font-semibold text-gray-900 active:bg-gray-50">Biblioteca</a>
            </nav>
            <div id="mobileMenuFooter" class="shrink-0 border-t border-gray-200 bg-white p-4 pb-[max(1rem,env(safe-area-inset-bottom,0px))]">
                <a href="iniciar_estudios.html" class="flex w-full items-center justify-center rounded-xl bg-gray-900 py-4 text-center text-base font-semibold text-white shadow-sm transition-colors hover:bg-gray-800">Consulta</a>
            </div>
        </div>
    </div>
"""

CSS_BLOCK = """
        /* Menú móvil: despliegue desde el header (estilo panel full-width) */
        #mobileMenuPanel {
            --mobile-nav-top: 5.5rem;
            --mobile-nav-max-h: calc(100dvh - var(--mobile-nav-top) - 0.75rem - env(safe-area-inset-bottom, 0px));
            --mobile-nav-footer-h: 88px;
        }
        #mobileMenuPanel .mobile-menu-sheet {
            transform: translateY(-100%);
            transition: transform 0.3s cubic-bezier(0.32, 0.72, 0, 1);
            will-change: transform;
            max-height: var(--mobile-nav-max-h);
            height: fit-content;
        }
        #mobileMenuPanel .mobile-menu-scroll {
            max-height: calc(var(--mobile-nav-max-h) - var(--mobile-nav-footer-h));
            overflow-y: auto;
        }
        #mobileMenuPanel.is-open .mobile-menu-sheet {
            transform: translateY(0);
        }
        details.mobile-nav-details[open] .mobile-nav-chevron {
            transform: rotate(180deg);
        }
"""

JS_BLOCK = r"""
<script>
  document.addEventListener('DOMContentLoaded', function () {
    var openBtn = document.getElementById('mobileMenuButton');
    var menuIcon = document.getElementById('mobileMenuButtonIcon');
    var panel = document.getElementById('mobileMenuPanel');
    var header = document.getElementById('siteHeader');
    var sheet = panel && panel.querySelector('.mobile-menu-sheet');
    var closeTimer;
    var sheetTransitionEnd = function (e) {
      if (!panel || e.propertyName !== 'transform') return;
      window.clearTimeout(closeTimer);
      if (sheet) sheet.removeEventListener('transitionend', sheetTransitionEnd);
      panel.classList.add('hidden');
    };

    function syncMenuButtonIcon(open) {
      if (!menuIcon || !openBtn) return;
      if (open) {
        menuIcon.className = 'ti ti-x text-2xl';
        openBtn.setAttribute('aria-label', 'Cerrar menú');
      } else {
        menuIcon.className = 'ti ti-menu-2 text-2xl';
        openBtn.setAttribute('aria-label', 'Abrir menú de navegación');
      }
    }

    function updateMobileNavMetrics() {
      if (!panel || !header) return;
      var top = Math.max(0, header.getBoundingClientRect().bottom);
      panel.style.setProperty('--mobile-nav-top', top + 'px');

      var available = window.innerHeight - top - 12;
      panel.style.setProperty('--mobile-nav-max-h', Math.max(240, available) + 'px');

      var footer = document.getElementById('mobileMenuFooter');
      if (footer) {
        panel.style.setProperty('--mobile-nav-footer-h', Math.max(0, footer.getBoundingClientRect().height) + 'px');
      }
    }

    function setMenuOpen(open) {
      if (!panel || !openBtn) return;
      window.clearTimeout(closeTimer);
      if (sheet) sheet.removeEventListener('transitionend', sheetTransitionEnd);
      if (open) {
        updateMobileNavMetrics();
        panel.classList.remove('hidden');
        panel.offsetHeight;
        requestAnimationFrame(function () {
          panel.classList.add('is-open');
          updateMobileNavMetrics();
        });
        openBtn.setAttribute('aria-expanded', 'true');
        panel.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        syncMenuButtonIcon(true);
      } else {
        if (panel.classList.contains('hidden')) return;
        panel.classList.remove('is-open');
        openBtn.setAttribute('aria-expanded', 'false');
        panel.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        syncMenuButtonIcon(false);
        function sealClosed() {
          window.clearTimeout(closeTimer);
          if (sheet) sheet.removeEventListener('transitionend', sheetTransitionEnd);
          panel.classList.add('hidden');
        }
        if (sheet) {
          sheet.addEventListener('transitionend', sheetTransitionEnd);
          closeTimer = window.setTimeout(sealClosed, 350);
        } else {
          sealClosed();
        }
      }
    }

    function toggleMenu() {
      if (!panel || panel.classList.contains('hidden') || !panel.classList.contains('is-open')) setMenuOpen(true);
      else setMenuOpen(false);
    }

    if (openBtn) {
      openBtn.addEventListener('click', function (e) {
        e.stopPropagation();
        toggleMenu();
      });
    }
    panel && panel.querySelectorAll('a[href]').forEach(function (link) {
      link.addEventListener('click', function () { setMenuOpen(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel && !panel.classList.contains('hidden')) setMenuOpen(false);
    });
    window.addEventListener('resize', function () {
      if (panel && !panel.classList.contains('hidden')) updateMobileNavMetrics();
    });
    window.addEventListener('orientationchange', function () {
      window.setTimeout(updateMobileNavMetrics, 200);
    });
  });
</script>
"""


def ensure_header_id_siteheader(text: str) -> str:
    if 'id="siteHeader"' in text:
        return text
    # add id to the first <header ...> tag
    return re.sub(r"<header(?![^>]*\bid=)([^>]*)>", r'<header id="siteHeader"\1>', text, count=1)


def ensure_css_block(text: str) -> str:
    if "Menú móvil: despliegue desde el header" in text:
        return text
    # insert before the last </style> in head
    return re.sub(r"</style>", CSS_BLOCK + "\n    </style>", text, count=1)


def replace_mobile_button(text: str) -> str:
    # replace any existing mobileMenuButton button with new one
    return re.sub(
        r'<!--\s*Mobile Menu Button\s*-->[\s\S]*?<button[^>]*\bid="mobileMenuButton"[\s\S]*?</button>',
        "<!-- Mobile Menu Button -->\n" + NEW_BUTTON,
        text,
        count=1,
    )


def remove_existing_mobile_panel(text: str) -> str:
    # remove any existing mobileMenuPanel block (usually inside nav)
    text = re.sub(r'<!--\s*Mobile Menu Panel\s*-->[\s\S]*?<div[^>]*\bid="mobileMenuPanel"[\s\S]*?</div>\s*</div>', "", text, count=1)
    text = re.sub(r'<div[^>]*\bid="mobileMenuPanel"[\s\S]*?</div>', "", text, count=1)
    return text


def insert_panel_after_header(text: str) -> str:
    if 'id="mobileMenuPanel"' in text and "<!-- Mobile Menu fuera del nav" in text:
        return text
    return text.replace("</header>", "</header>\n\n" + NEW_PANEL, 1)


def ensure_js_block(text: str) -> str:
    if "mobileMenuButtonIcon" in text and "updateMobileNavMetrics" in text:
        return text
    return text.replace("</body>", JS_BLOCK + "\n</body>", 1)


modified: list[str] = []
for path in sorted(root.glob("*.html")):
    text = path.read_text(encoding="utf-8")

    if 'id="mobileMenuButton"' not in text and "Mobile Menu Button" not in text:
        # no mobile menu in this file
        continue

    new_text = text
    new_text = ensure_header_id_siteheader(new_text)
    new_text = ensure_css_block(new_text)
    new_text = replace_mobile_button(new_text)
    new_text = remove_existing_mobile_panel(new_text)
    new_text = insert_panel_after_header(new_text)
    new_text = ensure_js_block(new_text)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        modified.append(path.name)

print("Modified files:")
for name in modified:
    print("-", name)
