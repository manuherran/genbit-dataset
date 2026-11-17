const I18N = {
  es: {nav_home:"Inicio",nav_dl:"Descargas",nav_model:"Modelo",nav_explore:"Tablas",nav_sql:"SQL en vivo",
    kicker:"Registro abierto · CSV + SQL · ES / EN",h1:'El dataset de <span class="g">Genbit</span>',
    lead:"Todo lo que hace Genbit queda registrado: tripulación, clientes de todo el sistema solar, proyectos de genética y física cuántica, productos, pedidos, pagos y devoluciones. Aquí tienes ese registro como base de datos relacional para aprender SQL, análisis de datos o machine learning.",
    cta_dl:"Descargar",cta_sql:"Probar SQL aquí",
    dl_title:"Descargas",dl_sub:"Los mismos datos en dos idiomas: cambian los nombres de tablas, columnas y los textos (Tierra / Earth, Entregado / Delivered…). Los identificadores numéricos coinciden.",
    dl_es:"Tablas t_cliente, t_pedido, t_planeta…",dl_en:"Tablas t_customer, t_order, t_planet…",dl_fmt_t:"Formatos",
    dl_fmt:"CSV en UTF-8 con cabecera y separador coma (NULL = celda vacía). Scripts para MySQL 8 / MariaDB y SQLite, y 15 consultas de ejemplo.",
    dl_browse:"Ver en GitHub ↗",model_title:"Modelo de datos",
    model_sub:"Relaciones 1-N y N-M (asignaciones, lista de materiales), una relación reflexiva (empleado → jefe), claves compuestas y NULLs a propósito para practicar LEFT JOIN.",
    explore_title:"Las tablas",explore_sub:"Elige una tabla para ver su descripción, sus columnas y todos sus datos.",
    sql_title:"SQL en vivo",sql_sub:"La base de datos completa se carga en tu navegador (SQLite en WebAssembly); nada sale de tu ordenador. Elige un ejemplo o escribe tu consulta. Ctrl+Enter para ejecutar.",
    run:"Ejecutar ▶",loading:"Cargando…",notice:"Genbit, su tripulación, sus clientes y sus empresas son ficticios. Todos los datos son sintéticos.",
    tables:"tablas",rows:"filas",langs:"idiomas",queries:"consultas de ejemplo",
    ms:(n,t)=>`${n} filas · ${t} ms`,noRows:"La consulta no devolvió filas.",ok:"Hecho.",custom:"— escribe tu propia consulta —"},
  en: {nav_home:"Home",nav_dl:"Downloads",nav_model:"Model",nav_explore:"Tables",nav_sql:"Live SQL",
    kicker:"Open log · CSV + SQL · ES / EN",h1:'The <span class="g">Genbit</span> dataset',
    lead:"Everything Genbit does gets logged: crew, customers from all over the solar system, genetics and quantum physics projects, products, orders, payments and refunds. Here is that log as a relational database to learn SQL, data analysis or machine learning.",
    cta_dl:"Download",cta_sql:"Try SQL here",
    dl_title:"Downloads",dl_sub:"Same data in two languages: table names, column names and text values change (Tierra / Earth, Entregado / Delivered…). Numeric ids match.",
    dl_es:"Tables t_cliente, t_pedido, t_planeta…",dl_en:"Tables t_customer, t_order, t_planet…",dl_fmt_t:"Formats",
    dl_fmt:"UTF-8 CSV with header row and comma separator (NULL = empty cell). Scripts for MySQL 8 / MariaDB and SQLite, plus 15 example queries.",
    dl_browse:"View on GitHub ↗",model_title:"Data model",
    model_sub:"1-N and N-M relationships (assignments, bill of materials), a self-reference (employee → manager), composite keys and deliberate NULLs to practise LEFT JOIN.",
    explore_title:"The tables",explore_sub:"Pick a table to see its description, columns and all of its data.",
    sql_title:"Live SQL",sql_sub:"The whole database is loaded in your browser (SQLite in WebAssembly); nothing leaves your computer. Pick an example or write your own query. Ctrl+Enter to run.",
    run:"Run ▶",loading:"Loading…",notice:"Genbit, its crew, customers and companies are fictional. All data is synthetic.",
    tables:"tables",rows:"rows",langs:"languages",queries:"example queries",
    ms:(n,t)=>`${n} rows · ${t} ms`,noRows:"The query returned no rows.",ok:"Done.",custom:"— write your own query —"}
};
const store = {get(k){try{return localStorage.getItem(k)}catch(e){return null}}, set(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
// El idioma lo fija la página: / (inglés) o /es/ (español). Los ficheros comunes
// (meta.js, db/, downloads/) están en la carpeta del inglés; BASE es la ruta hasta ella.
const lang = document.documentElement.lang === "es" ? "es" : "en";
const BASE = document.documentElement.dataset.base || "";
const dbs = {}; let SQL = null, currentTable = 0;
const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

// Estrellas (mismo fondo que genbit.com)
(function(){
  var c=$('stars'),x=c.getContext('2d'),s=[],W,H;
  var cols=['#ffffff','#22e4ff','#ff3dbb','#ffb627'];
  function size(){W=c.width=innerWidth;H=c.height=innerHeight;s=[];
    for(var i=0;i<Math.round(W*H/5000);i++)s.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.5+.2,d:Math.random()*.6+.1,c:Math.random()<.9?cols[0]:cols[1+Math.floor(Math.random()*3)],t:Math.random()*6});}
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function draw(ts){x.clearRect(0,0,W,H);var sc=scrollY;
    for(var i=0;i<s.length;i++){var p=s[i],yy=((p.y-sc*p.d*.3)%H+H)%H;
      x.globalAlpha=.5+.5*Math.sin(ts/900+p.t);x.fillStyle=p.c;x.beginPath();x.arc(p.x,yy,p.r,0,6.3);x.fill();}
    if(!reduce)requestAnimationFrame(draw);}
  addEventListener('resize',size);size();requestAnimationFrame(draw);
  addEventListener('scroll',function(){if(reduce)requestAnimationFrame(draw);});
})();

