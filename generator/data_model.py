# -*- coding: utf-8 -*-
"""
GenBit dataset — data model and hand-written seed data (ES / EN).

Every translatable value is written as a tuple ("español", "english").
Column definitions: (key_en, name_es, type, nullable, extra)
  type: int | bigint | str:N | dec:P,S | date | bool | text
  extra: "pk" | ("fk", table_key, column_key) | None
"""

T = lambda es, en: (es, en)  # noqa: E731  (readability helper)

# ---------------------------------------------------------------------------
# Static catalogues
# ---------------------------------------------------------------------------

PLANETS = [
    # id, name, star system, type, distance (ly), gravity (g), population, habitable
    (1, T("Tierra", "Earth"), "Sol", T("Planeta rocoso", "Rocky planet"), 0.00, 1.00, 9_800_000_000, True),
    (2, T("Luna", "Moon"), "Sol", T("Luna", "Moon"), 0.00, 0.17, 2_400_000, True),
    (3, T("Marte", "Mars"), "Sol", T("Planeta rocoso", "Rocky planet"), 0.00, 0.38, 48_000_000, True),
    (4, T("Europa", "Europa"), "Sol", T("Luna helada", "Icy moon"), 0.00, 0.13, 310_000, False),
    (5, T("Titán", "Titan"), "Sol", T("Luna helada", "Icy moon"), 0.00, 0.14, 1_150_000, False),
    (6, T("Ganímedes", "Ganymede"), "Sol", T("Luna helada", "Icy moon"), 0.00, 0.15, 640_000, False),
    (7, T("Ceres", "Ceres"), "Sol", T("Planeta enano", "Dwarf planet"), 0.00, 0.03, 95_000, False),
    (8, T("Estación Lagrange L5", "Lagrange L5 Station"), "Sol", T("Estación orbital", "Orbital station"), 0.00, 1.00, 72_000, True),
    (9, T("Próxima b", "Proxima b"), "Alfa Centauri", T("Planeta rocoso", "Rocky planet"), 4.24, 1.10, 3_200_000, True),
    (10, T("TRAPPIST-1e", "TRAPPIST-1e"), "TRAPPIST-1", T("Planeta oceánico", "Ocean planet"), 40.66, 0.93, 410_000, True),
    (11, T("Kepler-442b", "Kepler-442b"), "Kepler-442", T("Supertierra", "Super-Earth"), 1206.00, 1.30, 0, True),
    (12, T("Tau Ceti f", "Tau Ceti f"), "Tau Ceti", T("Supertierra", "Super-Earth"), 11.91, 1.70, 18_000, False),
    (13, T("Gliese 667 Cc", "Gliese 667 Cc"), "Gliese 667", T("Supertierra", "Super-Earth"), 23.62, 1.50, 5_600, False),
    (14, T("Nueva Aurora", "New Aurora"), "Kepler-186", T("Planeta rocoso", "Rocky planet"), 582.20, 0.89, 0, True),
]

# acronym, name, sector, hq planet, founded, parent company id, employees
COMPANIES = [
    (1, "GB", "GenBit Corporation", T("Conglomerado científico", "Scientific conglomerate"), 1, 2142, None, 52000),
    (2, "AA", "Astro Alleles", T("Genética", "Genetics"), 3, 2151, 1, 1800),
    (3, "AE", "Antimatter Engineering", T("Energía", "Energy"), 2, 2149, 1, 4300),
    (4, "CRS", "Cryo-Regeneration Systems", T("Medicina", "Medicine"), 1, 2155, 1, 950),
    (5, "EAF", "Exo-Agriculture Foundation", T("Astrobiología", "Astrobiology"), 3, 2160, None, 610),
    (6, "EN", "Entangled Networks", T("Física cuántica", "Quantum physics"), 1, 2147, 1, 7200),
    (7, "IA", "Interstellar Analytics", T("Datos y computación", "Data & computing"), 8, 2163, None, 380),
    (8, "IASP", "Institute for Advanced Spin Physics", T("Física cuántica", "Quantum physics"), 1, 2139, None, 1200),
    (9, "OPIS", "Orbital Proteomics & Imaging Systems", T("Biotecnología", "Biotechnology"), 8, 2166, 1, 540),
    (10, "PETRL", "Planetary Embryo & Tissue Research Lab", T("Medicina", "Medicine"), 9, 2171, 1, 290),
    (11, "QRI", "Quantum Resonance Institute", T("Neurociencia", "Neuroscience"), 1, 2158, None, 160),
    (12, "RS", "Replicator Solutions", T("Fabricación", "Manufacturing"), 7, 2152, 1, 3100),
    (13, "SFE", "Stellar Fusion Energy", T("Energía", "Energy"), 5, 2145, None, 8800),
    (14, "SR", "Synthetic Ribosomes", T("Genética", "Genetics"), 3, 2168, 1, 720),
    (15, "TFOI", "Terraforming & Ocean Initiatives", T("Terraformación", "Terraforming"), 3, 2150, 1, 5600),
    (16, "TNF", "Tachyon Navigation Foundry", T("Propulsión", "Propulsion"), 2, 2161, 1, 2050),
    (17, "WS", "Wormhole Shipping", T("Logística", "Logistics"), 9, 2170, None, 11900),
]

