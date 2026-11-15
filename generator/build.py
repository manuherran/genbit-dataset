# -*- coding: utf-8 -*-
"""
Builds the GenBit dataset in Spanish and English:

  data/{es,en}/*.csv          one CSV per table (UTF-8, comma, header row)
  sql/genbit_{es,en}_mysql.sql   MySQL / MariaDB script
  sql/genbit_{es,en}_sqlite.sql  SQLite script
  docs/db/genbit_{es,en}.sqlite  ready-to-use SQLite databases (used by the web)
  docs/downloads/*.zip           bundles for the website
  docs/meta.js                   metadata for the website

Run:  python generator/build.py      (deterministic: same output every time)
"""
import csv
import io
import json
import os
import random
import sqlite3
import unicodedata
import zipfile
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP

import data_model as M
from queries import QUERIES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("es", "en")
rng = random.Random(2187)


def tr(v, lang):
    """Pick the language variant of a translatable value."""
    if isinstance(v, tuple):
        return v[0] if lang == "es" else v[1]
    return v


def ascii_slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return "".join(ch for ch in s if ch.isalnum())


def money(x):
    return float(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def d(s):
    return date.fromisoformat(s)


# ---------------------------------------------------------------------------
# Schema: (key, es_name, en_name, description es/en, columns)
# column: (en, es, type, nullable, ref)   ref = "pk" | ("table_key", "col_en") | None
# ---------------------------------------------------------------------------
SCHEMA = [
    ("planet", "t_planeta", "t_planet",
     ("Planetas, lunas y estaciones donde opera GenBit.", "Planets, moons and stations where GenBit operates."), [
         ("id", "id", "int", False, "pk"),
         ("name", "nombre", "str:50", False, None),
         ("star_system", "sistema_estelar", "str:50", False, None),
         ("body_type", "tipo", "str:50", False, None),
         ("distance_ly", "distancia_al", "dec:8,2", False, None),
         ("gravity_g", "gravedad_g", "dec:4,2", False, None),
         ("population", "poblacion", "bigint", False, None),
         ("habitable", "habitable", "bool", False, None),
     ]),
    ("company", "t_empresa", "t_company",
     ("Empresas del grupo GenBit y socias. id_matriz apunta a la empresa matriz.", "GenBit group companies and partners. parent_company_id points to the parent company."), [
         ("id", "id", "int", False, "pk"),
         ("acronym", "siglas", "str:10", False, None),
         ("name", "nombre", "str:80", False, None),
         ("sector", "sector", "str:50", False, None),
         ("hq_planet_id", "id_planeta_sede", "int", False, ("planet", "id")),
         ("founded_year", "anio_fundacion", "int", False, None),
         ("parent_company_id", "id_matriz", "int", True, ("company", "id")),
         ("headcount", "num_empleados", "int", False, None),
     ]),
    ("office", "t_oficina", "t_office",
     ("Oficinas y laboratorios de cada empresa.", "Offices and labs of each company."), [
         ("id", "id", "int", False, "pk"),
         ("name", "nombre", "str:80", False, None),
         ("company_id", "id_empresa", "int", False, ("company", "id")),
         ("planet_id", "id_planeta", "int", False, ("planet", "id")),
         ("city", "ciudad", "str:50", False, None),
         ("capacity", "capacidad", "int", False, None),
         ("opening_date", "fecha_apertura", "date", False, None),
     ]),
    ("employee", "t_empleado", "t_employee",
     ("Empleados de GenBit. id_jefe es una relación reflexiva (empleado → jefe).", "GenBit employees. manager_id is a self-reference (employee → manager)."), [
         ("id", "id", "int", False, "pk"),
         ("first_name", "nombre", "str:50", False, None),
         ("last_name", "apellidos", "str:80", True, None),
         ("email", "email", "str:100", False, None),
         ("job_title", "puesto", "str:80", False, None),
         ("department", "departamento", "str:50", False, None),
         ("office_id", "id_oficina", "int", True, ("office", "id")),
         ("manager_id", "id_jefe", "int", True, ("employee", "id")),
         ("hire_date", "fecha_alta", "date", False, None),
         ("salary", "salario", "dec:10,2", False, None),
     ]),
    ("mobile", "t_movil", "t_mobile",
     ("Móviles de empresa. Un empleado puede tener varios; algunos no están asignados.", "Company phones. An employee may have several; some are unassigned."), [
         ("number", "numero", "str:15", False, "pk"),
         ("puk", "puk", "str:10", False, None),
         ("model", "modelo", "str:50", False, None),
         ("carrier", "operador", "str:50", False, None),
         ("employee_id", "id_empleado", "int", True, ("employee", "id")),
     ]),
    ("customer", "t_cliente", "t_customer",
     ("Clientes de toda la galaxia (humanos y no humanos).", "Customers from all over the galaxy (human and non-human)."), [
         ("id", "id", "int", False, "pk"),
         ("first_name", "nombre", "str:50", False, None),
         ("last_name", "apellidos", "str:80", True, None),
         ("species", "especie", "str:50", False, None),
         ("email", "email", "str:100", True, None),
         ("planet_id", "id_planeta", "int", False, ("planet", "id")),
         ("company_id", "id_empresa", "int", True, ("company", "id")),
         ("signup_date", "fecha_registro", "date", False, None),
         ("tier", "nivel", "str:20", False, None),
     ]),
    ("supplier", "t_proveedor", "t_supplier",
     ("Proveedores de piezas.", "Parts suppliers."), [
         ("id", "id", "int", False, "pk"),
         ("first_name", "nombre", "str:50", False, None),
         ("last_name", "apellidos", "str:80", False, None),
         ("business_name", "razon_social", "str:80", False, None),
         ("specialty", "especialidad", "str:50", False, None),
         ("planet_id", "id_planeta", "int", False, ("planet", "id")),
         ("rating", "valoracion", "dec:2,1", False, None),
         ("email", "email", "str:100", True, None),
     ]),
    ("investor", "t_inversor", "t_investor",
     ("Inversores. Algunos también son empleados (id_empleado).", "Investors. Some are also employees (employee_id)."), [
         ("id", "id", "int", False, "pk"),
         ("first_name", "nombre", "str:50", False, None),
         ("last_name", "apellidos", "str:80", False, None),
         ("employee_id", "id_empleado", "int", True, ("employee", "id")),
         ("company_id", "id_empresa", "int", False, ("company", "id")),
         ("shares", "numero_acciones", "int", False, None),
         ("investment_date", "fecha_inversion", "date", False, None),
     ]),
    ("project", "t_proyecto", "t_project",
     ("Proyectos de investigación (genética, física cuántica, neurociencia…).", "Research projects (genetics, quantum physics, neuroscience…)."), [
         ("id", "id", "int", False, "pk"),
         ("name", "nombre", "str:80", False, None),
         ("area", "area", "str:50", False, None),
         ("company_id", "id_empresa", "int", False, ("company", "id")),
         ("lead_employee_id", "id_responsable", "int", True, ("employee", "id")),
         ("start_date", "fecha_inicio", "date", False, None),
         ("end_date", "fecha_fin", "date", True, None),
         ("budget", "presupuesto", "dec:14,2", False, None),
         ("status", "estado", "str:20", False, None),
     ]),
    ("assignment", "t_asignacion", "t_assignment",
     ("Relación N-M entre empleados y proyectos.", "N-M relationship between employees and projects."), [
         ("employee_id", "id_empleado", "int", False, ("employee", "id")),
         ("project_id", "id_proyecto", "int", False, ("project", "id")),
         ("role", "rol", "str:30", False, None),
         ("weekly_hours", "horas_semana", "int", False, None),
     ]),
    ("patient", "t_paciente", "t_patient",
     ("Pacientes de los ensayos clínicos de GenBit.", "Patients in GenBit clinical trials."), [
         ("id", "id", "int", False, "pk"),
         ("first_name", "nombre", "str:50", False, None),
         ("last_name", "apellidos", "str:80", True, None),
         ("birth_date", "fecha_nacimiento", "date", False, None),
         ("species", "especie", "str:50", False, None),
         ("blood_type", "grupo_sanguineo", "str:3", True, None),
         ("planet_id", "id_planeta", "int", False, ("planet", "id")),
         ("project_id", "id_proyecto", "int", True, ("project", "id")),
         ("admission_date", "fecha_ingreso", "date", False, None),
         ("status", "estado", "str:30", False, None),
     ]),
    ("subscriber", "t_suscriptor", "t_subscriber",
     ("Suscriptores del boletín. Sin claves foráneas: se cruzan por email.", "Newsletter subscribers. No foreign keys: match them by email."), [
         ("email", "email", "str:100", False, "pk"),
         ("signup_date", "fecha_alta", "date", False, None),
         ("language", "idioma", "str:2", False, None),
         ("newsletter", "boletin", "str:50", False, None),
         ("active", "activo", "bool", False, None),
     ]),
    ("product_line", "t_linea_de_producto", "t_product_line",
     ("Líneas de producto.", "Product lines."), [
         ("id", "id", "int", False, "pk"),
         ("name", "nombre", "str:80", False, None),
         ("description", "descripcion", "str:200", False, None),
     ]),
    ("product", "t_producto", "t_product",
     ("Productos a la venta. Precios en créditos galácticos (CG).", "Products for sale. Prices in galactic credits (GC)."), [
         ("id", "id", "int", False, "pk"),
         ("name", "nombre", "str:80", False, None),
         ("product_line_id", "id_linea", "int", False, ("product_line", "id")),
         ("project_id", "id_proyecto", "int", True, ("project", "id")),
         ("price", "precio", "dec:12,2", False, None),
         ("stock", "stock", "int", False, None),
         ("launch_date", "fecha_lanzamiento", "date", False, None),
         ("weight_kg", "peso_kg", "dec:10,2", False, None),
     ]),
    ("piece", "t_pieza", "t_piece",
     ("Piezas y componentes.", "Parts and components."), [
         ("id", "id", "int", False, "pk"),
         ("name", "nombre", "str:80", False, None),
         ("material", "material", "str:50", False, None),
         ("supplier_id", "id_proveedor", "int", True, ("supplier", "id")),
         ("cost", "coste", "dec:10,2", False, None),
     ]),
    ("product_piece", "t_producto_pieza", "t_product_piece",
     ("Lista de materiales: qué piezas lleva cada producto (N-M).", "Bill of materials: which parts each product uses (N-M)."), [
         ("product_id", "id_producto", "int", False, ("product", "id")),
         ("piece_id", "id_pieza", "int", False, ("piece", "id")),
         ("quantity", "cantidad", "int", False, None),
     ]),
    ("order", "t_pedido", "t_order",
     ("Pedidos de clientes, gestionados por un empleado de ventas.", "Customer orders, handled by a sales employee."), [
         ("id", "id", "int", False, "pk"),
         ("customer_id", "id_cliente", "int", False, ("customer", "id")),
         ("employee_id", "id_empleado", "int", True, ("employee", "id")),
         ("order_date", "fecha_pedido", "date", False, None),
         ("delivery_date", "fecha_entrega", "date", True, None),
         ("destination_planet_id", "id_planeta_destino", "int", False, ("planet", "id")),
         ("status", "estado", "str:30", False, None),
     ]),
    ("order_line", "t_linea_de_pedido", "t_order_line",
     ("Líneas de cada pedido.", "Lines of each order."), [
         ("order_id", "id_pedido", "int", False, ("order", "id")),
         ("line_number", "numero_linea", "int", False, None),
         ("product_id", "id_producto", "int", False, ("product", "id")),
         ("quantity", "cantidad", "int", False, None),
         ("unit_price", "precio_unitario", "dec:12,2", False, None),
         ("discount_pct", "descuento_pct", "dec:5,2", False, None),
     ]),
    ("payment", "t_pago", "t_payment",
     ("Pagos de pedidos (puede haber varios por pedido; importes negativos = devoluciones).", "Order payments (several per order allowed; negative amounts = refunds)."), [
         ("id", "id", "int", False, "pk"),
         ("order_id", "id_pedido", "int", False, ("order", "id")),
         ("payment_date", "fecha_pago", "date", False, None),
         ("amount", "importe", "dec:14,2", False, None),
         ("method", "metodo", "str:50", False, None),
     ]),
]
COMPOSITE_PK = {"assignment": ("employee_id", "project_id"),
                "product_piece": ("product_id", "piece_id"),
                "order_line": ("order_id", "line_number")}
SCHEMA_BY_KEY = {s[0]: s for s in SCHEMA}


# ---------------------------------------------------------------------------
# Rows (dicts keyed by English column key; values may be (es, en) tuples)
# ---------------------------------------------------------------------------
def build_rows():
    R = {}
    R["planet"] = [dict(id=p[0], name=p[1], star_system=p[2], body_type=p[3], distance_ly=p[4],
                        gravity_g=p[5], population=p[6], habitable=p[7]) for p in M.PLANETS]
    R["company"] = [dict(id=c[0], acronym=c[1], name=c[2], sector=c[3], hq_planet_id=c[4],
                         founded_year=c[5], parent_company_id=c[6], headcount=c[7]) for c in M.COMPANIES]
    R["office"] = [dict(id=o[0], name=o[1], company_id=o[2], planet_id=o[3], city=o[4],
                        capacity=o[5], opening_date=o[6]) for o in M.OFFICES]
    R["employee"] = [dict(id=e[0], first_name=e[1], last_name=e[2] or None,
                          email=f"{ascii_slug(e[1] + e[2])}@genbit.com", job_title=e[3], department=e[4],
                          office_id=e[5], manager_id=e[6], hire_date=e[7], salary=e[8]) for e in M.EMPLOYEES]
    R["mobile"] = [dict(number=m[0], puk=m[1], model=m[2], carrier=m[3], employee_id=m[4]) for m in M.MOBILES]
    R["customer"] = [dict(id=c[0], first_name=c[1], last_name=c[2], species=M.SPECIES[c[3]], email=c[4],
                          planet_id=c[5], company_id=c[6], signup_date=c[7], tier=M.TIERS[c[8]]) for c in M.CUSTOMERS]
    R["supplier"] = [dict(id=s[0], first_name=s[1], last_name=s[2], business_name=s[3], specialty=s[4],
                          planet_id=s[5], rating=s[6], email=s[7]) for s in M.SUPPLIERS]
    R["investor"] = [dict(id=i[0], first_name=i[1], last_name=i[2], employee_id=i[3], company_id=i[4],
                          shares=i[5], investment_date=i[6]) for i in M.INVESTORS]
    R["project"] = [dict(id=p[0], name=p[1], area=p[2], company_id=p[3], lead_employee_id=p[4],
                         start_date=p[5], end_date=p[6], budget=p[7], status=M.PROJECT_STATUS[p[8]])
                    for p in M.PROJECTS]

    # --- assignments (N-M) -------------------------------------------------
    by_dept = {}
    for e in M.EMPLOYEES:
        by_dept.setdefault(e[4][1], []).append(e[0])
    area_dept = {"Neuroscience": ["Neuroscience", "Ethics"], "Genetics": ["Genetics", "Medicine"],
                 "Quantum physics": ["Quantum physics"], "Astrobiology": ["Terraforming", "Genetics"],
                 "Astrophysics": ["Astrophysics", "Engineering", "Quantum physics"],
                 "Bioengineering": ["Terraforming", "Genetics"], "Medicine": ["Medicine", "Genetics"],
                 "Ethics": ["Ethics", "Terraforming"], "Energy": ["Engineering"]}
    assign = {}
    for p in M.PROJECTS:
        pid, area, lead, status = p[0], p[2][1], p[4], p[8]
        if status == "planned":
            continue  # a project nobody works on yet (LEFT JOIN exercise)
        if lead:
            assign[(lead, pid)] = (M.ROLES[4], rng.choice([10, 15, 20]))
        pool = [e for dept in area_dept[area] for e in by_dept.get(dept, [])]
        for e in rng.sample(pool, min(len(pool), rng.randint(1, 4))):
            assign.setdefault((e, pid), (rng.choice(M.ROLES[:4]), rng.choice([5, 8, 10, 15, 20, 25, 30, 40])))
    assign[(7, 13)] = (M.ROLES[3], 6)        # Head of Ethics advises wild suffering project
    assign[(7, 5)] = (M.ROLES[3], 4)
    assign.pop((21, 3), None)
    R["assignment"] = [dict(employee_id=k[0], project_id=k[1], role=v[0], weekly_hours=v[1])
                       for k, v in sorted(assign.items(), key=lambda kv: (kv[0][1], kv[0][0]))]

    R["patient"] = [dict(id=p[0], first_name=p[1], last_name=p[2], birth_date=p[3], species=M.SPECIES[p[4]],
                         blood_type=p[5], planet_id=p[6], project_id=p[7], admission_date=p[8],
                         status=M.PATIENT_STATUS[p[9]]) for p in M.PATIENTS]

    # --- subscribers (matched by email to employees/patients/customers) ------
    subs = [("JulioCabrera@genbit.com", 0), ("RobertDaoust@genbit.com", 4), ("DavidPeace@genbit.com", 3)]
    for e in R["employee"]:
        if e["id"] in (2, 4, 6, 7, 9, 12, 18) and e["email"] not in [s[0] for s in subs]:
            subs.append((e["email"], rng.randrange(len(M.NEWSLETTERS))))
    for c in R["customer"]:
        if c["email"] and rng.random() < 0.45:
            subs.append((c["email"], rng.randrange(len(M.NEWSLETTERS))))
    subs += [("curious.kid@orbitmail.es", 2), ("anon42@darkmatter.void", 3), ("lab-news@opis.st", 0)]
    R["subscriber"] = []
    for i, (email, nl) in enumerate(subs):
        start = d("2180-01-01") + timedelta(days=rng.randrange(0, 3200))
        lang = "es" if email.endswith(".es") or rng.random() < 0.35 else "en"
        R["subscriber"].append(dict(email=email, signup_date=start.isoformat(), language=lang,
                                    newsletter=M.NEWSLETTERS[nl], active=rng.random() > 0.2))

    R["product_line"] = [dict(id=l[0], name=l[1], description=l[2]) for l in M.PRODUCT_LINES]
    R["product"] = [dict(id=p[0], name=p[1], product_line_id=p[2], project_id=p[3], price=p[4], stock=p[5],
                         launch_date=p[6], weight_kg=p[7]) for p in M.PRODUCTS]
    R["piece"] = [dict(id=p[0], name=p[1], material=p[2], supplier_id=p[3], cost=p[4]) for p in M.PIECES]
    R["product_piece"] = [dict(product_id=pr, piece_id=pc, quantity=q)
                          for pr, items in sorted(M.BOM.items()) for pc, q in items]

    # --- orders, lines, payments --------------------------------------------
    sellers = [3, 10, 11, 16, 20]
    seller_w = [1, 4, 4, 3, 2]
    products = {p[0]: p for p in M.PRODUCTS}
    sellable = [p[0] for p in M.PRODUCTS if p[0] != 26]  # the toaster never sold
    weights = []
    for pid in sellable:
        price = products[pid][4]
        weights.append(12 if price < 100 else 8 if price < 1000 else 4 if price < 10000 else 1.5 if price < 200000 else 0.3)
    active_customers = [c for c in M.CUSTOMERS if c[0] not in (11, 29)]  # two customers never buy
    cust_w = [3 if c[8] >= 2 else 1 for c in active_customers]

    orders, lines, payments = [], [], []
    start, end = d("2186-01-01"), d("2188-12-31")
    ndays = (end - start).days
    order_dates = sorted(start + timedelta(days=int(rng.random() ** 0.8 * ndays)) for _ in range(120))
    pay_id = 1
    for oid, odate in enumerate(order_dates, 1):
        cust = rng.choices(active_customers, cust_w)[0]
        seller = rng.choices(sellers, seller_w)[0] if rng.random() > 0.06 else None  # web orders
        dest = cust[5] if rng.random() > 0.15 else rng.choice(M.PLANETS)[0]
        age = (end - odate).days
        roll = rng.random()
        if age < 35:
            status = "pending" if roll < 0.5 else "transit"
        elif age < 60:
            status = "transit" if roll < 0.5 else "delivered" if roll < 0.9 else "pending"
        else:
            status = "delivered" if roll < 0.86 else "cancelled" if roll < 0.95 else "lost"
        dist = next(p for p in M.PLANETS if p[0] == dest)[4]
        delivery = None
        if status == "delivered":
            delivery = (odate + timedelta(days=rng.randint(2, 12) + int(dist * 2))).isoformat()
            if delivery > end.isoformat():
                delivery, status = None, "transit"
        orders.append(dict(id=oid, customer_id=cust[0], employee_id=seller, order_date=odate.isoformat(),
                           delivery_date=delivery, destination_planet_id=dest, status=M.ORDER_STATUS[status]))

        n = rng.choices([1, 2, 3, 4, 5], [35, 30, 20, 10, 5])[0]
        chosen = []
        while len(chosen) < n:
            pid = rng.choices(sellable, weights)[0]
            if pid not in chosen and products[pid][6] <= odate.isoformat():
                chosen.append(pid)
            elif len(chosen) == 0 and rng.random() < 0.05:
                chosen.append(16)
        total = Decimal("0")
        for ln, pid in enumerate(chosen, 1):
            price = products[pid][4]
            qty = 1 if price > 50000 else rng.choice([1, 1, 2, 3]) if price > 5000 else rng.choices([1, 2, 3, 5, 10, 50], [40, 25, 12, 10, 8, 5])[0]
            if pid == 16:
                qty *= 10
            disc = rng.choices([0, 5, 10, 15, 25], [60, 15, 12, 8, 5])[0]
            if cust[8] == 3 and disc == 0:
                disc = 5  # platinum customers always get something
            lines.append(dict(order_id=oid, line_number=ln, product_id=pid, quantity=qty,
                              unit_price=price, discount_pct=float(disc)))
            total += Decimal(str(price)) * qty * (Decimal(100 - disc) / 100)
        total = Decimal(money(total))

        method = rng.choices(M.PAYMENT_METHODS, [40, 25, 20, 10, 5])[0]
        pdate = odate + timedelta(days=rng.randint(0, 3))
        def pay(day, amount, meth=method):
            nonlocal pay_id
            payments.append(dict(id=pay_id, order_id=oid, payment_date=day.isoformat(),
                                 amount=money(amount), method=meth))
            pay_id += 1
        if status in ("delivered", "lost"):
            if total > 20000 and rng.random() < 0.6:
                k = rng.choice([2, 3])
                part = Decimal(money(total / k))
                for j in range(k):
                    amt = part if j < k - 1 else total - part * (k - 1)
                    pay(pdate + timedelta(days=30 * j), amt)
            elif rng.random() < 0.95:
                pay(pdate, total)  # ~5% delivered but never paid (debtors!)
            if status == "lost":
                pay(pdate + timedelta(days=45), -total)
        elif status == "transit":
            if rng.random() < 0.7:
                pay(pdate, total)
            elif total > 1000:
                pay(pdate, Decimal(money(total / 2)))
        elif status == "pending":
            if rng.random() < 0.3:
                pay(pdate, total)
        elif status == "cancelled":
            if rng.random() < 0.5:
                pay(pdate, total)
                pay(pdate + timedelta(days=rng.randint(3, 20)), -total)
    R["order"], R["order_line"], R["payment"] = orders, lines, payments
    return R


# ---------------------------------------------------------------------------
# Writers
# ---------------------------------------------------------------------------
def cname(col, lang):
    return col[1] if lang == "es" else col[0]


def tname(key, lang):
    s = SCHEMA_BY_KEY[key]
    return s[1] if lang == "es" else s[2]


def csv_value(v, typ):
    if v is None:
        return ""
    if typ == "bool":
        return "1" if v else "0"
    if typ.startswith("dec"):
        scale = int(typ.split(",")[1])
        return f"{v:.{scale}f}"
    return str(v)


def sql_value(v, typ):
    if v is None:
        return "NULL"
    if typ == "bool":
        return "TRUE" if v else "FALSE"
    if typ in ("int", "bigint"):
        return str(int(v))
    if typ.startswith("dec"):
        return csv_value(v, typ)
    return "'" + str(v).replace("'", "''") + "'"


def sql_type(typ, dialect):
    if typ == "int":
        return "INT" if dialect == "mysql" else "INTEGER"
    if typ == "bigint":
        return "BIGINT" if dialect == "mysql" else "INTEGER"
    if typ.startswith("str:"):
        return f"VARCHAR({typ[4:]})"
    if typ.startswith("dec:"):
        return f"DECIMAL({typ[4:]})"
    return {"date": "DATE", "bool": "BOOLEAN", "text": "TEXT"}[typ]


def localized_rows(R, key, lang):
    cols = SCHEMA_BY_KEY[key][4]
    out = []
    for r in R[key]:
        out.append([tr(r[c[0]], lang) for c in cols])
    return out


def write_csvs(R, lang):
    folder = os.path.join(ROOT, "data", lang)
    os.makedirs(folder, exist_ok=True)
    for key, es, en, _, cols in SCHEMA:
        path = os.path.join(folder, (es if lang == "es" else en) + ".csv")
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow([cname(c, lang) for c in cols])
            for row in localized_rows(R, key, lang):
                w.writerow([csv_value(v, c[2]) for v, c in zip(row, cols)])


HEADER = {
    "es": """-- =====================================================================
-- GenBit Dataset (ES) — base de datos relacional de ejemplo
-- Universo: GenBit, conglomerado científico del año 2188 (genética,
-- física cuántica, neurociencia, terraformación...).
-- Todos los datos son ficticios. Moneda: créditos galácticos (CG).
-- Licencia: CC BY 4.0 — https://github.com/manuherran/genbit-dataset
-- Generado automáticamente por generator/build.py — no editar a mano.
-- =====================================================================
""",
    "en": """-- =====================================================================
-- GenBit Dataset (EN) — sample relational database
-- Universe: GenBit, a scientific conglomerate in the year 2188 (genetics,
-- quantum physics, neuroscience, terraforming...).
-- All data is fictional. Currency: galactic credits (GC).
-- License: CC BY 4.0 — https://github.com/manuherran/genbit-dataset
-- Auto-generated by generator/build.py — do not edit by hand.
-- =====================================================================
""",
}


def sql_script(R, lang, dialect):
    out = io.StringIO()
    out.write(HEADER[lang] + "\n")
    db = f"db_genbit_{lang}"
    if dialect == "mysql":
        out.write(f"DROP DATABASE IF EXISTS {db};\n")
        out.write(f"CREATE DATABASE {db} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;\n")
        out.write(f"USE {db};\n\n")
    else:
        out.write("PRAGMA foreign_keys = ON;\n\n")
        for key, *_ in reversed(SCHEMA):
            out.write(f"DROP TABLE IF EXISTS {tname(key, lang)};\n")
        out.write("\n")

    step1 = "Paso 1: tablas, claves primarias y foráneas" if lang == "es" else "Step 1: tables, primary and foreign keys"
    out.write(f"-- {step1}\n\n")
    for key, es, en, desc, cols in SCHEMA:
        t = es if lang == "es" else en
        out.write(f"-- {tr(desc, lang)}\n")
        out.write(f"CREATE TABLE {t} (\n")
        parts = []
        for c in cols:
            line = f"  {cname(c, lang)} {sql_type(c[2], dialect)}"
            line += " NULL" if c[3] else " NOT NULL"
            parts.append(line)
        pk = COMPOSITE_PK.get(key) or tuple(c[0] for c in cols if c[4] == "pk")
        colmap = {c[0]: c for c in cols}
        parts.append(f"  PRIMARY KEY ({', '.join(cname(colmap[k], lang) for k in pk)})")
        n = 1
        for c in cols:
            if isinstance(c[4], tuple):
                rt, rc = c[4]
                rcol = next(x for x in SCHEMA_BY_KEY[rt][4] if x[0] == rc)
                parts.append(f"  CONSTRAINT fk_{t[2:]}_{n} FOREIGN KEY ({cname(c, lang)}) "
                             f"REFERENCES {tname(rt, lang)} ({cname(rcol, lang)})")
                n += 1
        out.write(",\n".join(parts))
        out.write("\n)" + (" ENGINE=InnoDB DEFAULT CHARSET=utf8mb4" if dialect == "mysql" else "") + ";\n\n")

    step2 = "Paso 2: inserción de datos" if lang == "es" else "Step 2: data"
    out.write(f"-- {step2}\n\n")
    for key, es, en, _, cols in SCHEMA:
        t = es if lang == "es" else en
        rows = localized_rows(R, key, lang)
        collist = ", ".join(cname(c, lang) for c in cols)
        out.write(f"INSERT INTO {t} ({collist}) VALUES\n")
        vals = ["  (" + ", ".join(sql_value(v, c[2]) for v, c in zip(row, cols)) + ")" for row in rows]
        out.write(",\n".join(vals) + ";\n\n")
    return out.getvalue()


def er_mermaid(lang):
    lines = ["erDiagram"]
    for key, es, en, _, cols in SCHEMA:
        t = es if lang == "es" else en
        for c in cols:
            if isinstance(c[4], tuple):
                rt = tname(c[4][0], lang)
                card = "|o--o{" if c[3] else "||--o{"
                lines.append(f"  {rt} {card} {t} : {cname(c, lang)}")
    return "\n".join(lines)


def main():
    R = build_rows()
    os.makedirs(os.path.join(ROOT, "sql"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "docs", "db"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "docs", "downloads"), exist_ok=True)
    meta = {}
    for lang in LANGS:
        write_csvs(R, lang)
        scripts = {}
        for dialect in ("mysql", "sqlite"):
            s = sql_script(R, lang, dialect)
            scripts[dialect] = s
            with open(os.path.join(ROOT, "sql", f"genbit_{lang}_{dialect}.sql"), "w", encoding="utf-8", newline="\n") as f:
                f.write(s)
        qpath = os.path.join(ROOT, "sql", f"queries_{lang}.sql")
        with open(qpath, "w", encoding="utf-8", newline="\n") as f:
            f.write(HEADER[lang].replace("— no editar a mano", "").replace("— do not edit by hand", "") + "\n")
            for q in QUERIES[lang]:
                f.write(f"-- {q['title']}\n{q['sql'].strip()};\n\n")

        # SQLite database (also validates the script + every example query)
        dbpath = os.path.join(ROOT, "docs", "db", f"genbit_{lang}.sqlite")
        if os.path.exists(dbpath):
            os.remove(dbpath)
        con = sqlite3.connect(dbpath)
        con.executescript(scripts["sqlite"])
        bad = con.execute("PRAGMA foreign_key_check").fetchall()
        assert not bad, f"FK violations: {bad[:5]}"
        counts = {}
        for key, *_ in SCHEMA:
            t = tname(key, lang)
            counts[t] = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        for q in QUERIES[lang]:
            con.execute(q["sql"]).fetchall()
        con.execute("VACUUM")
        con.close()

        # zip bundles
        with zipfile.ZipFile(os.path.join(ROOT, "docs", "downloads", f"genbit_{lang}_csv.zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for key, *_ in SCHEMA:
                fn = tname(key, lang) + ".csv"
                z.write(os.path.join(ROOT, "data", lang, fn), fn)
        with zipfile.ZipFile(os.path.join(ROOT, "docs", "downloads", f"genbit_{lang}_sql.zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for fn in (f"genbit_{lang}_mysql.sql", f"genbit_{lang}_sqlite.sql", f"queries_{lang}.sql"):
                z.write(os.path.join(ROOT, "sql", fn), fn)

        meta[lang] = {
            "er": er_mermaid(lang),
            "tables": [{"name": tname(k, lang), "desc": tr(desc, lang), "rows": counts[tname(k, lang)],
                        "cols": [{"name": cname(c, lang), "type": sql_type(c[2], "mysql"),
                                  "null": c[3], "pk": c[4] == "pk" or c[0] in COMPOSITE_PK.get(k, ()),
                                  "fk": (tname(c[4][0], lang) if isinstance(c[4], tuple) else None)} for c in cols]}
                       for k, _, _, desc, cols in SCHEMA],
            "queries": QUERIES[lang],
        }
        print(lang, sum(counts.values()), "rows", counts)
    with open(os.path.join(ROOT, "docs", "meta.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write("window.GENBIT_META = " + json.dumps(meta, ensure_ascii=False, indent=1) + ";\n")


if __name__ == "__main__":
    main()
