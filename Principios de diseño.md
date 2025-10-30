### **Filosofía y Arquitectura del Ecosistema de Lienzos Interconectados de Vorpal**

#### **1. Visión General**

El paradigma central de las herramientas creativas de Vorpal es el **Ecosistema de Lienzos Interconectados**. Esta arquitectura está diseñada para funcionar como un socio en el proceso creativo, proporcionando una estructura visual e inteligente que guía al usuario sin restringir su libertad. Cada componente del mundo de un usuario es un bloque de construcción modular que vive dentro de un lienzo dedicado y puede ser conectado a cualquier otro componente en todo el ecosistema.

#### **2. Principios Fundamentales de la Arquitectura**

Nuestra arquitectura se basa en tres principios fundamentales que definen la experiencia del usuario:

*   **Principio 1: Ecosistema de Lienzos Especializados.** Cada blueprint principal (Sistemas Mágicos, Facciones, Personajes, etc.) reside en su propio lienzo dedicado. Esto permite al usuario enfocarse en una tarea creativa a la vez, en un espacio de trabajo limpio y contextual. La herramienta se adapta al usuario, presentando solo la información y las opciones relevantes para el componente que está creando.

*   **Principio 2: Conectividad Profunda y Contextual.** La potencia del ecosistema reside en su capacidad para crear conexiones lógicas entre lienzos. Un usuario puede establecer un enlace desde un nodo específico en un lienzo a otro nodo específico en un lienzo diferente.
    *   **Ejemplo de Aplicación:** Desde el **Blueprint de un Personaje**, un usuario puede enlazar la habilidad "Bola de Fuego" directamente al **Nodo de Poder** "Bola de Fuego" dentro del **Blueprint del Sistema Mágico** "Piromancia". Al interactuar con este enlace, la aplicación navegará al lienzo de Piromancia y enfocará la vista directamente en el nodo conectado, mostrando instantáneamente todas sus reglas y relaciones.

*   **Principio 3: El Lienzo como Interfaz Primaria de Creación.** La interacción principal del usuario es visual y espacial. La creación de contenido se realiza directamente sobre el lienzo, construyendo y organizando nodos como si fueran ideas en una pizarra. La estructura textual es una propiedad del nodo, pero el acto de creación y organización es inherentemente visual, reflejando el proceso natural del pensamiento creativo.

#### **3. Componentes Clave de la Interfaz del Lienzo**

La interacción dentro de cada lienzo se materializa a través de los siguientes componentes:

*   **Nodos Temáticos y Únicos:** Cada pieza de información fundamental es un "Nodo". Para garantizar la claridad en todo el ecosistema, los nodos tienen nombres específicos y temáticos en lugar de genéricos. Por ejemplo, el nodo principal de un sistema mágico es el **"Corazón del Sistema"**; el de una facción es la **"Carta Magna"**. Cada nodo es un contenedor de datos estructurados (campos, descripciones, etc.).

*   **Conexiones Explícitas y Etiquetadas:** La relación entre nodos se establece mediante conexiones visuales dibujadas por el usuario. Estas conexiones son objetos interactivos que pueden ser etiquetados para definir la naturaleza precisa de la relación lógica (ej: "Requiere", "Causa", "Potencia", "Es Aliado de"). Esto crea una gramática visual que hace que el mapa del mundo sea legible y lógicamente coherente.

*   **Sugerencias de Conexión Proactivas:** El lienzo actúa como un socio inteligente. Desde los nodos existentes, emanan "sugerencias de conexión" (representadas visualmente, por ejemplo, con líneas discontinuas) que proponen la creación de nodos lógicamente relacionados. Al interactuar con una sugerencia, se presenta un menú contextual que permite crear el nuevo nodo y su conexión en un solo paso. Esta funcionalidad guía al usuario, acelera el flujo de trabajo y enseña las mejores prácticas de la creación estructurada de forma orgánica.

#### **4. La Filosofía de Implementación**

El principio que gobierna la implementación de cada blueprint y cada nodo es inmutable:

**La Estructura como Sugerencia.**

Ofrecemos plantillas de inicio y estructuras lógicas como el punto de partida más eficaz. Sin embargo, el usuario final siempre conserva la soberanía sobre su lienzo creativo. La modularidad es absoluta, permitiendo al usuario renombrar nodos, añadir o eliminar campos, y crear nuevos tipos de nodos desde cero para adaptar la herramienta perfectamente a las necesidades únicas de su mundo.


    

### **Apéndice B: Registro de Configuración del Entorno de Desarrollo**

#### **1. Stack Tecnológico y Herramientas Principales**

Este registro documenta el conjunto de herramientas y tecnologías seleccionadas y configuradas para el desarrollo del proyecto Vorpal.

*   **Entorno de Desarrollo Integrado (IDE):**
    *   **Visual Studio Code (VS Code):** Se utiliza como el editor de código principal.
    *   **Extensión Requerida:** Se ha instalado la extensión oficial de **Python de Microsoft** para permitir la integración del lenguaje y la selección de intérpretes.

