# Vorpal: Business & Product Vision

## I. El Fundamento y la Visión

### 1.0 La Visión de Vorpal (Resumen Ejecutivo)

Vorpal no es una herramienta, es un ecosistema integrado diseñado para eliminar la fricción y la complejidad de la creación y gestión de juegos de rol de mesa (TTRPGs). Nuestra misión es potenciar la creatividad de jugadores, Directores de Juego (GMs) y creadores de mundos, proporcionando un conjunto de herramientas rápidas, flexibles e intuitivas que funcionan en perfecta sinergia.

El ecosistema se construye sobre tres pilares fundamentales:
1.  **Vorpal Player:** La ficha de personaje definitiva, diseñada para ser el portal de entrada para todos los jugadores.
2.  **Vorpal GM:** El centro de mando para dirigir partidas, enfocado en la gestión y la ejecución fluida del juego.
3.  **Vorpal Worldforge:** La forja creativa para construir mundos, sistemas y narrativas desde cero.

A través de un roadmap de desarrollo por fases, Vorpal evolucionará de un asistente de juego indispensable a una plataforma de creación completa, culminando en una mesa de juego virtual (VTT) y un motor de juego en solitario guiado por IA ("The Oracle Engine"). Nuestro modelo de negocio se basa en un Freemium justo, con suscripciones de valor añadido y un mercado que recompensa a la comunidad, posicionándonos para convertirnos en la solución esencial para una nueva generación de jugadores de rol.

### 2.0 El Problema del Mercado

El mercado de herramientas para TTRPGs está saturado, pero profundamente fragmentado y lleno de barreras de entrada. Los usuarios actuales se enfrentan a un ecosistema de soluciones imperfectas que les obligan a elegir entre potencia y simplicidad, o entre flexibilidad y facilidad de uso.

Identificamos cuatro categorías de competidores y sus debilidades inherentes:

#### 1. Los Titanes (Mesas Virtuales - VTTs)
*   **Ejemplos:** Roll20, Foundry VTT.
*   **Pain Points:**
    *   **Complejidad Abrumadora:** Su inmensa cantidad de funciones resulta en una curva de aprendizaje extremadamente alta, intimidante para nuevos usuarios.
    *   **Rendimiento Lento:** Suelen ser aplicaciones pesadas y recargadas que requieren una conexión a internet estable y un hardware decente.
    *   **Enfoque Online:** Están diseñadas para reemplazar la mesa física, no para mejorar la experiencia de juego en persona.

#### 2. Los Especialistas (Ecosistemas Cerrados)
*   **Ejemplos:** D&D Beyond.
*   **Pain Points:**
    *   **Cárcel Dorada:** Ofrecen una experiencia pulida pero están limitados a un único sistema de juego (D&D 5e), ignorando miles de otros TTRPGs.
    *   **Falta de Flexibilidad:** Los usuarios no pueden crear contenido propio (homebrew) de forma sencilla o adaptar la herramienta a reglas caseras sin soluciones improvisadas.

#### 3. Las Enciclopedias (Herramientas de World-Building)
*   **Ejemplos:** World Anvil.
*   **Pain Points:**
    *   **Parálisis por Análisis:** Son herramientas de escritura, no de gestión de juego. Su nivel de detalle es tan profundo que a menudo obstaculiza la preparación de la partida en lugar de agilizarla.
    *   **Complejidad de Uso en Partida:** No están diseñadas para una consulta rápida y ágil durante una sesión de juego.

#### 4. El Enfoque "Hágalo Usted Mismo" (Herramientas de Notas)
*   **Ejemplos:** Obsidian.md, Notion.
*   **Pain Points:**
    *   **Inversión de Tiempo Masiva:** Requieren que el usuario construya su propio sistema desde cero, investigando e instalando plugins y plantillas. La barrera de entrada no es monetaria, sino de tiempo y conocimiento técnico.
    *   **Falta de Funciones Específicas:** Carecen de herramientas nativas para TTRPGs, como lanzadores de dados integrados, seguimiento de iniciativa o gestión de inventario.

### 3.0 Nuestra Solución: La Filosofía Vorpal

Vorpal no compite en funciones, compite en filosofía. Nuestra ventaja competitiva se basa en cuatro pilares fundamentales diseñados para abordar directamente los "pain points" del mercado y ofrecer un valor único.

#### 1. Simplicidad Radical y Rapidez
Nuestra obsesión es la velocidad y la facilidad de uso. La interfaz será minimalista, intuitiva y responderá instantáneamente. Cada acción, desde actualizar la vida de un personaje hasta buscar un PNJ, está diseñada para completarse en el menor número de clics posible, manteniendo al usuario inmerso en la narrativa, no perdido en menús.

#### 2. Agnosticismo de Sistema por Diseño
Vorpal es universal. El corazón de la plataforma es un constructor modular de "bloques". Los usuarios no se ven forzados a usar una plantilla predefinida; construyen sus propias fichas y sistemas de forma visual e intuitiva. Esto nos abre a todo el mercado de TTRPGs, desde los más populares hasta los juegos indie más nicho.

#### 3. Cero Fricción ("Ready to Use")
Vorpal funciona desde el primer segundo. No hay instalaciones complejas, no hay que configurar bases de datos, no hay que buscar plugins. El usuario abre la aplicación web y empieza a crear. Ofrecemos la flexibilidad de las herramientas de notas sin la abrumadora carga de la configuración inicial.