# name, company, planet, city, capacity, opening date
OFFICES = [
    (1, T("Sede central", "Headquarters"), 1, 1, "Ginebra", 4000, "2142-03-01"),
    (2, T("Laboratorio orbital", "Orbital lab"), 1, 8, "Anillo B", 350, "2158-06-15"),
    (3, T("Campus Olympus", "Olympus Campus"), 2, 3, "Olympus Mons", 900, "2152-01-10"),
    (4, T("Planta de antimateria", "Antimatter plant"), 3, 2, "Cráter Shackleton", 600, "2150-09-20"),
    (5, T("Clínica criogénica", "Cryogenic clinic"), 4, 1, "Reikiavik", 220, "2156-02-02"),
    (6, T("Invernadero Valles", "Valles Greenhouse"), 5, 3, "Valles Marineris", 180, "2161-04-30"),
    (7, T("Nodo cuántico", "Quantum node"), 6, 1, "Tokio", 1500, "2148-11-11"),
    (8, T("Observatorio de datos", "Data observatory"), 7, 8, "Anillo C", 120, "2164-07-07"),
    (9, T("Laboratorio de espín", "Spin lab"), 8, 1, "Zúrich", 400, "2140-05-05"),
    (10, T("Estación de imagen", "Imaging station"), 9, 8, "Anillo A", 160, "2167-03-03"),
    (11, T("Biobanco Próxima", "Proxima biobank"), 10, 9, "Puerto Centauri", 90, "2172-08-18"),
    (12, T("Instituto de resonancia", "Resonance institute"), 11, 1, "Barcelona", 140, "2158-10-01"),
    (13, T("Fábrica de replicadores", "Replicator factory"), 12, 7, "Occator", 1300, "2153-12-12"),
    (14, T("Reactor Kraken", "Kraken reactor"), 13, 5, "Kraken Mare", 700, "2146-01-20"),
    (15, T("Laboratorio de ribosomas", "Ribosome lab"), 14, 3, "Ciudad Bradbury", 210, "2169-02-14"),
    (16, T("Base oceánica", "Ocean base"), 15, 4, "Conamara Chaos", 260, "2162-06-21"),
    (17, T("Astillero taquiónico", "Tachyon shipyard"), 16, 2, "Base Armstrong", 800, "2162-09-09"),
    (18, T("Terminal de agujeros de gusano", "Wormhole terminal"), 17, 9, "Puerto Centauri", 2500, "2171-01-01"),
    (19, T("Oficina de ventas Ganímedes", "Ganymede sales office"), 1, 6, "Nueva Galilea", 45, "2175-05-25"),
    (20, T("Puesto avanzado TRAPPIST", "TRAPPIST outpost"), 1, 10, "Arrecife Uno", 30, "2181-07-04"),
]