*   **Gestor de Entornos y Paquetes:**
    *   **Miniconda:** Se ha instalado como el gestor principal para crear y gestionar entornos de desarrollo aislados y estables. Esta herramienta fue seleccionada para resolver problemas de compilación de dependencias complejas en el sistema operativo Windows.
    *   **Entorno de Proyecto:** Se ha creado un entorno Conda dedicado llamado **`vorpal_env`**, configurado con **Python 3.12** para garantizar un equilibrio óptimo entre modernidad y compatibilidad con el ecosistema de librerías de IA.

*   **Modelo de Lenguaje de IA:**
    *   El motor de inteligencia para el sistema de agentes es el modelo **Google Gemini 2.5 Pro**, accedido a través de su API oficial.


### **Filosofía de Diseño Vorpal: Blueprints Adaptativos y Niveles de Detalle (LoD)**

#### **1. Principio Fundamental: Diseño Basado en el Propósito del Usuario**

El núcleo de las herramientas creativas de Vorpal es la adaptabilidad. En lugar de ofrecer una única plantilla rígida, el sistema se amolda a la intención creativa del usuario a través de los **Niveles de Detalle (LoD)**.

Al iniciar la creación de un nuevo blueprint (un sistema mágico, una facción, etc.), al usuario se le presenta una selección de LoD. Cada nivel no solo varía en complejidad, sino que está diseñado para un **caso de uso** específico. La selección de un LoD carga en el lienzo una plantilla de inicio con un conjunto de nodos y campos predefinidos y adaptados a ese propósito, respetando siempre el principio de que **la estructura es una sugerencia.**

---

#### **2. Blueprint de Sistemas Mágicos: Espectro de Seis Niveles de Detalle**

**LoD 1: Magia Ornamental**
*   **Propósito:** Para magias de fondo, de cuentos de hadas o estéticas, donde la sensación es más importante que la mecánica.
*   **Plantilla de Inicio:** Carga un único nodo, el `**Corazón del Sistema**`, con dos campos:
    *   `Nombre del Sistema`
    *   `Descripción General / Temática`

**LoD 2: Magia Blanda Simple**
*   **Propósito:** Para sistemas donde la magia es misteriosa y sus capacidades son difusas, centrándose en el *qué* puede hacer de forma general.
*   **Plantilla de Inicio:** Carga el `**Corazón del Sistema**` y un `**Nodo de Poder**` genérico para describir las capacidades principales. No se incluyen nodos de reglas.

**LoD 3: Magia Blanda Compleja**
*   **Propósito:** Para magias blandas con poderes más definidos, aunque las reglas de su funcionamiento sigan siendo un misterio.
*   **Plantilla de Inicio:** Carga el `**Corazón del Sistema**`, múltiples `**Nodos de Poder**` (con campos para `Descripción del Efecto` y `Poseedor Conocido`), y un `**Nodo de Repercusión**` simple para definir consecuencias narrativas.

**LoD 4: Magia Blanda con Toques Duros**
*   **Propósito:** Define claramente *quién* puede usar la magia o *qué* se necesita para usarla, aunque los límites y costes sigan siendo difusos.
*   **Plantilla de Inicio:** Introduce nodos de reglas específicos. Carga nodos de `**Corazón del Sistema**`, `**Poder**`, y crucialmente, un `**Nodo de Aptitud**` (para definir requisitos innatos) y/o un `**Nodo de Denominación**` (para definir grupos de usuarios).

**LoD 5: Magia Dura No Sistematizada**
*   **Propósito:** Para sistemas con reglas claras y definidas para cada poder individual, pero sin una gran teoría unificadora. Típico de muchos sistemas de TTRPG.
*   **Plantilla de Inicio:** Carga múltiples `**Nodos de Poder**`, cada uno con sugerencias para conectar sus propios nodos de reglas de `**Coste**`, `**Activación**` y `**Manifestación**`.

**LoD 6: Magia Sistematizada / Científica Dura**
*   **Propósito:** Para diseñar sistemas de magia que funcionan como una ciencia, con leyes universales, reglas interconectadas y una lógica interna coherente.
*   **Plantilla de Inicio:** Carga el blueprint completo. Todos los tipos de nodos (`Corazón del Sistema`, `Denominación`, `Poder` y los 6 tipos de `Reglas`) están disponibles, con **Sugerencias de Conexión** pre-activadas para guiar al usuario en la construcción de un sistema totalmente interconectado.

---

#### **3. Blueprint de Facciones: Espectro de Cuatro Niveles de Detalle**

**LoD 1: El Gancho de Aventura**
*   **Propósito:** Crear rápidamente una facción simple para una aventura o encuentro específico.
*   **Plantilla de Inicio:** Carga un único nodo, el `**Núcleo de la Facción**`, con tres campos:
    *   `Nombre de la Facción`
    *   `Tipo` (Gremio, Tribu, Culto)
    *   `Objetivo Inmediato`