#### 4. Offline-First y Centrado en la Mesa
Construido como una Aplicación Web Progresiva (PWA), Vorpal funciona perfectamente sin conexión a internet. Esto la convierte en la compañera digital ideal para la mesa de juego física, inmune a problemas de Wi-Fi. Nuestro enfoque no es reemplazar la mesa, sino potenciarla.


## II. Pilar 1: Vorpal Player - El Portal de Entrada

### 4.0 Propósito y Estrategia

Vorpal Player es el primer pilar del ecosistema y nuestro principal motor de adquisición de usuarios. El objetivo estratégico es crear la herramienta de gestión de personajes más potente, flexible y generosa del mercado en su versión gratuita. Al resolver los problemas clave de los jugadores de forma gratuita, establecemos confianza, construimos una base de usuarios masiva y creamos un embudo natural hacia los productos premium del ecosistema.

### 4.1 Producto Gratuito: La Promesa al Jugador

La versión gratuita de Vorpal Player debe ser un producto completo y satisfactorio por sí mismo, diseñado para ser superior a cualquier alternativa no especializada (PDFs editables, hojas de cálculo, notas de texto).

#### 4.1.1 Funcionalidades Clave Gratuitas:

*   **Creación de Personajes Locales Ilimitada:** Los usuarios pueden crear y almacenar un número ilimitado de personajes. Todos los datos se guardan directamente en el `localStorage` del navegador, garantizando privacidad, velocidad y funcionalidad offline completa. Esta generosidad es un diferenciador clave e inmediato.

*   **Constructor de Fichas Modular ("Sistema de Bloques"):** El núcleo de la flexibilidad de Vorpal. El usuario comienza con un lienzo en blanco y puede añadir, eliminar y reorganizar "bloques" predefinidos para construir la ficha perfecta para cualquier sistema de juego.
    *   **Bloques Disponibles:** Bloque de Estadísticas (ej. Fuerza, Destreza), Bloque de Atributos (ej. Salud, Maná, Puntos de Cordura), Lista de Habilidades, Inventario, Lista de Hechizos/Poderes, Notas, y más.

*   **Gestión Dinámica Esencial:** La ficha no es estática, es interactiva.
    *   **Inventario Consumible:** Los objetos pueden tener cantidades que se reducen con un solo clic. Un historial de acciones simple permite revertir usos accidentales.
    *   **Trackers de Estado:** Botones de alternancia para gestionar estados comunes (Concentración, Inspiración, Envenenado, etc.), permitiendo al jugador ver su estado actual de un vistazo.
    *   **Lanzador de Dados Integrado:** Un lanzador de dados universal (d4, d6, d8, d10, d12, d20, d100) siempre accesible.

*   **Importación y Exportación de Personajes:** Los usuarios pueden exportar sus personajes a un archivo de datos local (`.json`). Esto sirve como método de copia de seguridad y, crucialmente, como el mecanismo para compartir personajes con su GM antes de la implementación de la sincronización en tiempo real.

### 4.2 Plan de Monetización del Jugador (Evolutivo)

La monetización del jugador está diseñada para ser completamente opcional, ofreciendo mejoras de conveniencia, personalización y creatividad sin limitar nunca la funcionalidad principal de la herramienta gratuita.

#### 4.2.1 Fase 1: Suscripción "Vorpal Plus" (Conveniencia y Estética)

El primer nivel de la oferta de pago, enfocado en el jugador individual.
*   **Modelo:** Suscripción de bajo coste (ej. 2€/mes o 20€/año).
*   **Propuesta de Valor:** Mejora tu experiencia personal de juego.
*   **Funciones Desbloqueadas:**
    1.  **Sincronización en la Nube:** La función estrella. Permite al usuario crear una cuenta y sincronizar sus personajes entre múltiples dispositivos (PC, tablet, móvil).
    2.  **Biblioteca de Temas Visuales:** Desbloquea temas estéticos para la interfaz (pergamino, cyberpunk, grimorio, etc.).
    3.  **Biblioteca de Skins de Dados:** Desbloquea sets de dados cosméticos para el lanzador integrado.
    4.  **Crónica de Personaje Avanzada:** Un editor de texto enriquecido para el diario del personaje, permitiendo formateo avanzado, inserción de imágenes y organización por capítulos.

#### 4.2.2 Fase 2: Expansión Social y de Inmersión

A medida que la plataforma madura, el valor de "Vorpal Plus" aumenta al añadir funciones que mejoran la interacción del jugador con su grupo. Estas funciones se añaden a la suscripción existente sin coste adicional.
*   **Funciones Adicionales "Plus":**
    1.  **Mapa de Relaciones del Personaje:** Una herramienta visual privada para que el jugador trace su red de alianzas, rivalidades y contactos con PNJs.
    2.  **Gestión de Trasfondo Secreto:** Una sección encriptada en la ficha para notas que el jugador quiere mantener ocultas, incluso de su GM.
    3.  **Habilitación de Funciones de Grupo:** Permite al jugador Plus iniciar y gestionar herramientas colaborativas (como un inventario de grupo compartido) que pueden ser utilizadas por todos los miembros de la campaña, incluso los gratuitos.

