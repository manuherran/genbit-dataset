window.GENBIT_META = {
 "es": {
  "er": "erDiagram\n  t_planeta ||--o{ t_empresa : id_planeta_sede\n  t_empresa |o--o{ t_empresa : id_matriz\n  t_empresa ||--o{ t_oficina : id_empresa\n  t_planeta ||--o{ t_oficina : id_planeta\n  t_oficina |o--o{ t_empleado : id_oficina\n  t_empleado |o--o{ t_empleado : id_jefe\n  t_empleado |o--o{ t_movil : id_empleado\n  t_planeta ||--o{ t_cliente : id_planeta\n  t_empresa |o--o{ t_cliente : id_empresa\n  t_planeta ||--o{ t_proveedor : id_planeta\n  t_empleado |o--o{ t_inversor : id_empleado\n  t_empresa ||--o{ t_inversor : id_empresa\n  t_empresa ||--o{ t_proyecto : id_empresa\n  t_empleado |o--o{ t_proyecto : id_responsable\n  t_empleado ||--o{ t_asignacion : id_empleado\n  t_proyecto ||--o{ t_asignacion : id_proyecto\n  t_planeta ||--o{ t_paciente : id_planeta\n  t_proyecto |o--o{ t_paciente : id_proyecto\n  t_linea_de_producto ||--o{ t_producto : id_linea\n  t_proyecto |o--o{ t_producto : id_proyecto\n  t_proveedor |o--o{ t_pieza : id_proveedor\n  t_producto ||--o{ t_producto_pieza : id_producto\n  t_pieza ||--o{ t_producto_pieza : id_pieza\n  t_cliente ||--o{ t_pedido : id_cliente\n  t_empleado |o--o{ t_pedido : id_empleado\n  t_planeta ||--o{ t_pedido : id_planeta_destino\n  t_pedido ||--o{ t_linea_de_pedido : id_pedido\n  t_producto ||--o{ t_linea_de_pedido : id_producto\n  t_pedido ||--o{ t_pago : id_pedido",
  "tables": [
   {
    "name": "t_planeta",
    "desc": "Planetas, lunas y estaciones donde opera GenBit.",
    "rows": 14,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "sistema_estelar",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "tipo",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "distancia_al",
      "type": "DECIMAL(8,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "gravedad_g",
      "type": "DECIMAL(4,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "poblacion",
      "type": "BIGINT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "habitable",
      "type": "BOOLEAN",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_empresa",
    "desc": "Empresas del grupo GenBit y socias. id_matriz apunta a la empresa matriz.",
    "rows": 17,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "siglas",
      "type": "VARCHAR(10)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "sector",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_planeta_sede",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planeta"
     },
     {
      "name": "anio_fundacion",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_matriz",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_empresa"
     },
     {
      "name": "num_empleados",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_oficina",
    "desc": "Oficinas y laboratorios de cada empresa.",
    "rows": 20,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_empresa",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_empresa"
     },
     {
      "name": "id_planeta",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planeta"
     },
     {
      "name": "ciudad",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "capacidad",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "fecha_apertura",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_empleado",
    "desc": "Empleados de GenBit. id_jefe es una relación reflexiva (empleado → jefe).",
    "rows": 21,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "apellidos",
      "type": "VARCHAR(80)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "email",
      "type": "VARCHAR(100)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "puesto",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "departamento",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_oficina",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_oficina"
     },
     {
      "name": "id_jefe",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_empleado"
     },
     {
      "name": "fecha_alta",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "salario",
      "type": "DECIMAL(10,2)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_movil",
    "desc": "Móviles de empresa. Un empleado puede tener varios; algunos no están asignados.",
    "rows": 13,
    "cols": [
     {
      "name": "numero",
      "type": "VARCHAR(15)",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "puk",
      "type": "VARCHAR(10)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "modelo",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "operador",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_empleado",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_empleado"
     }
    ]
   },
   {
    "name": "t_cliente",
    "desc": "Clientes de toda la galaxia (humanos y no humanos).",
    "rows": 30,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "apellidos",
      "type": "VARCHAR(80)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "especie",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "email",
      "type": "VARCHAR(100)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_planeta",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planeta"
     },
     {
      "name": "id_empresa",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_empresa"
     },
     {
      "name": "fecha_registro",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "nivel",
      "type": "VARCHAR(20)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_proveedor",
    "desc": "Proveedores de piezas.",
    "rows": 10,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "apellidos",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "razon_social",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "especialidad",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_planeta",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planeta"
     },
     {
      "name": "valoracion",
      "type": "DECIMAL(2,1)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "email",
      "type": "VARCHAR(100)",
      "null": true,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_inversor",
    "desc": "Inversores. Algunos también son empleados (id_empleado).",
    "rows": 15,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "apellidos",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_empleado",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_empleado"
     },
     {
      "name": "id_empresa",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_empresa"
     },
     {
      "name": "numero_acciones",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "fecha_inversion",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_proyecto",
    "desc": "Proyectos de investigación (genética, física cuántica, neurociencia…).",
    "rows": 15,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "area",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_empresa",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_empresa"
     },
     {
      "name": "id_responsable",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_empleado"
     },
     {
      "name": "fecha_inicio",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "fecha_fin",
      "type": "DATE",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "presupuesto",
      "type": "DECIMAL(14,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "estado",
      "type": "VARCHAR(20)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_asignacion",
    "desc": "Relación N-M entre empleados y proyectos.",
    "rows": 41,
    "cols": [
     {
      "name": "id_empleado",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_empleado"
     },
     {
      "name": "id_proyecto",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_proyecto"
     },
     {
      "name": "rol",
      "type": "VARCHAR(30)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "horas_semana",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_paciente",
    "desc": "Pacientes de los ensayos clínicos de GenBit.",
    "rows": 20,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "apellidos",
      "type": "VARCHAR(80)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "fecha_nacimiento",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "especie",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "grupo_sanguineo",
      "type": "VARCHAR(3)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_planeta",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planeta"
     },
     {
      "name": "id_proyecto",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_proyecto"
     },
     {
      "name": "fecha_ingreso",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "estado",
      "type": "VARCHAR(30)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_suscriptor",
    "desc": "Suscriptores del boletín. Sin claves foráneas: se cruzan por email.",
    "rows": 23,
    "cols": [
     {
      "name": "email",
      "type": "VARCHAR(100)",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "fecha_alta",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "idioma",
      "type": "VARCHAR(2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "boletin",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "activo",
      "type": "BOOLEAN",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_linea_de_producto",
    "desc": "Líneas de producto.",
    "rows": 8,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "descripcion",
      "type": "VARCHAR(200)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_producto",
    "desc": "Productos a la venta. Precios en créditos galácticos (CG).",
    "rows": 26,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_linea",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_linea_de_producto"
     },
     {
      "name": "id_proyecto",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_proyecto"
     },
     {
      "name": "precio",
      "type": "DECIMAL(12,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "stock",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "fecha_lanzamiento",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "peso_kg",
      "type": "DECIMAL(10,2)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_pieza",
    "desc": "Piezas y componentes.",
    "rows": 26,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "nombre",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "material",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_proveedor",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_proveedor"
     },
     {
      "name": "coste",
      "type": "DECIMAL(10,2)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_producto_pieza",
    "desc": "Lista de materiales: qué piezas lleva cada producto (N-M).",
    "rows": 69,
    "cols": [
     {
      "name": "id_producto",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_producto"
     },
     {
      "name": "id_pieza",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_pieza"
     },
     {
      "name": "cantidad",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_pedido",
    "desc": "Pedidos de clientes, gestionados por un empleado de ventas.",
    "rows": 120,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "id_cliente",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_cliente"
     },
     {
      "name": "id_empleado",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_empleado"
     },
     {
      "name": "fecha_pedido",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "fecha_entrega",
      "type": "DATE",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "id_planeta_destino",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planeta"
     },
     {
      "name": "estado",
      "type": "VARCHAR(30)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_linea_de_pedido",
    "desc": "Líneas de cada pedido.",
    "rows": 269,
    "cols": [
     {
      "name": "id_pedido",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_pedido"
     },
     {
      "name": "numero_linea",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "id_producto",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_producto"
     },
     {
      "name": "cantidad",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "precio_unitario",
      "type": "DECIMAL(12,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "descuento_pct",
      "type": "DECIMAL(5,2)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_pago",
    "desc": "Pagos de pedidos (puede haber varios por pedido; importes negativos = devoluciones).",
    "rows": 135,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "id_pedido",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_pedido"
     },
     {
      "name": "fecha_pago",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "importe",
      "type": "DECIMAL(14,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "metodo",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   }
  ],
  "queries": [
   {
    "title": "1. Todos los planetas habitables, del más cercano al más lejano",
    "sql": "SELECT nombre, sistema_estelar, distancia_al, gravedad_g, poblacion\nFROM t_planeta\nWHERE habitable = TRUE\nORDER BY distancia_al, nombre"
   },
   {
    "title": "2. INNER JOIN: empleados que también son inversores",
    "sql": "SELECT e.nombre, e.apellidos, e.puesto, i.numero_acciones, em.siglas AS empresa\nFROM t_empleado e\nINNER JOIN t_inversor i ON i.id_empleado = e.id\nINNER JOIN t_empresa em ON em.id = i.id_empresa\nORDER BY i.numero_acciones DESC"
   },
   {
    "title": "3. LEFT JOIN: acciones de cada empleado (0 si no invierte)",
    "sql": "SELECT e.id, e.nombre, e.apellidos, COALESCE(SUM(i.numero_acciones), 0) AS acciones\nFROM t_empleado e\nLEFT JOIN t_inversor i ON i.id_empleado = e.id\nGROUP BY e.id, e.nombre, e.apellidos\nORDER BY acciones DESC, e.id"
   },
   {
    "title": "4. Relación reflexiva: cada empleado con su jefe",
    "sql": "SELECT emp.nombre AS empleado, emp.puesto, jef.nombre AS jefe\nFROM t_empleado emp\nLEFT JOIN t_empleado jef ON emp.id_jefe = jef.id\nORDER BY jef.id, emp.id"
   },
   {
    "title": "5. Móviles sin asignar y empleados sin móvil",
    "sql": "SELECT m.numero, m.modelo, e.nombre AS empleado\nFROM t_movil m\nLEFT JOIN t_empleado e ON e.id = m.id_empleado\nWHERE e.id IS NULL\nUNION ALL\nSELECT NULL, NULL, e.nombre\nFROM t_empleado e\nWHERE e.id NOT IN (SELECT id_empleado FROM t_movil WHERE id_empleado IS NOT NULL)"
   },
   {
    "title": "6. Facturación por línea de producto",
    "sql": "SELECT l.nombre AS linea,\n       COUNT(DISTINCT lp.id_pedido) AS pedidos,\n       SUM(lp.cantidad) AS unidades,\n       ROUND(SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)), 2) AS facturacion_cg\nFROM t_linea_de_producto l\nLEFT JOIN t_producto p ON p.id_linea = l.id\nLEFT JOIN t_linea_de_pedido lp ON lp.id_producto = p.id\nGROUP BY l.id, l.nombre\nORDER BY facturacion_cg DESC"
   },
   {
    "title": "7. Top 5 clientes por importe pagado (neto de devoluciones)",
    "sql": "SELECT c.nombre, c.apellidos, c.especie, ROUND(SUM(pg.importe), 2) AS pagado_cg\nFROM t_cliente c\nJOIN t_pedido pe ON pe.id_cliente = c.id\nJOIN t_pago pg ON pg.id_pedido = pe.id\nGROUP BY c.id, c.nombre, c.apellidos, c.especie\nORDER BY pagado_cg DESC\nLIMIT 5"
   },
   {
    "title": "8. Pedidos entregados con deuda pendiente",
    "sql": "SELECT pe.id, pe.fecha_pedido, c.nombre AS cliente, t.total, COALESCE(pg.pagado, 0) AS pagado,\n       ROUND(t.total - COALESCE(pg.pagado, 0), 2) AS pendiente\nFROM t_pedido pe\nJOIN t_cliente c ON c.id = pe.id_cliente\nJOIN (SELECT id_pedido, ROUND(SUM(cantidad * precio_unitario * (1 - descuento_pct / 100.0)), 2) AS total\n      FROM t_linea_de_pedido GROUP BY id_pedido) t ON t.id_pedido = pe.id\nLEFT JOIN (SELECT id_pedido, SUM(importe) AS pagado FROM t_pago GROUP BY id_pedido) pg ON pg.id_pedido = pe.id\nWHERE pe.estado = 'Entregado' AND t.total - COALESCE(pg.pagado, 0) > 0.01\nORDER BY pendiente DESC"
   },
   {
    "title": "9. Productos que nunca se han vendido",
    "sql": "SELECT p.id, p.nombre, p.stock\nFROM t_producto p\nWHERE NOT EXISTS (SELECT 1 FROM t_linea_de_pedido lp WHERE lp.id_producto = p.id)"
   },
   {
    "title": "10. Coste de fabricación vs. precio (margen) de cada producto",
    "sql": "SELECT p.nombre, p.precio, ROUND(SUM(pp.cantidad * pz.coste), 2) AS coste_piezas,\n       ROUND(p.precio - SUM(pp.cantidad * pz.coste), 2) AS margen\nFROM t_producto p\nJOIN t_producto_pieza pp ON pp.id_producto = p.id\nJOIN t_pieza pz ON pz.id = pp.id_pieza\nGROUP BY p.id, p.nombre, p.precio\nORDER BY margen"
   },
   {
    "title": "11. Proyectos con su responsable, nº de personas y horas semanales",
    "sql": "SELECT pr.nombre AS proyecto, pr.area, pr.estado, r.nombre AS responsable,\n       COUNT(a.id_empleado) AS personas, COALESCE(SUM(a.horas_semana), 0) AS horas_semana\nFROM t_proyecto pr\nLEFT JOIN t_empleado r ON r.id = pr.id_responsable\nLEFT JOIN t_asignacion a ON a.id_proyecto = pr.id\nGROUP BY pr.id, pr.nombre, pr.area, pr.estado, r.nombre\nORDER BY horas_semana DESC"
   },
   {
    "title": "12. Pacientes por proyecto y estado",
    "sql": "SELECT COALESCE(pr.nombre, '(sin proyecto)') AS proyecto, pa.estado, COUNT(*) AS pacientes\nFROM t_paciente pa\nLEFT JOIN t_proyecto pr ON pr.id = pa.id_proyecto\nGROUP BY pr.nombre, pa.estado\nORDER BY proyecto, pacientes DESC"
   },
   {
    "title": "13. Suscriptores que son empleados, clientes o ninguno (cruce por email)",
    "sql": "SELECT s.email, s.boletin,\n       CASE WHEN e.id IS NOT NULL THEN 'Empleado'\n            WHEN c.id IS NOT NULL THEN 'Cliente'\n            ELSE 'Desconocido' END AS tipo\nFROM t_suscriptor s\nLEFT JOIN t_empleado e ON e.email = s.email\nLEFT JOIN t_cliente c ON c.email = s.email\nORDER BY tipo, s.email"
   },
   {
    "title": "14. Ventas mensuales y acumulado (funciones de ventana)",
    "sql": "SELECT mes, ventas_cg, ROUND(SUM(ventas_cg) OVER (ORDER BY mes), 2) AS acumulado_cg\nFROM (\n  SELECT SUBSTR(pe.fecha_pedido, 1, 7) AS mes,\n         ROUND(SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)), 2) AS ventas_cg\n  FROM t_pedido pe\n  JOIN t_linea_de_pedido lp ON lp.id_pedido = pe.id\n  WHERE pe.estado <> 'Cancelado'\n  GROUP BY SUBSTR(pe.fecha_pedido, 1, 7)\n) m\nORDER BY mes"
   },
   {
    "title": "15. Ranking de vendedores por facturación",
    "sql": "SELECT COALESCE(e.nombre, '(web)') AS vendedor, COUNT(DISTINCT pe.id) AS pedidos,\n       ROUND(SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)), 2) AS facturacion_cg,\n       RANK() OVER (ORDER BY SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)) DESC) AS puesto\nFROM t_pedido pe\nJOIN t_linea_de_pedido lp ON lp.id_pedido = pe.id\nLEFT JOIN t_empleado e ON e.id = pe.id_empleado\nGROUP BY e.id, e.nombre"
   }
  ]
 },
 "en": {
  "er": "erDiagram\n  t_planet ||--o{ t_company : hq_planet_id\n  t_company |o--o{ t_company : parent_company_id\n  t_company ||--o{ t_office : company_id\n  t_planet ||--o{ t_office : planet_id\n  t_office |o--o{ t_employee : office_id\n  t_employee |o--o{ t_employee : manager_id\n  t_employee |o--o{ t_mobile : employee_id\n  t_planet ||--o{ t_customer : planet_id\n  t_company |o--o{ t_customer : company_id\n  t_planet ||--o{ t_supplier : planet_id\n  t_employee |o--o{ t_investor : employee_id\n  t_company ||--o{ t_investor : company_id\n  t_company ||--o{ t_project : company_id\n  t_employee |o--o{ t_project : lead_employee_id\n  t_employee ||--o{ t_assignment : employee_id\n  t_project ||--o{ t_assignment : project_id\n  t_planet ||--o{ t_patient : planet_id\n  t_project |o--o{ t_patient : project_id\n  t_product_line ||--o{ t_product : product_line_id\n  t_project |o--o{ t_product : project_id\n  t_supplier |o--o{ t_piece : supplier_id\n  t_product ||--o{ t_product_piece : product_id\n  t_piece ||--o{ t_product_piece : piece_id\n  t_customer ||--o{ t_order : customer_id\n  t_employee |o--o{ t_order : employee_id\n  t_planet ||--o{ t_order : destination_planet_id\n  t_order ||--o{ t_order_line : order_id\n  t_product ||--o{ t_order_line : product_id\n  t_order ||--o{ t_payment : order_id",
  "tables": [
   {
    "name": "t_planet",
    "desc": "Planets, moons and stations where GenBit operates.",
    "rows": 14,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "name",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "star_system",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "body_type",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "distance_ly",
      "type": "DECIMAL(8,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "gravity_g",
      "type": "DECIMAL(4,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "population",
      "type": "BIGINT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "habitable",
      "type": "BOOLEAN",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_company",
    "desc": "GenBit group companies and partners. parent_company_id points to the parent company.",
    "rows": 17,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "acronym",
      "type": "VARCHAR(10)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "name",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "sector",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "hq_planet_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planet"
     },
     {
      "name": "founded_year",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "parent_company_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_company"
     },
     {
      "name": "headcount",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_office",
    "desc": "Offices and labs of each company.",
    "rows": 20,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "name",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "company_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_company"
     },
     {
      "name": "planet_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planet"
     },
     {
      "name": "city",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "capacity",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "opening_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_employee",
    "desc": "GenBit employees. manager_id is a self-reference (employee → manager).",
    "rows": 21,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "first_name",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "last_name",
      "type": "VARCHAR(80)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "email",
      "type": "VARCHAR(100)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "job_title",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "department",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "office_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_office"
     },
     {
      "name": "manager_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_employee"
     },
     {
      "name": "hire_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "salary",
      "type": "DECIMAL(10,2)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_mobile",
    "desc": "Company phones. An employee may have several; some are unassigned.",
    "rows": 13,
    "cols": [
     {
      "name": "number",
      "type": "VARCHAR(15)",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "puk",
      "type": "VARCHAR(10)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "model",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "carrier",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "employee_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_employee"
     }
    ]
   },
   {
    "name": "t_customer",
    "desc": "Customers from all over the galaxy (human and non-human).",
    "rows": 30,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "first_name",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "last_name",
      "type": "VARCHAR(80)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "species",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "email",
      "type": "VARCHAR(100)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "planet_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planet"
     },
     {
      "name": "company_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_company"
     },
     {
      "name": "signup_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "tier",
      "type": "VARCHAR(20)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_supplier",
    "desc": "Parts suppliers.",
    "rows": 10,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "first_name",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "last_name",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "business_name",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "specialty",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "planet_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planet"
     },
     {
      "name": "rating",
      "type": "DECIMAL(2,1)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "email",
      "type": "VARCHAR(100)",
      "null": true,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_investor",
    "desc": "Investors. Some are also employees (employee_id).",
    "rows": 15,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "first_name",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "last_name",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "employee_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_employee"
     },
     {
      "name": "company_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_company"
     },
     {
      "name": "shares",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "investment_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_project",
    "desc": "Research projects (genetics, quantum physics, neuroscience…).",
    "rows": 15,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "name",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "area",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "company_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_company"
     },
     {
      "name": "lead_employee_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_employee"
     },
     {
      "name": "start_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "end_date",
      "type": "DATE",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "budget",
      "type": "DECIMAL(14,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "status",
      "type": "VARCHAR(20)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_assignment",
    "desc": "N-M relationship between employees and projects.",
    "rows": 41,
    "cols": [
     {
      "name": "employee_id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_employee"
     },
     {
      "name": "project_id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_project"
     },
     {
      "name": "role",
      "type": "VARCHAR(30)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "weekly_hours",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_patient",
    "desc": "Patients in GenBit clinical trials.",
    "rows": 20,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "first_name",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "last_name",
      "type": "VARCHAR(80)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "birth_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "species",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "blood_type",
      "type": "VARCHAR(3)",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "planet_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planet"
     },
     {
      "name": "project_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_project"
     },
     {
      "name": "admission_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "status",
      "type": "VARCHAR(30)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_subscriber",
    "desc": "Newsletter subscribers. No foreign keys: match them by email.",
    "rows": 23,
    "cols": [
     {
      "name": "email",
      "type": "VARCHAR(100)",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "signup_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "language",
      "type": "VARCHAR(2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "newsletter",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "active",
      "type": "BOOLEAN",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_product_line",
    "desc": "Product lines.",
    "rows": 8,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "name",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "description",
      "type": "VARCHAR(200)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_product",
    "desc": "Products for sale. Prices in galactic credits (GC).",
    "rows": 26,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "name",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "product_line_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_product_line"
     },
     {
      "name": "project_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_project"
     },
     {
      "name": "price",
      "type": "DECIMAL(12,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "stock",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "launch_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "weight_kg",
      "type": "DECIMAL(10,2)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_piece",
    "desc": "Parts and components.",
    "rows": 26,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "name",
      "type": "VARCHAR(80)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "material",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "supplier_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_supplier"
     },
     {
      "name": "cost",
      "type": "DECIMAL(10,2)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_product_piece",
    "desc": "Bill of materials: which parts each product uses (N-M).",
    "rows": 69,
    "cols": [
     {
      "name": "product_id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_product"
     },
     {
      "name": "piece_id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_piece"
     },
     {
      "name": "quantity",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_order",
    "desc": "Customer orders, handled by a sales employee.",
    "rows": 120,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "customer_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_customer"
     },
     {
      "name": "employee_id",
      "type": "INT",
      "null": true,
      "pk": false,
      "fk": "t_employee"
     },
     {
      "name": "order_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "delivery_date",
      "type": "DATE",
      "null": true,
      "pk": false,
      "fk": null
     },
     {
      "name": "destination_planet_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_planet"
     },
     {
      "name": "status",
      "type": "VARCHAR(30)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_order_line",
    "desc": "Lines of each order.",
    "rows": 269,
    "cols": [
     {
      "name": "order_id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": "t_order"
     },
     {
      "name": "line_number",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "product_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_product"
     },
     {
      "name": "quantity",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "unit_price",
      "type": "DECIMAL(12,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "discount_pct",
      "type": "DECIMAL(5,2)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   },
   {
    "name": "t_payment",
    "desc": "Order payments (several per order allowed; negative amounts = refunds).",
    "rows": 135,
    "cols": [
     {
      "name": "id",
      "type": "INT",
      "null": false,
      "pk": true,
      "fk": null
     },
     {
      "name": "order_id",
      "type": "INT",
      "null": false,
      "pk": false,
      "fk": "t_order"
     },
     {
      "name": "payment_date",
      "type": "DATE",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "amount",
      "type": "DECIMAL(14,2)",
      "null": false,
      "pk": false,
      "fk": null
     },
     {
      "name": "method",
      "type": "VARCHAR(50)",
      "null": false,
      "pk": false,
      "fk": null
     }
    ]
   }
  ],
  "queries": [
   {
    "title": "1. All habitable planets, nearest first",
    "sql": "SELECT name, star_system, distance_ly, gravity_g, population\nFROM t_planet\nWHERE habitable = TRUE\nORDER BY distance_ly, name"
   },
   {
    "title": "2. INNER JOIN: employees who are also investors",
    "sql": "SELECT e.first_name, e.last_name, e.job_title, i.shares, c.acronym AS company\nFROM t_employee e\nINNER JOIN t_investor i ON i.employee_id = e.id\nINNER JOIN t_company c ON c.id = i.company_id\nORDER BY i.shares DESC"
   },
   {
    "title": "3. LEFT JOIN: shares per employee (0 if not investing)",
    "sql": "SELECT e.id, e.first_name, e.last_name, COALESCE(SUM(i.shares), 0) AS shares\nFROM t_employee e\nLEFT JOIN t_investor i ON i.employee_id = e.id\nGROUP BY e.id, e.first_name, e.last_name\nORDER BY shares DESC, e.id"
   },
   {
    "title": "4. Self-join: every employee with their manager",
    "sql": "SELECT emp.first_name AS employee, emp.job_title, mgr.first_name AS manager\nFROM t_employee emp\nLEFT JOIN t_employee mgr ON emp.manager_id = mgr.id\nORDER BY mgr.id, emp.id"
   },
   {
    "title": "5. Unassigned phones and employees without a phone",
    "sql": "SELECT m.number, m.model, e.first_name AS employee\nFROM t_mobile m\nLEFT JOIN t_employee e ON e.id = m.employee_id\nWHERE e.id IS NULL\nUNION ALL\nSELECT NULL, NULL, e.first_name\nFROM t_employee e\nWHERE e.id NOT IN (SELECT employee_id FROM t_mobile WHERE employee_id IS NOT NULL)"
   },
   {
    "title": "6. Revenue by product line",
    "sql": "SELECT l.name AS product_line,\n       COUNT(DISTINCT ol.order_id) AS orders,\n       SUM(ol.quantity) AS units,\n       ROUND(SUM(ol.quantity * ol.unit_price * (1 - ol.discount_pct / 100.0)), 2) AS revenue_gc\nFROM t_product_line l\nLEFT JOIN t_product p ON p.product_line_id = l.id\nLEFT JOIN t_order_line ol ON ol.product_id = p.id\nGROUP BY l.id, l.name\nORDER BY revenue_gc DESC"
   },
   {
    "title": "7. Top 5 customers by amount paid (net of refunds)",
    "sql": "SELECT c.first_name, c.last_name, c.species, ROUND(SUM(py.amount), 2) AS paid_gc\nFROM t_customer c\nJOIN t_order o ON o.customer_id = c.id\nJOIN t_payment py ON py.order_id = o.id\nGROUP BY c.id, c.first_name, c.last_name, c.species\nORDER BY paid_gc DESC\nLIMIT 5"
   },
   {
    "title": "8. Delivered orders with outstanding debt",
    "sql": "SELECT o.id, o.order_date, c.first_name AS customer, t.total, COALESCE(py.paid, 0) AS paid,\n       ROUND(t.total - COALESCE(py.paid, 0), 2) AS outstanding\nFROM t_order o\nJOIN t_customer c ON c.id = o.customer_id\nJOIN (SELECT order_id, ROUND(SUM(quantity * unit_price * (1 - discount_pct / 100.0)), 2) AS total\n      FROM t_order_line GROUP BY order_id) t ON t.order_id = o.id\nLEFT JOIN (SELECT order_id, SUM(amount) AS paid FROM t_payment GROUP BY order_id) py ON py.order_id = o.id\nWHERE o.status = 'Delivered' AND t.total - COALESCE(py.paid, 0) > 0.01\nORDER BY outstanding DESC"
   },
   {
    "title": "9. Products that have never been sold",
    "sql": "SELECT p.id, p.name, p.stock\nFROM t_product p\nWHERE NOT EXISTS (SELECT 1 FROM t_order_line ol WHERE ol.product_id = p.id)"
   },
   {
    "title": "10. Manufacturing cost vs. price (margin) per product",
    "sql": "SELECT p.name, p.price, ROUND(SUM(pp.quantity * pc.cost), 2) AS parts_cost,\n       ROUND(p.price - SUM(pp.quantity * pc.cost), 2) AS margin\nFROM t_product p\nJOIN t_product_piece pp ON pp.product_id = p.id\nJOIN t_piece pc ON pc.id = pp.piece_id\nGROUP BY p.id, p.name, p.price\nORDER BY margin"
   },
   {
    "title": "11. Projects with lead, headcount and weekly hours",
    "sql": "SELECT pr.name AS project, pr.area, pr.status, l.first_name AS lead,\n       COUNT(a.employee_id) AS people, COALESCE(SUM(a.weekly_hours), 0) AS weekly_hours\nFROM t_project pr\nLEFT JOIN t_employee l ON l.id = pr.lead_employee_id\nLEFT JOIN t_assignment a ON a.project_id = pr.id\nGROUP BY pr.id, pr.name, pr.area, pr.status, l.first_name\nORDER BY weekly_hours DESC"
   },
   {
    "title": "12. Patients by project and status",
    "sql": "SELECT COALESCE(pr.name, '(no project)') AS project, pa.status, COUNT(*) AS patients\nFROM t_patient pa\nLEFT JOIN t_project pr ON pr.id = pa.project_id\nGROUP BY pr.name, pa.status\nORDER BY project, patients DESC"
   },
   {
    "title": "13. Subscribers who are employees, customers or neither (match by email)",
    "sql": "SELECT s.email, s.newsletter,\n       CASE WHEN e.id IS NOT NULL THEN 'Employee'\n            WHEN c.id IS NOT NULL THEN 'Customer'\n            ELSE 'Unknown' END AS kind\nFROM t_subscriber s\nLEFT JOIN t_employee e ON e.email = s.email\nLEFT JOIN t_customer c ON c.email = s.email\nORDER BY kind, s.email"
   },
   {
    "title": "14. Monthly sales and running total (window functions)",
    "sql": "SELECT month, sales_gc, ROUND(SUM(sales_gc) OVER (ORDER BY month), 2) AS running_total_gc\nFROM (\n  SELECT SUBSTR(o.order_date, 1, 7) AS month,\n         ROUND(SUM(ol.quantity * ol.unit_price * (1 - ol.discount_pct / 100.0)), 2) AS sales_gc\n  FROM t_order o\n  JOIN t_order_line ol ON ol.order_id = o.id\n  WHERE o.status <> 'Cancelled'\n  GROUP BY SUBSTR(o.order_date, 1, 7)\n) m\nORDER BY month"
   },
   {
    "title": "15. Sales rep ranking by revenue",
    "sql": "SELECT COALESCE(e.first_name, '(web)') AS sales_rep, COUNT(DISTINCT o.id) AS orders,\n       ROUND(SUM(ol.quantity * ol.unit_price * (1 - ol.discount_pct / 100.0)), 2) AS revenue_gc,\n       RANK() OVER (ORDER BY SUM(ol.quantity * ol.unit_price * (1 - ol.discount_pct / 100.0)) DESC) AS position\nFROM t_order o\nJOIN t_order_line ol ON ol.order_id = o.id\nLEFT JOIN t_employee e ON e.id = o.employee_id\nGROUP BY e.id, e.first_name"
   }
  ]
 }
};