# first name, last name, job title, department, office, manager, hire date, salary
EMPLOYEES = [
    (1, "Thomas", "Matzinger", T("Director general", "Chief Executive Officer"), T("Dirección", "Executive"), 1, None, "2160-01-15", 480000),
    (2, "Olé", "Martínez Möen", T("Dirección científica", "Chief Science Officer"), T("Dirección", "Executive"), 1, 1, "2161-03-01", 390000),
    (3, "David", "Peace", T("Director comercial", "Chief Sales Officer"), T("Ventas", "Sales"), 1, 1, "2163-07-12", 350000),
    (4, "Tobias", "Lenaert", T("Genetista sénior", "Senior Geneticist"), T("Genética", "Genetics"), 3, 2, "2165-02-20", 210000),
    (5, "Jonathan", "Laighton", T("Físico cuántico", "Quantum Physicist"), T("Física cuántica", "Quantum physics"), 7, 2, "2166-09-05", 205000),
    (6, "Jamie", "Maierfeld", T("Investigador/a en neurociencia", "Neuroscientist"), T("Neurociencia", "Neuroscience"), 12, 2, "2168-04-18", 198000),
    (7, "Peter", "Singers", T("Responsable de ética", "Head of Ethics"), T("Ética", "Ethics"), 1, 1, "2162-11-30", 260000),
    (8, "Michael", "St. Yulés", T("Ingeniero de propulsión", "Propulsion Engineer"), T("Ingeniería", "Engineering"), 17, 2, "2169-06-01", 185000),
    (9, "Brian", "Thomasik", T("Analista de sufrimiento salvaje", "Wild Suffering Analyst"), T("Ética", "Ethics"), 1, 7, "2170-01-10", 142000),
    (10, "Stijn", "Bruwèrs", T("Vendedor interplanetario", "Interplanetary Sales Rep"), T("Ventas", "Sales"), 19, 3, "2171-08-22", 98000),
    (11, "Mark", "Spark", T("Vendedor interplanetario", "Interplanetary Sales Rep"), T("Ventas", "Sales"), 3, 3, "2172-03-14", 96000),
    (12, "Ada", "Quintero", T("Ingeniera de qubits", "Qubit Engineer"), T("Física cuántica", "Quantum physics"), 9, 5, "2174-05-02", 154000),
    (13, "Yuki", "Tanabe", T("Bioinformática", "Bioinformatician"), T("Genética", "Genetics"), 2, 4, "2175-10-19", 131000),
    (14, "Nia", "Okonkwo", T("Médica de ensayos clínicos", "Clinical Trial Physician"), T("Medicina", "Medicine"), 5, 2, "2173-12-01", 176000),
    (15, "Rafael", "Domínguez Sol", T("Terraformador", "Terraformer"), T("Terraformación", "Terraforming"), 6, 2, "2176-02-27", 127000),
    (16, "Lena", "Voss", T("Vendedora interplanetaria", "Interplanetary Sales Rep"), T("Ventas", "Sales"), 2, 3, "2177-07-07", 92000),
    (17, "Kai", "Moreno", T("Técnico de criogenia", "Cryogenics Technician"), T("Medicina", "Medicine"), 5, 14, "2178-01-03", 74000),
    (18, "Priya", "Raman", T("Astrofísica", "Astrophysicist"), T("Astrofísica", "Astrophysics"), 18, 2, "2178-09-15", 149000),
    (19, "Zeta-7", "", T("Asistente de laboratorio sintético", "Synthetic Lab Assistant"), T("Genética", "Genetics"), 3, 4, "2180-04-01", 0),
    (20, "Ilse", "Brandt", T("Vendedora interplanetaria", "Interplanetary Sales Rep"), T("Ventas", "Sales"), 20, 3, "2181-07-10", 88000),
    (21, "Omar", "Haddad", T("Becario de física", "Physics Intern"), T("Física cuántica", "Quantum physics"), None, 5, "2186-09-01", 31000),
]

# number, PUK, model, carrier, employee
MOBILES = [
    ("666111000", "34565465", "Q-Phone 12", "Orbitel", 1),
    ("123456789", "54676767", "Nebula Fold", "Marsnet", 3),
    ("666111222", "45675675", "Q-Phone 12", "Orbitel", 3),
    ("666000555", "77812390", "Kepler Mini", "Lunacom", 5),
    ("666222333", "11223344", "Holofón X", "Orbitel", 10),
    ("666222444", "99881122", "Holofón X", "Marsnet", 11),
    ("666222555", "55667788", "Nebula Fold", "Centauri Mobile", 16),
    ("666222666", "33445566", "Kepler Mini", "Orbitel", 20),
    ("666333000", "45675678", "Q-Phone 12", "Lunacom", None),
    ("666333111", "90909090", "Holofón X", "Orbitel", None),
    ("666444777", "12121212", "Q-Phone 13 Pro", "Orbitel", 2),
    ("666444888", "65656565", "Kepler Mini", "Marsnet", 14),
    ("666555999", "78787878", "Nebula Fold", "Centauri Mobile", 18),
]

SPECIES = {
    "human": T("Humano", "Human"),
    "europan": T("Cefalópodo europano", "Europan cephalopod"),
    "silicoid": T("Silicoide", "Silicoid"),
    "synthetic": T("Sintético", "Synthetic"),
    "taucetian": T("Insectoide de Tau Ceti", "Tau Cetian insectoid"),
    "cloud": T("Nube consciente", "Sentient cloud"),
}

TIERS = [T("Bronce", "Bronze"), T("Plata", "Silver"), T("Oro", "Gold"), T("Platino", "Platinum")]