#### 4.2.3 Fase 3: El Legado ("Salón de los Héroes")

Una nueva vía de ingresos que apela a la conexión emocional del jugador con sus historias.
*   **Modelo:** Compra única por personaje (ej. 4.99€).
*   **Propuesta de Valor:** Inmortaliza a tus héroes.
*   **Función:** Convierte una ficha de personaje retirada en una página de perfil conmemorativa, pública y compartible. Esta página muestra las estadísticas finales, el equipo, la crónica completa y una galería de arte, preservando el legado del personaje.

#### 4.2.4 Fase 4: La Creatividad ("Constructor de Playbooks")

La evolución final de "Vorpal Plus", que transforma al jugador de un gestor de personaje a un estratega eficiente.
*   **Función Adicional "Plus":**
    1.  **Constructor de "Playbooks":** Una herramienta avanzada que permite al usuario crear macros o secuencias de acciones personalizadas. Por ejemplo, un "Ataque Furtivo Completo" que agrupa una tirada de Sigilo, una tirada de ataque y las tiradas de daño correspondientes, todo ejecutable con un solo clic.

## III. Pilar 2: Vorpal GM - El Centro de Mando

### 5.0 Propósito y Estrategia

Vorpal GM es el segundo pilar del ecosistema, diseñado específicamente para el Director de Juego. Su propósito es transformar la ardua tarea de dirigir una partida en una experiencia fluida, organizada y creativa. Estratégicamente, este pilar es nuestro principal motor de monetización por suscripción. Apelamos directamente al usuario que más valora el ahorro de tiempo y las herramientas de gestión potentes. La sinergia con la base de usuarios gratuita de Vorpal Player es el gancho fundamental para la adopción de "GM Pro".

### 5.1 Producto Gratuito (Versión de Prueba)

La versión gratuita de Vorpal GM actúa como una demostración funcional, permitiendo al GM experimentar el poder de la plataforma en un entorno controlado antes de comprometerse. No es una solución a largo plazo, sino una prueba de concepto convincente.

#### 5.1.1 Funcionalidades y Limitaciones Clave:

*   **Gestión de UNA Campaña:** El GM puede crear y gestionar una única campaña activa a la vez.

*   **Límite de Jugadores:** Se puede invitar a un número limitado de jugadores a la campaña (ej. hasta 4 jugadores).

*   **Límite de Entradas en el Códice:** El GM puede crear un número limitado de entradas totales (ej. 25 entradas combinadas) para sus Personajes No Jugadores (PNJs), Lugares, Objetos y notas de Lore. El sistema de enlazado interno `[[wiki]]` es completamente funcional dentro de este límite.

*   **Sincronización en Tiempo Real (Limitada):** El GM puede conectar con las fichas de sus jugadores (incluso si estos usan la versión gratuita de Vorpal Player) y ver sus datos actualizados al instante. La limitación reside en la **persistencia y las funciones avanzadas**. Por ejemplo, el historial de cambios o el acceso a dashboards analíticos de la sesión estarían desactivados. La conexión existe para demostrar su poder, pero carece de las herramientas de gestión robustas del modo Pro.

### 5.2 Suscripción "GM Pro"

"GM Pro" es nuestro producto de suscripción premium. Su propuesta de valor es clara y directa: "Invierte en esta herramienta para ahorrar horas de preparación y dirigir partidas más dinámicas y memorables".

#### 5.2.1 Funcionalidades Clave de "GM Pro":

*   **Campañas y Jugadores Ilimitados:** Elimina todas las limitaciones de la versión gratuita. El GM puede dirigir tantas partidas como quiera con grupos de cualquier tamaño.

*   **Sincronización en Tiempo Real Completa y Robusta:** Esta es la *killer feature*.
    *   **Dashboard del GM:** El GM ve un panel de control con las estadísticas vitales de sus jugadores (Salud, Recursos, Estados) actualizadas al instante.
    *   **Interacción del GM:** El GM Pro desbloquea la capacidad de interactuar directamente con las fichas de los jugadores (con su permiso), como añadir un objeto a su inventario, aplicar daño o cambiar un estado.
    *   **Gestión Centralizada:** El GM Pro puede iniciar y gestionar herramientas de grupo como el inventario compartido, calendarios, etc., que son visibles para todos los jugadores.

*   **Códice de Campaña Ilimitado:** Creación ilimitada de PNJs, Lugares, Facciones, Objetos y Lore, todo interconectado con el sistema de enlazado `[[wiki]]`.

*   **Herramientas Avanzadas de Gestión de Sesión:**
    *   **Seguimiento de Iniciativa:** Un tracker de iniciativa visual e integrado que se vincula directamente a las fichas de jugadores y monstruos.
    *   **Constructor de Encuentros:** Una herramienta para preparar encuentros de combate, calculando niveles de dificultad y permitiendo al GM agrupar monstruos para una gestión rápida.
    *   **Notas de Sesión y Planificación:** Un espacio dedicado para planificar futuras sesiones, tomar notas durante la partida y llevar un registro del progreso de la campaña.

