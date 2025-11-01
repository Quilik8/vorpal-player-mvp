# REGISTRO TÉCNICO DEL PROYECTO: VORPAL BUILDER

## 1. Objetivo del Proyecto

El objetivo es establecer un entorno de desarrollo automatizado, estable y reproducible, capaz de ejecutar scripts de Python que utilizan el framework de agentes de IA `crewai` para procesar una serie de documentos de texto.

---

## 2. Historial de Estrategias y Diagnóstico Evolutivo

Este registro documenta el proceso de depuración, los enfoques intentados, el análisis de sus fallos y la arquitectura de la solución final.

### Intento #1: Entorno Local en Windows (Diagnóstico Inicial)

*   **Estrategia:** Configuración de un entorno Python estándar (`venv`) en Windows con instalación de paquetes vía `pip`.
*   **Resultado:** Fallo catastrófico debido a errores de compilación (`C++`, `Rust`) y permisos de sistema (`WinError`).
*   **Lección Aprendida #1:** La instalación de paquetes de IA con dependencias binarias complejas es inherentemente frágil en un entorno Windows estándar. La compilación local no es una estrategia robusta.

### Intento #2: Pivote a Entorno Local Híbrido (Éxito Parcial Validado)

*   **Estrategia:** Se adoptó `Miniconda` para gestionar el entorno y las dependencias con binarios pre-compilados. Se utilizó un enfoque híbrido: `conda install` para las dependencias pesadas (`langchain-google-genai`) y `pip install` para los paquetes no disponibles en el catálogo de Conda (`crewai`).
*   **Resultado:** **Éxito.** Se logró un entorno funcional localmente en Windows.
*   **Lección Aprendida #2:** La estrategia híbrida (Conda para la base + Pip para los paquetes específicos de PyPI) es una arquitectura válida y funcional para superar los problemas de compilación en Windows. **Este fue el único enfoque que produjo un resultado positivo y se convirtió en la base para la solución final.**

### Intento #3: Transición a la Nube con Metodologías Incorrectas (Ciclo de Fallos)

*   **Estrategia:** Se intentó replicar el entorno en la nube usando GitHub Codespaces para mejorar la reproducibilidad. Sin embargo, se abandonó la lógica del "éxito híbrido" y se intentaron métodos de configuración puristas.
    *   **Sub-intento 3.1 (Pip/Requirements):** Se intentó usar `pip` con un archivo `requirements.txt`. Falló por conflictos de dependencias irresolubles.
    *   **Sub-intento 3.2 (Poetry):** Se intentó usar `Poetry` con un archivo `pyproject.toml`. Falló por el mismo motivo: conflictos lógicos entre las versiones de `crewai` (que requería el ecosistema antiguo de `langchain v0.1.x`) y `langchain-google-genai` (que requería el ecosistema moderno de `langchain v0.2.x`).
*   **Resultado:** Fracaso total. El proceso entró en un ciclo de `ResolutionImpossible`, demostrando que intentar adivinar una combinación compatible de paquetes es una estrategia inviable.
*   **Lección Aprendida #3:** El problema no es la herramienta (`pip`, `Poetry`, `Conda`), sino el **blueprint** (el archivo de configuración). Intentar mezclar paquetes de ecosistemas tecnológicos incompatibles está destinado al fracaso.

---

## 3. Estrategia Final Exitosa: Entorno Híbrido en un Contenedor Declarativo

Esta es la arquitectura final, estable y verificada que está actualmente en uso.

### 3.1. Filosofía de la Solución

La solución se basa en una única premisa: **replicar la lógica del "Intento #2" (el único exitoso) dentro de un entorno definido como código (`devcontainer`) para lograr la robustez del enfoque híbrido y la reproducibilidad de la nube.**

### 3.2. Arquitectura Técnica

*   **Plataforma de Ejecución:** GitHub Codespaces.
*   **Tecnología de Contenedorización:** `Dev Containers`.
*   **Blueprint del Entorno (`.devcontainer/devcontainer.json`):**
    1.  **Imagen Base:** Se utiliza `mcr.microsoft.com/devcontainers/miniconda`. Este es el pilar de la solución. En lugar de una imagen de Python genérica, se parte de una que ya contiene un entorno `Conda` funcional, eliminando la necesidad de instalarlo.
    2.  **Comando de Construcción (`postCreateCommand`):** Se utiliza un único comando que encapsula la lógica híbrida: `conda install ... && pip install ...`.
        *   La parte de `conda install` establece la base de dependencias pesadas y binarias.
        *   La parte de `pip install` completa el entorno con los paquetes específicos de PyPI.
*   **Gestión de Dependencias:** Se ha eliminado la necesidad de `requirements.txt` o `pyproject.toml`. Las dependencias están ahora declaradas **directamente** en el comando de construcción del `devcontainer.json`, creando un sistema autocontenido.

### 3.3. Verificación

*   **Resultado:** La construcción del Codespace utilizando esta configuración finalizó con éxito (`exit code 0`).
*   **Validación:** La ejecución de un script de prueba (`test_environment.py`) dentro del entorno final confirmó que todas las librerías (`crewai`, `langchain-google-genai`, `python-dotenv`) están instaladas, son importables y funcionales para establecer una conexión con la API de Google.

---

## 4. Estado Actual y Próximos Pasos

*   **Estado Actual:** Se ha establecido con éxito un entorno de desarrollo automatizado, estable y reproducible. La fase de configuración de la infraestructura ha concluido.
*   **Próxima Acción:** El siguiente paso es volver al objetivo original del proyecto: la creación y ejecución del script de automatización (`generar_plan.py`) para procesar los documentos del proyecto Vorpal.