function table(cols, rows) {
  if (!rows.length) return `<p class="msg">${I18N[lang].noRows}</p>`;
  let h = '<table class="data"><thead><tr>' + cols.map(c => `<th>${esc(c)}</th>`).join("") + "</tr></thead><tbody>";
  for (const r of rows) h += "<tr>" + r.map(v => v === null ? '<td class="null">NULL</td>' :
    `<td${typeof v === "number" ? ' class="num"' : ""}>${esc(v)}</td>`).join("") + "</tr>";
  return h + "</tbody></table>";
}

function applyLang() {
  const t = I18N[lang], M = window.GENBIT_META[lang];
  document.querySelectorAll("[data-i18n]").forEach(el => el.textContent = t[el.dataset.i18n]);
  document.querySelectorAll("[data-i18n-html]").forEach(el => el.innerHTML = t[el.dataset.i18nHtml]);
  const total = M.tables.reduce((a, b) => a + b.rows, 0);
  $("stats").innerHTML = [[M.tables.length, t.tables], [total, t.rows], [2, t.langs], [M.queries.length, t.queries]]
    .map(([n, l]) => `<div class="stat"><b>${n.toLocaleString(lang)}</b><small>${l}</small></div>`).join("");
  $("tlist").innerHTML = M.tables.map((tb, i) => `<button data-i="${i}"><span>${tb.name}</span><small>${tb.rows}</small></button>`).join("");
  $("tlist").querySelectorAll("button").forEach(b => b.onclick = () => showTable(+b.dataset.i));
  $("qsel").innerHTML = M.queries.map((q, i) => `<option value="${i}">${esc(q.title)}</option>`).join("") + `<option value="-1">${t.custom}</option>`;
  $("qsel").value = 0; $("qtext").value = M.queries[0].sql;
  showTable(currentTable);
  renderER();
  if (dbs[lang]) runQuery();
}

function showTable(i) {
  currentTable = i;
  const tb = window.GENBIT_META[lang].tables[i];
  $("tlist").querySelectorAll("button").forEach(b => b.classList.toggle("on", +b.dataset.i === i));
  $("tdesc").textContent = tb.desc;
  $("tcols").innerHTML = tb.cols.map(c => `<span class="chip${c.pk ? " pk" : c.fk ? " fk" : ""}" title="${c.type}${c.null ? " NULL" : " NOT NULL"}">${c.pk ? "◆ " : ""}${c.name}${c.fk ? " → " + c.fk : ""}</span>`).join("");
  const db = dbs[lang];
  if (!db) return;
  const r = db.exec(`SELECT * FROM ${tb.name}`)[0];
  $("tdata").innerHTML = r ? table(r.columns, r.values) : table([], []);
}

let erSeq = 0;
async function renderER() {
  if (!window.mermaid) return;
  mermaid.initialize({startOnLoad: false, theme: "base", securityLevel: "strict", er: {useMaxWidth: true},
    themeVariables: {background: "#10142e", primaryColor: "#0b0e24", primaryBorderColor: "#22e4ff", primaryTextColor: "#e8ebff",
      lineColor: "#9aa3d6", secondaryColor: "#10142e", tertiaryColor: "#10142e", fontFamily: "JetBrains Mono, monospace", fontSize: "13px"}});
  try {
    const {svg} = await mermaid.render("er" + (++erSeq), window.GENBIT_META[lang].er);
    $("er").innerHTML = svg;
  } catch (e) { $("er").innerHTML = `<p class="msg">${esc(e.message || e)}</p>`; }
}

function runQuery() {
  const db = dbs[lang]; if (!db) return;
  const t0 = performance.now();
  try {
    const res = db.exec($("qtext").value);
    const ms = Math.round(performance.now() - t0);
    const last = res[res.length - 1];
    $("qout").innerHTML = last ? table(last.columns, last.values) : `<p class="msg">${I18N[lang].ok}</p>`;
    $("qmsg").className = "qmsg"; $("qmsg").textContent = I18N[lang].ms(last ? last.values.length : 0, ms);
  } catch (e) { $("qmsg").className = "qmsg err"; $("qmsg").textContent = e.message; $("qout").innerHTML = ""; }
}

async function loadDb(l) {
  if (dbs[l]) return dbs[l];
  const buf = await fetch(`${BASE}db/genbit_${l}.sqlite`).then(r => r.arrayBuffer());
  dbs[l] = new SQL.Database(new Uint8Array(buf));
  return dbs[l];
}

// Recordar la elección del visitante al cambiar de idioma (y conservar la sección).
const sw = document.querySelector(".lang");
if (sw) sw.addEventListener("click", () => { store.set("genbit-lang", sw.getAttribute("hreflang")); sw.href = sw.getAttribute("href").split("#")[0] + location.hash; });
$("qsel").onchange = () => { const i = +$("qsel").value; if (i >= 0) { $("qtext").value = window.GENBIT_META[lang].queries[i].sql; runQuery(); } };
$("run").onclick = runQuery;
$("qtext").addEventListener("keydown", e => { if ((e.ctrlKey || e.metaKey) && e.key === "Enter") { e.preventDefault(); runQuery(); } });

applyLang();
initSqlJs({locateFile: f => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.10.3/${f}`})
  .then(async S => { SQL = S; await loadDb(lang); showTable(currentTable); runQuery(); })
  .catch(e => { $("tdata").innerHTML = `<p class="msg">${esc(e.message || e)}</p>`; });