*   **Acceso al Arsenal Creativo (Generadores IA):**
    *   Acceso a una suite de generadores basados en IA para superar el bloqueo creativo, incluyendo:
        *   Generador de Nombres y Descripciones de PNJs.
        *   Generador de Ganchos de Misión y Rumores.
        *   Generador de Descripciones de Lugares y Ambientes.

### 5.3 La Sinergia Clave (El Embudo de Conversión)

El modelo de negocio de Vorpal GM se basa en una sinergia directa con Vorpal Player.
1.  **Adopción:** Un jugador descubre y ama Vorpal Player por su calidad y gratuidad.
2.  **Evangelización:** El jugador se lo recomienda a su grupo y a su GM como una forma de estandarizar las fichas de personaje.
3.  **Demostración de Valor:** El GM prueba la versión gratuita de Vorpal GM. Experimenta la magia de la sincronización en tiempo real, aunque de forma limitada, y reconoce su potencial inmediato.
4.  **Conversión:** Para desbloquear el verdadero poder de la gestión (interactuar con las fichas, usar herramientas de sesión avanzadas, dirigir más de una campaña), la decisión de suscribirse a "GM Pro" se convierte en un paso lógico para mejorar la calidad de juego para todo el grupo.

## IV. Pilar 3: Vorpal Worldforge - La Forja Creativa

### 6.0 Propósito y Estrategia

Vorpal Worldforge es el tercer pilar del ecosistema, diseñado como un conjunto de herramientas de creación estructurada para construir mundos, historias y sistemas de reglas desde cero. Su propósito estratégico es triple:
1.  **Expandir Nuestro Mercado:** Atraer a una audiencia adyacente que incluye escritores de ficción, diseñadores de juegos y aficionados a la creación de mundos (worldbuilding) que pueden no ser Directores de Juego activos.
2.  **Aumentar el Valor para los GMs Existentes:** Proporcionar a nuestra base de GMs herramientas de creación más profundas y organizadas que las simples notas de un códice de campaña.
3.  **Crear un Nuevo Flujo de Ingresos:** Introducir un modelo de monetización flexible que apela tanto a compras impulsivas como a suscripciones de alto valor.

La filosofía de Worldforge es reemplazar el "lienzo en blanco" de las wikis y las herramientas de notas con un sistema de "fichas" guiadas, transformando la abrumadora tarea de crear un mundo en un proceso manejable y modular.

### 6.1 Producto Gratuito (Versión de Prueba)

La versión gratuita de Worldforge permite a cualquier usuario experimentar el poder de la creación estructurada. Sirve como una potente herramienta de brainstorming y como la puerta de entrada al ecosistema de monetización.

#### 6.1.1 Funcionalidades y Limitaciones Clave:

*   **Un Proyecto de Mundo:** El usuario puede crear un único proyecto de mundo.
*   **Acceso a Todas las Plantillas de Ficha:** El usuario puede ver y utilizar todas las plantillas de creación disponibles (Ciudades, Facciones, Sistemas de Magia, etc.).
*   **Límite de Creación por Plantilla:** La limitación reside en la cantidad. El usuario puede crear un número limitado de "fichas" de cada tipo (ej. 1 Sistema de Magia, 3 Ciudades, 5 Facciones, 10 Personajes). Esto le permite esbozar las bases de su mundo y entender el valor de cada herramienta.
*   **Funcionalidad Completa de Enlazado:** El sistema de enlazado `[[wiki]]` funciona sin restricciones entre todas las fichas creadas, permitiendo al usuario experimentar el poder de una base de datos interconectada.

### 6.2 Modelo de Monetización Flexible

A diferencia de los otros pilares, Worldforge emplea un modelo híbrido que combina compras únicas (a la carta) con una suscripción premium, permitiendo al usuario pagar solo por lo que necesita o acceder a todo con un plan completo.

#### 6.2.1 Compras a la Carta ("Paquetes de Fichas")

Este modelo está diseñado para usuarios que tienen una necesidad específica o que prefieren poseer sus herramientas digitalmente. Al comprar un paquete, el usuario desbloquea permanentemente la creación ilimitada de las fichas incluidas en él.
*   **Modelo:** Pagos únicos por paquete temático.
*   **Ejemplos de Paquetes:**
    *   **Paquete "Arquitecto de Magia" (ej. 10€):** Creación ilimitada de Sistemas de Magia y Hechizos.
    *   **Paquete "Cartógrafo Urbano" (ej. 10€):** Creación ilimitada de Ciudades, Distritos y Puntos de Interés.
    *   **Paquete "Maestro de la Intriga" (ej. 10€):** Creación ilimitada de Facciones, Personajes Políticos y Conspiraciones.
    *   **Paquete "Cronista Divino" (ej. 10€):** Creación ilimitada de Dioses, Panteones y Mitos de Creación.
    *   ...y muchos más, permitiendo una expansión continua de la oferta.

#### 6.2.2 Suscripción "Worldforge Pro"

