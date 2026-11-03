/* Visium Digital — Hero Motion · Web Animations API, sin dependencias */
(() => {
  const root = document.getElementById('vhStage'); if (!root) return;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !root.animate) { root.classList.add('vh-on'); return; }
  const q = s => root.querySelector(s), E = 'cubic-bezier(.65,0,.35,1)', T = 6200;
  // Estados [cx, cy, w, h, radio, rot, z] en unidades cqw (0–100 del escenario)
  const S = {
    card:{s:[20,24,15,15,3,-24,80], i:[50,55,24,24,3,0,0]},
    ring:{s:[80,20,9,9,99,0,120],  i:[50,25,13,13,99,0,20]},
    btn: {s:[22,80,11,11,3,30,-60],i:[31,69,12,12,2.5,12,0]},
    tog: {s:[84,74,18,18,99,0,40], i:[50,55,50,50,99,0,-30]},
    bars:{s:[50,10,10,10,1.5,45,-120],i:[70,67,11,11,1.5,45,10]},
    chip:{s:[12,52,4,4,99,0,160],  i:[71,33,5,5,99,0,40]}
  };
  const run = () => {
    const W = root.clientWidth, c = px => px / W * 100;
    root.querySelectorAll('.pc').forEach((el, n) => {
      const k = el.dataset.k, cs = getComputedStyle(el), w = c(el.offsetWidth), h = c(el.offsetHeight);
      const rr = cs.borderTopLeftRadius, r = rr.endsWith('%') ? parseFloat(rr) / 100 * Math.min(w, h) : c(parseFloat(rr));
      const f = { l: c(el.offsetLeft), t: c(el.offsetTop) };
      const fin = [f.l + w / 2, f.t + h / 2, w, h, r, 0, 0], st = S[k];
      const fr = (a, o, ex = {}) => ({ offset: o, easing: E, opacity: 1,
        transform: `translate3d(${a[0]-f.l-a[2]/2}cqw,${a[1]-f.t-a[3]/2}cqw,${a[6]}px) rotate(${a[5]}deg)`,
        width: a[2] + 'cqw', height: a[3] + 'cqw', borderRadius: a[4] + 'cqw', ...ex });
      const s2 = st.s.map((v, j) => j === 0 ? v + 2.5 : j === 1 ? v - 3 : j === 5 ? v + 10 : v);
      const d = n * 90, o = { duration: T, delay: d, fill: 'both' };
      el.animate([fr(st.s, 0, { opacity: 0 }), fr(st.s, .10, { easing: 'ease-in-out' }), fr(s2, .27), fr(st.i, .50, { easing: 'linear' }),
        fr(st.i, .57), fr(fin, .84, { easing: 'linear' }), fr(fin, 1)], o);
      el.querySelector('.sh').animate([{ opacity: 0, offset: 0 }, { opacity: 1, offset: .10 }, { opacity: 1, offset: .62 }, { opacity: 0, offset: .76 }, { opacity: 0, offset: 1 }], o);
      el.querySelector('.ui').animate([{ opacity: 0, offset: 0 }, { opacity: 0, offset: .70 }, { opacity: 1, offset: .86 }, { opacity: 1, offset: 1 }], o);
    });
    // Selección tipo Figma: envuelve la "idea", luego la composición final
    const G = (a, o, op, e = E) => ({ offset: o, easing: e, opacity: op, left: a[0] + 'cqw', top: a[1] + 'cqw', width: a[2] + 'cqw', height: a[3] + 'cqw' });
    q('.sel').animate([G([16,16,68,68], .30, 0), G([16,16,68,68], .38, 1), G([25,28,50,54], .52, 1, 'linear'), G([25,28,50,54], .57, 1),
      G([9,8,82,78], .84, 1, 'linear'), G([9,8,82,78], .93, 1, 'ease-out'), G([9,8,82,78], 1, 0)], { duration: T, fill: 'both' });
    // Cierre: cursor entra y pulsa el botón
    q('.cur').animate([{ opacity: 0, transform: 'translate(22cqw,-14cqw)' }, { opacity: 1, transform: 'translate(0,0)', offset: .6 }, { opacity: 1, transform: 'translate(0,0)' }],
      { duration: 1500, delay: 4700, easing: 'cubic-bezier(.22,1,.36,1)', fill: 'both' });
    const press = (sel, delay, to) => q(sel + ' .ui').animate([{ transform: 'scale(1)' }, { transform: `scale(${to})` }, { transform: 'scale(1)' }], { duration: 380, delay, easing: 'ease-in-out' });
    press('.c-btn', 5650, .93); press('.c-chip', 5850, 1.22);
    root.classList.add('vh-on');
  };
  const start = () => (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(run);
  'IntersectionObserver' in window
    ? new IntersectionObserver((e, io) => { if (e[0].isIntersecting) { io.disconnect(); start(); } }, { threshold: .3 }).observe(root)
    : start();
  // Parallax por capas (solo puntero fino)
  if (matchMedia('(pointer:fine)').matches) {
    let raf; addEventListener('pointermove', e => { cancelAnimationFrame(raf); raf = requestAnimationFrame(() => {
      root.style.setProperty('--mx', (e.clientX / innerWidth - .5) * 2); root.style.setProperty('--my', (e.clientY / innerHeight - .5) * 2); }); }, { passive: true });
  }
})();