**LoD 2: El Poder en Juego**
*   **Propósito:** Diseñar una facción principal y recurrente en una campaña, definiendo su lugar en el mundo.
*   **Plantilla de Inicio:** Carga un lienzo con los nodos estándar interconectados: `**Núcleo de la Facción**`, `**Ideología**`, `**Estructura**` y `**Recursos**`.

**LoD 3: La Simulación de Organización**
*   **Propósito:** Para un worldbuilding de máxima profundidad, simulando el funcionamiento interno de la facción.
*   **Plantilla de Inicio:** Carga todos los nodos del LoD 2 y añade nodos granulares como `**Logística y Cadena de Suministro**`, `**Políticas Internas y Sub-facciones**`, y `**Doctrina Detallada (Militar/Económica)**`.

**LoD 4: La Facción Jugable**
*   **Propósito:** Diseñar una facción con mecánicas de juego, como para un juego de estrategia o gestión.
*   **Plantilla de Inicio:** Similar al LoD 3, pero con un enfoque en la mecánica. Añade nodos como `**Acciones de Facción**`, `**Árbol de Mejoras/Tecnología**` y `**Condiciones de Victoria**`.

---

#### **4. Blueprint de Fichas de Personaje: Espectro de Tres Niveles de Detalle**

**LoD 1: El Boceto de PNJ**
*   **Propósito:** Crear un Personaje No Jugador funcional y memorable para una interacción rápida.
*   **Plantilla de Inicio:** Carga un único nodo, el `**Perfil del Personaje**`, con campos narrativos:
    *   `Nombre`
    *   `Concepto Principal`
    *   `Motivación Principal`
    *   `Voz / Manierismo`

**LoD 2: El Héroe de Campaña**
*   **Propósito:** La ficha de personaje estándar para un Personaje Jugador o un PNJ principal en un TTRPG.
*   **Plantilla de Inicio:** Carga un lienzo con los nodos clásicos interconectados: `**Perfil**`, `**Atributos**`, `**Habilidades**`, `**Inventario**` y `**Rasgos y Dotes**`.

**LoD 3: El Protagonista de Novela**
*   **Propósito:** Para un desarrollo de personaje profundo, ideal para escritores o jugadores de rol narrativo.
*   **Plantilla de Inicio:** Carga todos los nodos del LoD 2 y añade nodos puramente narrativos como `**Perfil Psicológico**` (miedos, vicios), `**Red de Relaciones**` (mapa visual de contactos) y `**Arco del Personaje**`.

---

#### **5. Plantillas de Inicio Basadas en Sistemas de Juego**

Como una alternativa a los LoD genéricos, el blueprint de Fichas de Personaje ofrecerá una selección de plantillas pre-configuradas para sistemas de TTRPG populares. Estas plantillas cargarán un lienzo con los nodos, campos y conexiones lógicas específicas de ese sistema.

*   **Ejemplo - D&D 5e:** Cargaría nodos para los 6 `Atributos` (`Fuerza`, `Destreza`, etc.), un nodo de `Habilidades` con las 18 habilidades oficiales ya listadas y conectadas a su atributo correspondiente, un nodo de `Clase y Nivel`, y un `Libro de Hechizos`.
*   **Ejemplo - La Llamada de Cthulhu:** Cargaría nodos para `Características` (FUE, DES, etc.), `Cordura (COR)`, `Puntos de Magia`, y un nodo de `Habilidades` con la lista de habilidades del sistema (Buscar Libros, Mitos de Cthulhu, etc.).

3.1. Ejemplo Práctico del Flujo de Ejecución Local

Para evitar ambigüedades, es crucial entender que el Socio de IA (Gemini) no ejecuta el código de forma remota. Su función es la de un generador de código y un consultor técnico. El Director del Proyecto (Humano) mantiene el control total de la ejecución en su entorno de desarrollo local.
El ciclo de trabajo para una tarea de automatización (como generar el plan de proyecto detallado) es el siguiente:

Fase 1: Preparación de Inputs (Director): El Director crea o reúne los archivos de entrada necesarios en su carpeta de trabajo local. Por ejemplo, guia Vorpal para estructura.md y DIRECTIVAS_MAESTRAS.md.
Fase 2: Generación del Script de Automatización (Colaboración): El Director solicita al Socio de IA el script de Python necesario para la tarea. El Socio de IA analiza los requisitos, las directivas y los inputs, y entrega el código fuente completo de un script de Python (ej. generar_plan.py).
Fase 3: Ejecución Local (Director): El Director guarda el script .py proporcionado en su carpeta de trabajo (Vorpal_Builder). A continuación, abre una terminal en VS Code, activa su entorno Conda (conda activate vorpal_env) y ejecuta el script directamente en su máquina (python generar_plan.py).
Fase 4: Resultado y Validación (Local): El script se ejecuta en el PC del Director. Utiliza las librerías instaladas en vorpal_env, carga la clave de API desde el archivo .env local, lee los archivos .md del disco duro, se comunica con la API de Gemini, y guarda los archivos de salida (.md detallados) directamente en las carpetas locales. El Director entonces revisa y valida los resultados.