Diseñada para el creador de mundos serio, el escritor o el diseñador de juegos que necesita acceso sin restricciones a todo el arsenal creativo.
*   **Modelo:** Suscripción mensual/anual.
*   **Propuesta de Valor:** Desbloquea todo el potencial creativo de la plataforma.
*   **Funciones Desbloqueadas:**
    1.  **Acceso a Todos los Paquetes de Fichas:** Desbloquea la creación ilimitada de todas las plantillas de fichas, tanto existentes como las que se añadan en el futuro.
    2.  **Proyectos de Mundo Ilimitados:** Permite al usuario trabajar en múltiples mundos o versiones de un mismo mundo simultáneamente.
    3.  **Herramientas Avanzadas de Visualización:** Desbloquea herramientas como líneas de tiempo interactivas, mapas de relaciones entre facciones y jerarquías dinámicas.
    4.  **Exportación Avanzada:** Permite exportar el proyecto de mundo completo a formatos como PDF o Markdown para su uso externo.

#### 6.2.3 El "Vorpal Ultimate Bundle" (Suscripción Combinada)

El paquete de máximo valor, diseñado para el usuario más comprometido: el GM que también es un apasionado creador de mundos.
*   **Modelo:** Suscripción única que combina los productos Pro.
*   **Oferta:** Incluye **"GM Pro" + "Worldforge Pro"** con un descuento significativo sobre el precio de ambos por separado (ej. si cada uno cuesta 10€/mes, el bundle cuesta 15€/mes).
*   **Sinergia Estratégica:** Este bundle es la culminación de nuestro modelo. Permite a un GM construir su mundo con las herramientas detalladas de Worldforge y luego importar y usar sin problemas ese contenido (monstruos, PNJs, lugares) directamente en sus campañas de Vorpal GM.

## V. El Ecosistema y la Comunidad

### 7.0 La Sinergia del Ecosistema

Vorpal no es una colección de herramientas dispares, sino un ecosistema integrado donde el valor de cada pilar se ve amplificado por la existencia de los otros. Esta sinergia crea un "foso" competitivo y fomenta la retención de usuarios a largo plazo. El flujo de valor está diseñado para moverse fluidamente entre los tres pilares.

#### 7.1 El Flujo de Usuario: Del Jugador al Creador

1.  **Adquisición (Player):** Un nuevo usuario entra en el ecosistema a través de **Vorpal Player** debido a su potente oferta gratuita. Se convierte en la herramienta por defecto para gestionar su personaje.

2.  **Conversión a Grupo (GM):** El jugador introduce la herramienta a su grupo. El GM, al ver los beneficios de la estandarización, adopta **Vorpal GM** para gestionar la campaña, convirtiéndose en un cliente de suscripción ("GM Pro") para acceder a la sincronización en tiempo real y a las herramientas de gestión.

3.  **Conversión a Creación (Worldforge):** El GM, ahora inmerso en la plataforma, desea crear contenido más profundo y estructurado para sus campañas. Descubre **Vorpal Worldforge** como la solución perfecta para construir su mundo de forma organizada. Se convierte en un cliente de Worldforge (ya sea a través de la compra de paquetes o de la suscripción "Pro"), reemplazando sus viejos métodos de notas desorganizadas.

4.  **Retroalimentación (Ecosistema Completo):** El contenido creado en Worldforge (un monstruo, un PNJ, una ciudad) se puede importar sin problemas al Códice de **Vorpal GM** para ser utilizado en una partida en vivo con jugadores que usan **Vorpal Player**. El círculo se completa.

### 8.0 El Mercado de Creadores y "La Senda del Creador"

El Mercado es el corazón de la comunidad de Vorpal y una pieza central de nuestro modelo de negocio. Su propósito es transformar a los usuarios de consumidores pasivos a creadores activos, permitiéndoles monetizar su creatividad y enriquecer el ecosistema para todos los demás.

#### 8.1 Propósito y Tipos de Contenido

El Mercado permitirá a los usuarios vender activos digitales creados tanto dentro como fuera de la plataforma, compatibles con el ecosistema Vorpal.
*   **Contenido para Vorpal Player:**
    *   **Plantillas de Ficha de Personaje:** Para sistemas de juego de nicho.
    *   **Paquetes de Temas Visuales y Skins de Dados:** Creados por artistas de la comunidad.
*   **Contenido para Vorpal GM:**
    *   **Módulos de Aventura:** Aventuras "one-shot" o mini-campañas con PNJs, mapas y notas de trama pre-hechos.
    *   **Bestiarios y Colecciones de PNJs:** Paquetes de "monstruos" o personajes listos para ser importados en una campaña.
*   **Contenido para Vorpal Worldforge:**
    *   **Plantillas de Ficha de Creación:** Plantillas avanzadas para crear tipos de contenido muy específicos (ej. una plantilla para naves espaciales, una para organizaciones secretas).
    *   **"World-Kits":** Paquetes de contenido de mundo listos para usar (panteones de dioses, sistemas de magia, ciudades iniciales).
*   **Contenido para Futuras Evoluciones:**
    *   **Paquetes de Mapas y Tokens:** Para el Vorpal VTT.
    *   **Módulos para el "Oracle Engine":** Aventuras diseñadas para el juego en solitario con IA.

#### 8.2 El Sistema de Comisiones por Niveles: "La Senda del Creador"

Para posicionarnos como la plataforma más amigable para los creadores, implementaremos un sistema de comisiones dinámico que recompensa el éxito y la persistencia. Este sistema es una herramienta de marketing y retención en sí misma.

*   **Principio:** Todos los creadores comienzan con una comisión base del 20%. A medida que alcanzan hitos de ventas acumuladas (ingresos totales generados), su tasa de comisión se reduce permanentemente, permitiéndoles quedarse con una mayor parte de sus ganancias.