# first, last, species, email, planet, company, register date, tier
CUSTOMERS = [
    (1, "Simon", "Knutsön", "human", "simon.knutson@orbitmail.se", 1, None, "2180-02-11", 2),
    (2, "Magnus", "Winding", "human", "mwinding@marsnet.mr", 3, 15, "2180-05-30", 3),
    (3, "Jean-Christophe", "Laurenbaum", "human", "jc.laurenbaum@lunacom.mn", 2, None, "2181-01-19", 1),
    (4, "Axelle", "Playoust-Brâure", "human", "axelle.pb@orbitmail.fr", 1, 5, "2181-03-03", 2),
    (5, "Jack", "Rese", "human", None, 8, None, "2181-06-21", 0),
    (6, "Suzan", "Schnëider", "human", "suzan.schneider@orbitmail.de", 1, None, "2181-11-08", 1),
    (7, "Ronald", "Änderson", "human", "ronald.anderson@titan.net", 5, 13, "2182-01-14", 3),
    (8, "Tobias", "Bauman", "human", "tobias.bauman@orbitmail.de", 1, None, "2182-04-02", 0),
    (9, "Vlastimill", "Vohánka", "human", "vlasta@ceres.coop", 7, 12, "2182-07-27", 2),
    (10, "Oliver", "Bertrand", "human", "oliver.bertrand@proxima.ac", 9, 10, "2182-10-10", 1),
    (11, "Seraphine", "Duval", "human", "seraphine.duval@orbitmail.fr", 1, None, "2183-01-05", 0),
    (12, "Kwame", "Asante", "human", "kwame.asante@lagrange.st", 8, 7, "2183-02-17", 2),
    (13, "Mei Lin", "Zhao", "human", "meilin.zhao@marsnet.mr", 3, 2, "2183-04-22", 3),
    (14, "Lucía", "Ferrer", "human", "lucia.ferrer@orbitmail.es", 1, None, "2183-06-09", 1),
    (15, "Dmitri", "Volkov", "human", "d.volkov@ganymede.gal", 6, None, "2183-08-30", 0),
    (16, "Hugo", "Lindqvist", "human", "hugo.lindqvist@orbitmail.se", 1, 8, "2183-11-12", 2),
    (17, "Fátima Zahra", "Benali", "human", "fz.benali@lunacom.mn", 2, 3, "2184-01-25", 1),
    (18, "Tomás", "Iriarte", "human", None, 3, None, "2184-03-14", 0),
    (19, "Ingrid", "Solberg", "human", "ingrid.solberg@europa.ice", 4, 15, "2184-05-05", 2),
    (20, "Kenji", "Arakawa", "human", "kenji.arakawa@orbitmail.jp", 1, 6, "2184-07-19", 3),
    (21, "Valentina", "Greco", "human", "valentina.greco@titan.net", 5, None, "2184-09-02", 1),
    (22, "Zorblax", "Qin", "silicoid", "zorblax@ceres.coop", 7, None, "2185-01-30", 2),
    (23, "Vael", "Thorassi", "taucetian", "vael.thorassi@tauceti.hive", 12, None, "2185-03-11", 1),
    (24, "Krrr'tik", None, "taucetian", None, 12, None, "2185-06-06", 0),
    (25, "Oomu", "Paal", "europan", "oomu.paal@europa.ice", 4, 15, "2185-08-08", 3),
    (26, "Nyx", "Arvandi", "cloud", "nyx@trappist.sea", 10, None, "2185-10-31", 2),
    (27, "HAL-0", None, "synthetic", "hal0@lagrange.st", 8, 7, "2186-02-14", 1),
    (28, "Ilunga", "Mbeki", "human", "ilunga.mbeki@proxima.ac", 9, None, "2186-05-20", 0),
    (29, "Ana", "Sokolova", "human", "ana.sokolova@ganymede.gal", 6, None, "2186-09-09", 1),
    (30, "Glorp", "Vexx", "silicoid", "glorp.vexx@gliese.rock", 13, None, "2187-01-01", 0),
]

# first, last, business name, specialty, planet, rating, email
SUPPLIERS = [
    (1, "Jonathan", "Byrch", "Byrch Cryogenics Ltd.", T("Criogenia", "Cryogenics"), 1, 4.6, "jbyrch@byrchcryo.com"),
    (2, "Axelle", "Playdust-Brâure", "Poussière d'Étoiles SARL", T("Metamateriales", "Metamaterials"), 1, 4.1, "axelle@poussiere.fr"),
    (3, "Ian", "Wilkinson", "Wilkinson Quantum Parts", T("Componentes cuánticos", "Quantum components"), 8, 4.8, "ian@wqp.st"),
    (4, "Catia", "Fairia", "Fairia Biologicals", T("Reactivos biológicos", "Biological reagents"), 3, 3.9, "catia@fairiabio.mr"),
    (5, "Dorothea", "Krenz", "Ceres Mining Collective", T("Minería de asteroides", "Asteroid mining"), 7, 3.5, "dkrenz@ceresmining.coop"),
    (6, "Oluwaseun", "Adeyemi", "Adeyemi Plasma Works", T("Plasma y energía", "Plasma & energy"), 5, 4.3, "seun@plasmaworks.tt"),
    (7, "Mara", "Lindgren", "Graphene Gardens", T("Grafeno", "Graphene"), 2, 4.0, "mara@graphenegardens.mn"),
    (8, "Xith", "Ul-Morrow", "Tau Ceti Hive Supplies", T("Bioingeniería", "Bioengineering"), 12, 2.7, None),
    (9, "Pedro", "Almagro", "Almagro Nanosistemas", T("Nanotecnología", "Nanotechnology"), 1, 4.5, "pedro@almagronano.es"),
    (10, "Sven", "Haraldsen", "Haraldsen Neurolinks", T("Neurotecnología", "Neurotechnology"), 1, 4.2, "sven@neurolinks.no"),
]

