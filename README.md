# GenBit Dataset

**🌐 Web: https://manuherran.github.io/genbit-dataset/** — explora las tablas y ejecuta SQL en el navegador.

[Español](#español) · [English](#english)

---

## Español

Una base de datos relacional de ejemplo para aprender y enseñar SQL, **que no es la aburrida de clientes y ventas**.

GenBit es un conglomerado científico del año 2188. Investiga genética, física cuántica y neurociencia; vende rayos congeladores, lanza piñas, llaveros de entrelazamiento y motores de curvatura; tiene oficinas en la Luna, Marte y Próxima b; y sus clientes incluyen humanos, cefalópodos de Europa y alguna nube consciente.

- **19 tablas** relacionadas, ~900 filas.
- **Español e inglés**: mismos datos e ids; cambian nombres de tablas/columnas y textos.
- **CSV** (UTF-8, coma, cabecera; NULL = celda vacía) y **SQL** para **MySQL 8 / MariaDB** y **SQLite**, más bases de datos `.sqlite` listas para usar.
- **15 consultas de ejemplo** por idioma (JOINs, agregados, subconsultas, funciones de ventana).
- Todos los datos son **ficticios**. Moneda: créditos galácticos (CG).

### Ficheros

| Ruta | Contenido |
|---|---|
| `data/es/*.csv`, `data/en/*.csv` | Una tabla por fichero CSV |
| `sql/genbit_es_mysql.sql`, `sql/genbit_en_mysql.sql` | Script completo MySQL / MariaDB (crea la BD `db_genbit_es` / `db_genbit_en`) |
| `sql/genbit_es_sqlite.sql`, `sql/genbit_en_sqlite.sql` | Script completo SQLite |
| `sql/queries_es.sql`, `sql/queries_en.sql` | Consultas de ejemplo |
| `docs/db/genbit_es.sqlite`, `docs/db/genbit_en.sqlite` | Bases de datos SQLite ya construidas |
| `generator/` | Script Python que genera todo (determinista) |

### Cargar los datos

```bash
mysql -u root -p < sql/genbit_es_mysql.sql
```

```bash
sqlite3 genbit.db < sql/genbit_es_sqlite.sql
```

```python
import pandas as pd
pedidos = pd.read_csv("data/es/t_pedido.csv")
```

### Tablas

| ES | EN | Qué es |
|---|---|---|
| t_planeta | t_planet | Planetas, lunas y estaciones |
| t_empresa | t_company | Empresas del grupo (con relación reflexiva a su matriz) |
| t_oficina | t_office | Oficinas y laboratorios |
| t_empleado | t_employee | Empleados (relación reflexiva empleado → jefe) |
| t_movil | t_mobile | Móviles de empresa (algunos sin asignar) |
| t_cliente | t_customer | Clientes de toda la galaxia |
| t_proveedor | t_supplier | Proveedores de piezas |
| t_inversor | t_investor | Inversores (algunos son empleados) |
| t_proyecto | t_project | Proyectos de investigación |
| t_asignacion | t_assignment | N-M empleados ↔ proyectos |
| t_paciente | t_patient | Pacientes de ensayos clínicos |
| t_suscriptor | t_subscriber | Suscriptores del boletín (sin FK: se cruzan por email) |
| t_linea_de_producto | t_product_line | Líneas de producto |
| t_producto | t_product | Productos |
| t_pieza | t_piece | Piezas y componentes |
| t_producto_pieza | t_product_piece | Lista de materiales (N-M) |
| t_pedido | t_order | Pedidos |
| t_linea_de_pedido | t_order_line | Líneas de pedido |
| t_pago | t_payment | Pagos (varios por pedido; negativos = devoluciones) |

Hay "trampas" a propósito para practicar: productos nunca vendidos, un proyecto sin personas asignadas, clientes sin pedidos, pedidos entregados sin pagar, móviles sin dueño, empleados sin oficina, NULLs en emails…

### Regenerar

```bash
python generator/build.py
```

---

## English

A sample relational database to learn and teach SQL, **that isn't the boring customers-and-sales one**.

GenBit is a scientific conglomerate in the year 2188. It researches genetics, quantum physics and neuroscience; sells freeze rays, pine cone launchers, entanglement keychains and warp drives; has offices on the Moon, Mars and Proxima b; and its customers include humans, Europan cephalopods and the odd sentient cloud.

- **19 related tables**, ~900 rows.
- **Spanish and English**: same data and ids; table/column names and text values are translated.
- **CSV** (UTF-8, comma, header; NULL = empty cell) and **SQL** for **MySQL 8 / MariaDB** and **SQLite**, plus ready-made `.sqlite` databases.
- **15 example queries** per language (JOINs, aggregates, subqueries, window functions).
- All data is **fictional**. Currency: galactic credits (GC).

Files live in `data/en/`, `sql/genbit_en_*.sql`, `sql/queries_en.sql` and `docs/db/genbit_en.sqlite` (see the table above for the Spanish ↔ English table names).

```bash
mysql -u root -p < sql/genbit_en_mysql.sql
```

```bash
sqlite3 genbit.db < sql/genbit_en_sqlite.sql
```

Built-in gotchas for practice: never-sold products, a project with nobody assigned, customers without orders, delivered-but-unpaid orders, unassigned phones, employees without an office, NULL emails…

Regenerate everything with `python generator/build.py`.

---

## Licencia / License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — Manu Herrán. Úsalo libremente citando la fuente / Free to use with attribution.