*   **La Estructura de 6 Niveles:**

    *   **Nivel 1: Aspirante**
        *   **Comisión:** 20%
        *   **Requisito:** Registrarse como creador.

    *   **Nivel 2: Artesano**
        *   **Comisión:** 18% (-2%)
        *   **Requisito:** Alcanzar **100€** en ventas totales.

    *   **Nivel 3: Maestro**
        *   **Comisión:** 16% (-2%)
        *   **Requisito:** Alcanzar **500€** en ventas totales.

    *   **Nivel 4: Forjador**
        *   **Comisión:** 14% (-2%)
        *   **Requisito:** Alcanzar **1.500€** en ventas totales.

    *   **Nivel 5: Augur**
        *   **Comisión:** 12% (-2%)
        *   **Requisito:** Alcanzar **4.000€** en ventas totales.

    *   **Nivel 6: Leyenda**
        *   **Comisión:** 10% (-2%)
        *   **Requisito:** Alcanzar **10.000€** en ventas totales.

## VI. El Plan de Despliegue Estratégico y la Visión a Largo Plazo

### 9.0 El Roadmap de Despliegue Fásico

El desarrollo de Vorpal se abordará como una secuencia de fases estratégicas. Cada fase se construye sobre el éxito de la anterior, permitiendo que el proyecto crezca de forma orgánica, valide sus hipótesis de mercado y genere valor (y potencialmente ingresos) antes de comprometer recursos en la siguiente etapa. Este enfoque es flexible y prioriza la construcción de un ecosistema sostenible.

#### Fase 1: La Fundación - Construir la Base de la Pirámide
*   **Foco Estratégico:** Adquisición de masa crítica y validación del producto principal.
*   **Productos a Lanzar:** **Vorpal Player** (Versión Gratuita y Suscripción "Plus").
*   **Racional Estratégico:**
    La base de cualquier ecosistema exitoso es su gente. Al comenzar con la mejor herramienta gratuita para el segmento de usuarios más grande (los jugadores), logramos tres objetivos cruciales: 1) Creamos nuestro motor de adquisición de usuarios. 2) Establecemos la marca Vorpal como sinónimo de calidad y facilidad de uso. 3) Construimos la base de la pirámide sobre la cual se apoyarán todas las futuras ofertas de monetización para GMs y Creadores. El éxito en esta fase no se mide en ingresos, sino en adopción y amor por el producto.
*   **Métricas Clave de Éxito:** Tasa de adopción, usuarios activos mensuales, feedback cualitativo de la comunidad.

#### Fase 2: La Viabilidad - Monetizar al Usuario Motivado
*   **Foco Estratégico:** Probar la viabilidad del modelo de negocio principal y establecer ingresos recurrentes.
*   **Productos a Lanzar:** **Vorpal GM** (Versión Gratuita de Prueba y Suscripción "GM Pro").
*   **Racional Estratégico:**
    El Director de Juego es el usuario con el "dolor" más agudo (falta de tiempo, complejidad de la gestión) y, por lo tanto, el más motivado para pagar por una solución. Esta fase se enfoca en convertir la base de usuarios de GMs que ya existe dentro de nuestra comunidad de jugadores. Al ofrecer una herramienta que les ahorra horas y mejora sus partidas (la sincronización en tiempo real), probamos que el mercado está dispuesto a pagar por valor. El éxito aquí valida todo el modelo de negocio.
*   **Métricas Clave de Éxito:** Tasa de conversión de GMs a "Pro", Ingreso Mensual Recurrente (MRR).

#### Fase 3: La Expansión - Crear el Efecto de Red
*   **Foco Estratégico:** Expandir el mercado más allá de los jugadores activos y crear un ecosistema auto-sostenible.
*   **Productos a Lanzar:** **Vorpal Worldforge** (Gratuito y a la carta) y el **Mercado de Creadores**.
*   **Racional Estratégico:**
    Con un producto viable y una comunidad establecida, el siguiente paso es la expansión. Vorpal Worldforge atrae a una nueva demografía (escritores, diseñadores) que antes no teníamos. Simultáneamente, el Mercado de Creadores transforma el modelo de valor: ya no solo proveemos herramientas, sino que facilitamos una economía. Cada nueva plantilla o aventura subida al mercado por un creador aumenta el valor de la plataforma para todos los demás usuarios. Este es el "efecto de red" que crea un foso competitivo duradero.
*   **Métricas Clave de Éxito:** Ingresos por ventas en el mercado, número de creadores activos, crecimiento de la base de usuarios de Worldforge.

#### Fase 4: La Optimización - Maximizar el Valor del Ecosistema
*   **Foco Estratégico:** Aumentar el Valor de Vida del Cliente (LTV) y consolidar la oferta de productos.
*   **Productos a Lanzar:** Suscripciones **"Worldforge Pro"** y **"Vorpal Ultimate Bundle"**.
*   **Racional Estratégico:**
    En esta fase, la plataforma está madura. El objetivo es ofrecer paquetes de alto valor para nuestros usuarios más comprometidos. La suscripción "Worldforge Pro" sirve al creador profesional, y el "Ultimate Bundle" es la solución definitiva para el GM/Creador que vive dentro de nuestro ecosistema. Esta fase se centra en la retención y en maximizar el ingreso promedio por usuario (ARPU) a través de la conveniencia y el valor combinado.