# first, last, employee (if also employee), company invested in, shares, date
INVESTORS = [
    (1, "Paul", "Yngraham", None, 1, 120000, "2170-04-01"),
    (2, "Jaime", "Woodhouse", None, 6, 45000, "2172-06-15"),
    (3, "Tobias", "Bawmann", None, 15, 30000, "2175-09-09"),
    (4, "Klat", "Ros Kirdan", None, 17, 88000, "2176-02-20"),
    (5, "Iain", "Wilkinson", None, 12, 15000, "2178-11-30"),
    (6, "Thomas", "Matzinger", 1, 1, 280000, "2160-01-15"),
    (7, "Olé", "Martínez Möen", 2, 1, 120000, "2161-03-01"),
    (8, "David", "Peace", 3, 1, 30000, "2164-01-01"),
    (9, "Peter", "Singers", 7, 5, 25000, "2165-05-05"),
    (10, "Jamie", "Maierfeld", 6, 11, 8800, "2170-07-07"),
    (11, "Ada", "Quintero", 12, 8, 5500, "2179-03-03"),
    (12, "Brian", "Thomasik", 9, 5, 12000, "2176-08-08"),
    (13, "Zorblax", "Qin", None, 12, 400, "2186-01-01"),
    (14, "Oomu", "Paal", None, 15, 13000, "2186-06-30"),
    (15, "Marina", "Okafor", None, 13, 2500, "2187-02-02"),
]

PROJECT_STATUS = {
    "active": T("Activo", "Active"),
    "done": T("Finalizado", "Completed"),
    "paused": T("En pausa", "On hold"),
    "planned": T("Planificado", "Planned"),
    "cancelled": T("Cancelado", "Cancelled"),
}

# name, area, company, leader, start, end, budget, status
PROJECTS = [
    (1, T("Conteo de neuronas", "Neuron Counting"), T("Neurociencia", "Neuroscience"), 11, 6, "2179-01-10", None, 4_200_000, "active"),
    (2, T("Reprogramación celular", "Cell Reprogramming"), T("Genética", "Genetics"), 14, 4, "2177-05-01", None, 12_500_000, "active"),
    (3, T("Teletransporte cuántico", "Quantum Teleportation"), T("Física cuántica", "Quantum physics"), 6, 5, "2172-02-14", "2184-12-20", 88_000_000, "done"),
    (4, T("Edición genética CRISPR-Ω", "CRISPR-Ω Gene Editing"), T("Genética", "Genetics"), 2, 4, "2174-09-09", "2182-06-30", 23_000_000, "done"),
    (5, T("Terraformación de Marte", "Mars Terraforming"), T("Astrobiología", "Astrobiology"), 15, 15, "2165-01-01", None, 950_000_000, "active"),
    (6, T("Ordenador cuántico topológico", "Topological Quantum Computer"), T("Física cuántica", "Quantum physics"), 8, 12, "2178-03-03", None, 61_000_000, "active"),
    (7, T("Motor de curvatura", "Warp Drive"), T("Astrofísica", "Astrophysics"), 16, 8, "2180-07-07", None, 420_000_000, "paused"),
    (8, T("Fotosíntesis artificial", "Artificial Photosynthesis"), T("Bioingeniería", "Bioengineering"), 5, 15, "2176-04-22", "2183-04-22", 9_700_000, "done"),
    (9, T("Criopreservación humana", "Human Cryopreservation"), T("Medicina", "Medicine"), 4, 14, "2175-11-11", None, 31_000_000, "active"),
    (10, T("Regeneración telomérica", "Telomere Regeneration"), T("Medicina", "Medicine"), 10, 14, "2181-02-02", None, 18_400_000, "active"),
    (11, T("Mapa del conectoma", "Connectome Map"), T("Neurociencia", "Neuroscience"), 9, 6, "2183-06-01", None, 7_300_000, "active"),
    (12, T("Atlas de agujeros de gusano", "Wormhole Atlas"), T("Astrofísica", "Astrophysics"), 17, 18, "2182-01-01", None, 140_000_000, "active"),
    (13, T("Reducción del sufrimiento salvaje", "Wild Suffering Reduction"), T("Ética", "Ethics"), 5, 9, "2184-03-15", None, 2_100_000, "active"),
    (14, T("Xenolingüística", "Xenolinguistics"), T("Neurociencia", "Neuroscience"), 7, None, "2189-01-01", None, 3_000_000, "planned"),
    (15, T("Tostadora de antimateria", "Antimatter Toaster"), T("Energía", "Energy"), 3, 5, "2181-01-01", "2181-03-01", 500_000, "cancelled"),
]