*   **Métricas Clave de Éxito:** Tasa de adopción de los bundles, ARPU, tasa de retención de suscriptores.

### 10.0 La Visión a Largo Plazo: Las Fronteras Finales

Estas son las metas que guían nuestro desarrollo a largo plazo, transformando a Vorpal de una herramienta líder a un verdadero pilar de la industria.

#### 10.1 Meta de Unificación: El Vorpal VTT (Mesa Virtual)
*   **Visión Estratégica: El Teatro Unificado.** El VTT es el paso que consolida los tres pilares en una experiencia de juego única y fluida. No es una característica más; es la unificación del ecosistema. Su ventaja competitiva no será la cantidad de funciones, sino la **integración nativa perfecta**. Arrastrar un monstruo desde tu Códice de Worldforge a un mapa de batalla en el VTT, donde su ficha se vincula instantáneamente con tu dashboard de GM y es visible para los jugadores en sus fichas de Player, es una experiencia que ninguna plataforma fragmentada puede ofrecer.
*   **Posicionamiento:** El VTT rápido, intuitivo y sin fricciones para el juego online.

#### 10.2 Meta de Innovación: "The Oracle Engine" (El GM por IA)
*   **Visión Estratégica: La Frontera de la Innovación.** Esta es la meta que nos posiciona como un líder tecnológico. "The Oracle Engine" aborda el mayor cuello de botella del hobby: la necesidad de un GM humano para cada partida. Al permitir experiencias de rol en solitario de alta calidad, abrimos un mercado completamente nuevo para jugadores que quieren probar un personaje, jugar cuando su grupo no puede reunirse, o simplemente disfrutar de una historia interactiva. Es la evolución final de una herramienta de soporte a una plataforma de creación de experiencias.
*   **Posicionamiento:** La experiencia de rol en solitario más inmersiva y accesible del mercado.

## VI. El Plan de Despliegue Estratégico y la Visión a Largo Plazo

### 9.0 El Roadmap de Despliegue Fásico

El desarrollo de Vorpal se abordará como una secuencia de fases estratégicas. Cada fase se construye sobre el éxito de la anterior, permitiendo que el proyecto crezca de forma orgánica, valide sus hipótesis de mercado y genere valor antes de comprometer recursos en la siguiente etapa. Este enfoque es flexible y prioriza la construcción de un ecosistema sostenible.

#### Fase 1: La Fundación - Construir la Base de la Pirámide
*   **Foco Estratégico:** Adquisición de masa crítica y validación del producto principal.
*   **Productos a Lanzar:** **Vorpal Player** (Versión Gratuita y Suscripción "Plus").
*   **Racional Estratégico:** La base de cualquier ecosistema exitoso es su comunidad. Al comenzar con la mejor herramienta gratuita para el segmento de usuarios más grande (los jugadores), logramos tres objetivos: 1) Creamos nuestro motor de adquisición de usuarios. 2) Establecemos la marca Vorpal como sinónimo de calidad y facilidad de uso. 3) Construimos la base sobre la cual se apoyarán todas las futuras ofertas de monetización. El éxito en esta fase no se mide en ingresos, sino en adopción.

#### Fase 2: La Viabilidad - Monetizar al Usuario Motivado
*   **Foco Estratégico:** Probar la viabilidad del modelo de negocio principal y establecer ingresos recurrentes.
*   **Productos a Lanzar:** **Vorpal GM** (Versión Gratuita de Prueba y Suscripción "GM Pro").
*   **Racional Estratégico:** El Director de Juego es el usuario con el "dolor" más agudo (falta de tiempo, complejidad) y, por lo tanto, el más motivado para pagar por una solución. Esta fase se enfoca en convertir la base de GMs de nuestra comunidad existente, probando que el mercado está dispuesto a pagar por valor. El éxito aquí valida el modelo de negocio.

#### Fase 3: La Expansión - Crear el Efecto de Red
*   **Foco Estratégico:** Expandir el mercado más allá de los jugadores activos y crear un ecosistema auto-sostenible.
*   **Productos a Lanzar:** **Vorpal Worldforge** (Gratuito y a la carta) y el **Mercado de Creadores**.
*   **Racional Estratégico:** Con un producto viable, el siguiente paso es la expansión. Worldforge atrae a una nueva demografía (escritores, diseñadores). Simultáneamente, el Mercado de Creadores transforma el modelo de valor: ya no solo proveemos herramientas, sino que facilitamos una economía, creando un foso competitivo duradero.

#### Fase 4: La Consolidación y Unificación - La Mesa Virtual
*   **Foco Estratégico:** Unificar el ecosistema en una experiencia de juego completa y expandir el mercado al juego online.
*   **Producto a Lanzar:** El **Vorpal VTT (Mesa Virtual)**.
*   **Racional Estratégico:** El VTT es el paso que consolida los tres pilares. Su ventaja competitiva no será la cantidad de funciones, sino la **integración nativa perfecta** con todo el contenido creado en el ecosistema (personajes de Player, mundos de Worldforge, campañas de GM). Esto nos posiciona para capturar una porción del mercado de juego online.

### 10.0 La Visión Final (Fase 5 y más allá): La Capa de IA Simbiótica

La meta final de Vorpal es evolucionar de una herramienta de gestión a un **socio creativo simbiótico**. Esto se logra a través de la integración profunda de una capa de inteligencia artificial que potencia, pero no reemplaza, la creatividad humana en todo el ecosistema.

#### 10.1 IA en Vorpal Worldforge: El "Motor Génesis"
El rol de la IA en Worldforge es asistir en la creación y estructuración de ideas desde cero.
*   **Diálogo Creativo (Chat-to-Structure):** Un asistente conversacional que ayuda al usuario a desarrollar sus ideas y luego rellena automáticamente las fichas estructuradas (Sistemas de Magia, Facciones, etc.) con los detalles discutidos.
*   **Generación de Contenido Estructurado:** Relleno inteligente de detalles secundarios en las fichas a partir de un concepto central proporcionado por el usuario.
*   **Visualizador de Mundos:** Generación de imágenes conceptuales por IA directamente desde las descripciones de PNJs, lugares u objetos.

#### 10.2 IA en Vorpal GM: El "Motor de Improvisación"
El rol de la IA en Vorpal GM es ser un asistente de improvisación en tiempo real durante la partida.
*   **Creación de Adversarios sobre la Marcha:** Generación instantánea de fichas de monstruos y PNJs con estadísticas balanceadas para el nivel del grupo.
*   **Ayuda Descriptiva Dinámica:** Generación de descripciones de ambientes y situaciones para ayudar al GM a superar bloqueos narrativos.
*   **Relleno de Contenido Dinámico:** Creación instantánea de rumores, inventarios de tiendas, nombres, etc.

#### 10.3 IA en Vorpal Player: El "Motor de Persona"
El rol de la IA para el jugador es profundizar su conexión con el personaje y su historia.
*   **Asistente de Creación de Personajes:** Ayuda en la generación de trasfondos, rasgos de personalidad y la "voz" del personaje a partir de un concepto.
*   **"The Oracle Engine" (El GM Solitario):** La culminación de la IA para el jugador, permitiendo experiencias de rol en solitario. El Oráculo podrá dirigir tanto módulos pre-hechos como aventuras personalizadas utilizando los mundos creados por los usuarios en Worldforge.

#### 10.4 La Culminación: El VTT Aumentado por IA
El Vorpal VTT es donde todas estas capas de IA convergen. Un GM podrá usar el "Motor Génesis" para crear visuales, el "Motor de Improvisación" para generar encuentros en tiempo real, y los jugadores podrán usar el "Motor de Persona" para obtener inspiración, todo dentro de una única interfaz de juego unificada.


### **Apéndice A: La Filosofía del Lienzo Creativo - Principios de Diseño y Arquitectura de Vorpal**

#### **1. Introducción**

Este documento establece los principios de diseño y la arquitectura fundamental para todas las herramientas creativas dentro del ecosistema Vorpal. Sirve como el *blueprint* para el desarrollo de módulos como Vorpal Worldforge y las futuras fichas de personaje interactivas. Nuestro objetivo es crear una experiencia de usuario que sea un socio en la creatividad, guiando al usuario sin imponerle una estructura rígida.

#### **2. Principios Fundamentales de Diseño**

Todas las herramientas creativas de Vorpal se construirán sobre tres principios irrenunciables:

*   **Principio 1: El Lienzo Inteligente.** La interfaz principal para la creación de contenido es un lienzo visual e interactivo. Los conceptos y datos se representan como nodos en este lienzo, permitiendo al usuario organizar sus ideas de forma espacial y lógica, reflejando el proceso de pensamiento creativo.

*   **Principio 2: La Estructura como Sugerencia, no Sentencia.** Ofrecemos plantillas de inicio y estructuras lógicas como el mejor punto de partida posible. El propósito de estas plantillas es guiar y acelerar el proceso creativo. Sin embargo, el usuario siempre mantiene el control absoluto.

*   **Principio 3: Modularidad Absoluta.** El usuario tiene la capacidad de modificar cada aspecto del lienzo. Esto incluye renombrar nodos y campos, añadir o eliminar campos dentro de un nodo, crear nuevos tipos de nodos desde cero y guardar sus configuraciones personalizadas como plantillas reutilizables.

#### **3. La Arquitectura de Interacción del Lienzo**

La funcionalidad del Lienzo Inteligente se basa en dos mecanismos clave que fomentan la creación guiada y el descubrimiento orgánico:

*   **Conexiones Explícitas:** Los usuarios establecen relaciones lógicas entre los nodos dibujando conexiones visuales. Estas conexiones pueden ser etiquetadas para definir la naturaleza de la relación (ej: "Requiere", "Causa", "Potencia", "Limita a"). Esto crea un mapa visual y comprensible de la estructura del contenido.

*   **Sugerencias de Conexión:** La herramienta asiste proactivamente al usuario. Desde los nodos existentes, emanan "sugerencias de conexión" (representadas como líneas discontinuas) que proponen la creación de nodos lógicamente relacionados. Al interactuar con una sugerencia, se crea automáticamente el nuevo nodo y su conexión, agilizando el flujo de trabajo y enseñando las buenas prácticas de la creación estructurada.