ROLES = [T("Investigador/a", "Researcher"), T("Ingeniero/a", "Engineer"), T("Analista", "Analyst"),
         T("Asesor/a", "Advisor"), T("Coordinador/a", "Coordinator")]

PATIENT_STATUS = [T("En tratamiento", "In treatment"), T("Observación", "Observation"),
                  T("Alta", "Discharged"), T("Criopreservado", "Cryopreserved")]

# first, last, birth date, species, blood type, planet, project, admission, status idx
PATIENTS = [
    (1, "Julio", "Cabrera", "2121-05-02", "human", "0+", 1, 9, "2180-01-12", 3),
    (2, "Lucius", "Caviola", "2156-09-14", "human", "A+", 1, 1, "2182-03-03", 0),
    (3, "Bruno", "Contestabile", "2140-02-28", "human", "B-", 9, 10, "2182-07-19", 0),
    (4, "Oscar", "Huerta", "2149-12-01", "human", "0-", 1, 2, "2181-11-11", 1),
    (5, "Michael", "Dello-Iacovo", "2160-06-06", "human", "AB+", 3, 1, "2183-02-02", 2),
    (6, "Michael Edward", "Johnson", "2158-03-17", "human", "A-", 1, 11, "2184-08-08", 0),
    (7, "Robert", "Daoust", "2130-10-10", "human", "0+", 2, 9, "2179-12-24", 3),
    (8, "Lukas", "Gloor", "2162-01-21", "human", "B+", 8, 10, "2185-05-05", 0),
    (9, "Andrés", "Gómez-Emilsson", "2161-07-30", "human", "A+", 1, 1, "2183-09-09", 1),
    (10, "Nely", "Watson", "2155-04-04", "human", "AB-", 3, 2, "2184-01-15", 0),
    (11, "Oomu", "Paal", "2090-01-01", "europan", None, 4, 2, "2186-06-30", 1),
    (12, "Teodora", "Ilić", "2170-11-11", "human", "0+", 3, 10, "2186-02-27", 0),
    (13, "Raúl", "Benítez", "2148-08-08", "human", "A+", 1, 9, "2185-12-12", 3),
    (14, "Grommk", "Ul", "2105-05-05", "silicoid", None, 7, 2, "2187-01-20", 1),
    (15, "Sofía", "Lindahl", "2172-02-02", "human", "B+", 9, 10, "2187-03-14", 0),
    (16, "Amara", "Nwosu", "2166-06-16", "human", "0-", 3, 1, "2187-05-05", 2),
    (17, "Haruto", "Mori", "2159-09-19", "human", "A-", 1, 11, "2187-08-01", 0),
    (18, "Elif", "Kaya", "2164-12-12", "human", "AB+", 8, None, "2188-01-10", 1),
    (19, "Krrr'tik", None, "2140-04-04", "taucetian", None, 12, 2, "2188-02-29", 0),
    (20, "Bea", "Montalbán", "2175-07-07", "human", "0+", 1, 10, "2188-04-04", 0),
]

NEWSLETTERS = [T("Genética", "Genetics"), T("Física cuántica", "Quantum physics"),
               T("Exploración espacial", "Space exploration"), T("Ofertas", "Deals"),
               T("Neurociencia", "Neuroscience")]

PRODUCT_LINES = [
    (1, T("Gadgets de defensa no letal", "Non-lethal defense gadgets"), T("Dispositivos para inmovilizar sin causar daño.", "Devices to immobilise without causing harm.")),
    (2, T("Dispositivos cuánticos", "Quantum devices"), T("Computación, comunicación y sensores cuánticos.", "Quantum computing, communication and sensing.")),
    (3, T("Biotecnología y genética", "Biotech & genetics"), T("Herramientas de edición y lectura genética.", "Tools to read and edit genomes.")),
    (4, T("Propulsión y navegación", "Propulsion & navigation"), T("Motores y sistemas de navegación interestelar.", "Engines and interstellar navigation systems.")),
    (5, T("Terraformación", "Terraforming"), T("Organismos y equipos para hacer habitables otros mundos.", "Organisms and equipment to make other worlds habitable.")),
    (6, T("Medicina regenerativa", "Regenerative medicine"), T("Reparación de tejidos, órganos y criogenia.", "Tissue and organ repair, cryogenics.")),
    (7, T("Neurotecnología", "Neurotech"), T("Interfaces y mediciones del cerebro.", "Brain interfaces and measurement.")),
    (8, T("Accesorios", "Accessories"), T("Línea creada para futuras novedades.", "Line reserved for future releases.")),
]

# name, line, project, price, stock, launch date, weight kg
PRODUCTS = [
    (1, T("Rayo congelador", "Freeze Ray"), 1, None, 1299.99, 140, "2178-02-01", 2.40),
    (2, T("Lanza piñas", "Pine Cone Launcher"), 1, None, 349.50, 610, "2179-06-15", 3.10),
    (3, T("Escudo de plasma de bolsillo", "Pocket Plasma Shield"), 1, None, 2499.00, 75, "2183-01-20", 0.80),
    (4, T("Red de gravedad cero", "Zero-G Capture Net"), 1, None, 189.90, 1200, "2180-10-10", 1.20),
    (5, T("Teletransportador de corto alcance", "Short-Range Teleporter"), 2, 3, 149999.00, 6, "2185-03-01", 340.00),
    (6, T("Ordenador cuántico de sobremesa", "Desktop Quantum Computer"), 2, 6, 38500.00, 22, "2184-09-09", 18.50),
    (7, T("Llavero de entrelazamiento (pareja)", "Entanglement Keychain (pair)"), 2, 3, 59.99, 4800, "2182-02-14", 0.05),
    (8, T("Generador de números verdaderamente aleatorios", "True Random Number Generator"), 2, None, 990.00, 300, "2177-07-07", 0.30),
    (9, T("Gafas de visión cuántica", "Quantum Vision Goggles"), 2, 6, 3150.00, 90, "2186-04-04", 0.25),
    (10, T("Kit CRISPR-Ω doméstico", "Home CRISPR-Ω Kit"), 3, 4, 899.00, 520, "2182-08-01", 1.50),
    (11, T("Secuenciador de ADN de mano", "Handheld DNA Sequencer"), 3, 4, 1599.00, 260, "2181-05-05", 0.45),
    (12, T("Mascota sintética (gato de Schrödinger)", "Synthetic Pet (Schrödinger's Cat)"), 3, 2, 4999.00, 40, "2186-12-24", 4.20),
    (13, T("Motor de curvatura compacto", "Compact Warp Drive"), 4, 7, 2500000.00, 2, "2188-01-01", 8200.00),
    (14, T("Brújula de agujeros de gusano", "Wormhole Compass"), 4, 12, 12800.00, 35, "2185-07-07", 1.10),
    (15, T("Velas solares de grafeno", "Graphene Solar Sails"), 4, None, 7600.00, 60, "2179-09-09", 25.00),
    (16, T("Semillas de musgo marciano", "Martian Moss Seeds"), 5, 5, 24.90, 25000, "2172-03-21", 0.10),
    (17, T("Bacterias fijadoras de nitrógeno para Titán", "Titan Nitrogen-Fixing Bacteria"), 5, 5, 310.00, 900, "2178-11-11", 0.50),
    (18, T("Paneles de fotosíntesis artificial", "Artificial Photosynthesis Panels"), 5, 8, 5400.00, 140, "2183-05-01", 40.00),
    (19, T("Parche de regeneración telomérica", "Telomere Regeneration Patch"), 6, 10, 780.00, 350, "2187-02-02", 0.02),
    (20, T("Cápsula de criosueño", "Cryosleep Pod"), 6, 9, 96000.00, 12, "2183-11-11", 650.00),
    (21, T("Riñón impreso en 3D", "3D-Printed Kidney"), 6, 2, 21000.00, 18, "2184-06-06", 0.30),
    (22, T("Nanobots reparadores (dosis)", "Repair Nanobots (dose)"), 6, 2, 1250.00, 700, "2185-10-10", 0.01),
    (23, T("Casco contador de neuronas", "Neuron-Counting Helmet"), 7, 1, 8900.00, 45, "2186-06-01", 1.80),
    (24, T("Interfaz cerebro-nube", "Brain-Cloud Interface"), 7, 11, 17500.00, 30, "2187-09-09", 0.15),
    (25, T("Traductor xenolingüístico", "Xenolinguistic Translator"), 7, None, 2200.00, 110, "2184-04-04", 0.20),
    (26, T("Tostadora de antimateria", "Antimatter Toaster"), 2, 15, 666.00, 0, "2181-03-01", 3.00),
]

# name, material, supplier, cost
PIECES = [
    (1, T("Cristal de cuarzo cuántico", "Quantum quartz crystal"), T("Cuarzo", "Quartz"), 3, 85.00),
    (2, T("Bobina superconductora", "Superconducting coil"), T("Niobio-titanio", "Niobium-titanium"), 3, 240.00),
    (3, T("Condensador de taquiones", "Tachyon capacitor"), T("Exótico", "Exotic"), 3, 3900.00),
    (4, T("Qubit topológico", "Topological qubit"), T("Semiconductor", "Semiconductor"), 3, 250.00),
    (5, T("Trampa de iones", "Ion trap"), T("Silicio", "Silicon"), 3, 650.00),
    (6, T("Chip criogénico", "Cryogenic chip"), T("Silicio", "Silicon"), 1, 310.00),
    (7, T("Carcasa de titanio", "Titanium casing"), T("Titanio", "Titanium"), 5, 45.00),
    (8, T("Lente de metamaterial", "Metamaterial lens"), T("Metamaterial", "Metamaterial"), 2, 190.00),
    (9, T("Batería de fusión fría", "Cold fusion battery"), T("Paladio", "Palladium"), 6, 520.00),
    (10, T("Emisor de plasma", "Plasma emitter"), T("Tungsteno", "Tungsten"), 6, 410.00),
    (11, T("Muelle de grafeno", "Graphene spring"), T("Grafeno", "Graphene"), 7, 12.00),
    (12, T("Cargador de piñas", "Pine cone magazine"), T("Madera reciclada", "Recycled wood"), 5, 6.50),
    (13, T("Nitrógeno líquido (litro)", "Liquid nitrogen (litre)"), T("Nitrógeno", "Nitrogen"), 1, 1.20),
    (14, T("Vector viral sintético", "Synthetic viral vector"), T("Biológico", "Biological"), 4, 95.00),
    (15, T("Enzima Cas-Ω", "Cas-Ω enzyme"), T("Biológico", "Biological"), 4, 60.00),
    (16, T("Cultivo de células madre", "Stem cell culture"), T("Biológico", "Biological"), 4, 480.00),
    (17, T("Biotinta", "Bio-ink"), T("Biológico", "Biological"), 8, 220.00),
    (18, T("Nanoensamblador", "Nano-assembler"), T("Carbono", "Carbon"), 9, 0.35),
    (19, T("Electrodo neuronal", "Neural electrode"), T("Platino-iridio", "Platinum-iridium"), 10, 140.00),
    (20, T("Sensor fotónico de neuronas", "Photonic neuron sensor"), T("Fotónico", "Photonic"), 10, 360.00),
    (21, T("Membrana de grafeno", "Graphene membrane"), T("Grafeno", "Graphene"), 7, 60.00),
    (22, T("Esporas de musgo", "Moss spores"), T("Biológico", "Biological"), 8, 0.10),
    (23, T("Generador de campo gravitatorio", "Gravity field generator"), T("Exótico", "Exotic"), 6, 2700.00),
    (24, T("Antena de entrelazamiento", "Entanglement antenna"), T("Semiconductor", "Semiconductor"), 3, 18.00),
    (25, T("Tornillo de unobtanio", "Unobtainium screw"), T("Unobtanio", "Unobtainium"), 5, 9999.00),
    (26, T("Núcleo de antimateria (1 ng)", "Antimatter core (1 ng)"), T("Antimateria", "Antimatter"), None, 15000.00),
]

# product -> [(piece, quantity)]
BOM = {
    1: [(13, 4), (6, 1), (7, 1), (9, 1)],
    2: [(11, 2), (12, 1), (7, 1)],
    3: [(10, 2), (9, 1), (8, 1)],
    4: [(11, 4), (21, 1)],
    5: [(3, 2), (4, 8), (24, 4), (7, 2), (9, 2)],
    6: [(4, 64), (6, 4), (2, 6), (13, 20), (7, 1)],
    7: [(24, 2)],
    8: [(1, 1), (6, 1)],
    9: [(8, 2), (4, 2), (9, 1)],
    10: [(15, 5), (14, 3)],
    11: [(5, 1), (6, 1), (7, 1)],
    12: [(16, 3), (18, 10), (4, 1)],
    13: [(3, 12), (23, 4), (9, 6), (7, 20), (2, 40)],
    14: [(23, 1), (1, 1), (8, 1)],
    15: [(21, 50)],
    16: [(22, 100)],
    17: [(14, 2)],
    18: [(21, 4), (16, 1)],
    19: [(16, 1), (17, 1)],
    20: [(13, 200), (6, 6), (7, 4), (9, 2)],
    21: [(17, 5), (16, 4)],
    22: [(18, 1000)],
    23: [(20, 8), (19, 32), (7, 1)],
    24: [(19, 64), (24, 2), (6, 1)],
    25: [(24, 1), (6, 1), (1, 1)],
    26: [(26, 1), (7, 1)],
}

ORDER_STATUS = {
    "delivered": T("Entregado", "Delivered"),
    "transit": T("En tránsito", "In transit"),
    "pending": T("Pendiente", "Pending"),
    "cancelled": T("Cancelado", "Cancelled"),
    "lost": T("Perdido en el hiperespacio", "Lost in hyperspace"),
}

PAYMENT_METHODS = [T("Créditos galácticos", "Galactic credits"), T("Transferencia cuántica", "Quantum transfer"),
                   T("Tarjeta interestelar", "Interstellar card"), T("Criptomoneda de antimateria", "Antimatter crypto"),
                   T("Trueque", "Barter")]
